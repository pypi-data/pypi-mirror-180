from dataclasses import dataclass
import decimal, json
from datetime import datetime
import gspread, json, google.auth, dataclasses
from googleapiclient.discovery import build
from gspread import Spreadsheet, Worksheet
from datetime import datetime
import wdig.config as config
import pandas as pd
from gspread_formatting import set_column_widths, format_cell_ranges, format_cell_range, get_conditional_format_rules
from gspread_formatting.models import CellFormat, TextFormat
from wdig.queries import transactions_dataframe, merchant_type_summary, get_transactions_grouped_by_budget_tag, BudgetTagGroups


@dataclass
class GoogleWorkspace:
    drive: object
    gspread: gspread.Client
    is_dev: bool


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])  # https://stackoverflow.com/a/1960649
        return super(EnhancedJSONEncoder, self).default(o)

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


# budget = {'income': 9600, 'fixed': -1798.74, 'variable': -3108.33, 'mortgage': -2594.98, 'savings': -950, 'donation': -293.33, 'bank fees': -95, 'debt': -340}


# https://developers.google.com/drive/api/v3/about-sdk
# https://developers.google.com/sheets/api/guides/concepts
# https://docs.gspread.org/en/v3.7.0/index.html


_title_cell_format = CellFormat(
    textFormat=TextFormat(
        bold=True,
        foregroundColor={
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
        },
    ),
    horizontalAlignment="CENTER",
    backgroundColor={
        "red": 1.0,
        "green": 0.0,
        "blue": 0.0
    },
)

_google_workspace = None


def google_connect() -> GoogleWorkspace:
    global _google_workspace
    if _google_workspace is None:
        SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
        creds, project = google.auth.load_credentials_from_file(
            config.google_auth_filepath, scopes=SCOPES
        )
        drive_service = build("drive", "v3", credentials=creds)
        gspread_service = gspread.service_account(filename=config.google_auth_filepath)
        _google_workspace = GoogleWorkspace(drive_service, gspread_service, config.development)
    return _google_workspace


def get_or_create_sheet(sheet_title: str, first_worksheet_title: str = 'Sheet1') -> Worksheet:
    google = google_connect()
    if google.is_dev:
        sheet_title += ' DEV'

    sheet = next(iter(google.gspread.openall(title=sheet_title)), None)
    if sheet is None:
        sheet = google.gspread.create(sheet_title, folder_id=config.google_wdig_folder_id)
        worksheet = sheet.get_worksheet(0)
        worksheet.update_title(first_worksheet_title)
    return sheet


def update_empty_sheet():
    sheet = get_or_create_sheet('wdig - test sheet', first_worksheet_title='status')
    worksheet = sheet.get_worksheet(0)
    worksheet.update([['last updated:', datetime.now().strftime('%x'), datetime.now().strftime('%X')]])

def get_transaction_sheet(year: str = '2022') -> Worksheet:
    sheet = get_or_create_sheet(f'wdig - {year}', first_worksheet_title='categories')
    return sheet

def update_transaction_sheet(year: str = '2022') -> None:
    sheet = get_transaction_sheet(year)

    df = transactions_dataframe()
    df = df[df['period_year'] == year]
    df['tran_date'] = pd.to_datetime(df['tran_date']).dt.strftime('%d %b')
    df = df[['period_month', 'tran_date', 'category', 'budget_category', 'budget_tag', 'description', 'amount', 'tran_type', 'account_name', 'bank_name', 'merchant_type', 'tran_id', 'file_name']]

    _update_category_worksheet(df, _create_or_replace_worksheet(sheet, 'categories'))
    _update_transaction_worksheet(df, _create_or_replace_worksheet(sheet, 'transactions'))
    # _update_merchant_type_summary_worksheet(_create_or_replace_worksheet(sheet, 'merchant types'), year)
    _update_budget_worksheet(_create_or_replace_worksheet(sheet, 'budget', rows=100), year)


def _update_merchant_type_summary_worksheet(mt_worksheet: Worksheet, year: str) -> None:
    results = merchant_type_summary(year)
    mt_worksheet.update(results)
    format_cell_ranges(mt_worksheet, [("1", _title_cell_format)])
    mt_worksheet.set_basic_filter()
    set_column_widths(mt_worksheet, [('A', 116), ('B', 122), ('C', 96), ('D', 111)])
    format_cell_range(mt_worksheet, 'D', CellFormat(numberFormat={'type': 'CURRENCY', 'pattern': '"$"#,##0.00'}))
    mt_worksheet.freeze(rows=1)


def _update_transaction_worksheet(df_trans: pd.DataFrame, year_worksheet: Worksheet):
    values = json.loads(json.dumps(df_trans.values.tolist(), default=str))
    year_worksheet.update([df_trans.columns.values.tolist()] + values)

    format_cell_ranges(year_worksheet, [("1", _title_cell_format)])
    year_worksheet.set_basic_filter()
    set_column_widths(year_worksheet, [('A', 116), ('B', 87), ('C', 87), ('D', 122), ('E', 122), ('F', 319), ('G', 75), ('H', 87), ('I', 156), ('J', 100), ('K', 262), ('L', 391)])
    format_cell_range(year_worksheet, 'F', CellFormat(numberFormat={'type': 'CURRENCY', 'pattern': '"$"#,##0.00'}))
    year_worksheet.freeze(rows=1)


def _update_category_worksheet(df_trans: pd.DataFrame, cat_worksheet: Worksheet):
    df_cat = df_trans.groupby(['period_month', 'category']).agg(
        count=pd.NamedAgg(column='amount', aggfunc='count'),
        amount=pd.NamedAgg(column='amount', aggfunc='sum')
    )
    df_cat.reset_index(inplace=True)

    df_cat = df_cat.pivot(
        index=["period_month"], columns="category", values="amount"
    )
    df_cat.reset_index(inplace=True)
    df_cat.fillna(0, inplace=True)
    df_cat['remaining'] = df_cat.sum(axis=1)

    values = json.loads(json.dumps(df_cat.values.tolist(), default=str))
    cat_worksheet.update('A2', [df_cat.columns.values.tolist()] + values)
    format_cell_ranges(cat_worksheet, [("2", _title_cell_format)])


def _update_budget_worksheet(budget_worksheet: Worksheet, year: str):
    budget = {
        'fixed': {
            'mobile usage': -26,
            'disney': -12.99,
            'school fees': -169,
            'apple': -2,
            'casey gym': -87,
            'google storage+youtube': -24.48,
            'swim lessons': 0,
            'life insurance': -21.26,
            'water': -80,
            'southern cross': -127.86,
            'amazon music': -8.5,
            'city council': -246,
            'recycling': -27.16,
            'orcon': -88,
            'minecraft realm': -5.9,
            'home insurance': -142.07,
            'car insurance': -17.51,
            'backup': -19,
            'netflix': -12.99,
            'onedrive': -3,
            'tkd': -190,
            'school special character': -53,
            'kindy': -120,
            'reading eggs': -14.99,
            'power': -250,
        },
        'debt': {
            'cc payments': -340,
            'bank fees': -20,
            'interest': -75,
        },
        'variable': {
            'groceries': -1300,
            'eating out': -433.33,
            'entertainment & misc': -1083.33,
            'petrol': -108.33,
            'at hop': -100.00,
        },
        'donations': {
            'salvation army': -20,
            'kiva': -40,
            'church': -180,
            'city mission': -60,
        },
        'mortgage': {'mortgage': -2594.98},
        'savings': {'savings': -900},
        'unknown': {'unknown': -1085}
    }

    assert len(budget['fixed']) == 25
    assert len(budget['debt']) == 3
    assert len(budget['unknown']) == 1

    actuals = get_transactions_grouped_by_budget_tag(year)

    rows = []
    rows.append(['category', 'tag', 'budget'])
    for m in range(1, datetime.now().month + 1):
        period = f'{datetime(int(year), m, 1).strftime("%m-%b")}'
        rows[0].append(period)

# TODO add category total row

    for bc in budget.keys():
        print(bc)
        for bt in budget[bc].keys():
            row = [bc, bt, float(budget[bc][bt])]
            for m in range(1, datetime.now().month + 1):
                period = f'{datetime(int(year), m, 1).strftime("%m-%b")}'

                def filter_budget_group(group: BudgetTagGroups) -> bool:
                    if group.period == period and group.budget_category == bc and group.budget_tag == bt:
                        return True

                match = list(filter(filter_budget_group, actuals))
                actual = 0
                if len(match) == 1:
                    actual = match[0].amount
                elif len(match) == 0:
                    actual = 0
                else:
                    raise KeyError(f'too many matches for [{bc}] [{bt}]')
                row.append(float(actual))
            rows.append(row)

    budget_worksheet.update(rows)
    format_cell_ranges(budget_worksheet, [("1", _title_cell_format)])
    budget_worksheet.set_basic_filter()
    budget_worksheet.freeze(rows=1)


def _create_or_replace_worksheet(sheet: Spreadsheet, title: str, rows: int = 10, cols: int = 10) -> Worksheet:
    worksheet = _find_worksheet(sheet, title)
    if worksheet:
        sheet.del_worksheet(worksheet)
    worksheet = sheet.add_worksheet(title=title, rows=rows, cols=cols)
    return worksheet


def _find_worksheet(sheet: Spreadsheet, title: str) -> Worksheet:
    worksheets = sheet.worksheets()
    for ws in worksheets:
        if ws.title == title:
            return ws
    return None


if __name__ == '__main__':
    # _update_budget_worksheet(None, '2022')
    update_transaction_sheet()
