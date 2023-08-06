from wdig.database import Transaction
from fnmatch import fnmatch


def map_to_variable_budget(tran: Transaction) -> None:
    budget_tag = None

    if tran.description == 'PAY Daehan tkd ;':
        return False

    for m in [
        'AT Hop *',
        'At Hop *',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'at hop'

    for m in [
        'Mobil Red Beach*',
        'Z Greville Rd*',
        'Z Silverdale*',
        'Mobil Red Beach*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'petrol'

    for m in [
        'FAMILY MARKET- OREWA*',
        'Four Square Red Beach*',
        'Imart*',
        'IMART*',
        'ALBANY VEGE*',
        'CANAAN VEGE*',
        'Chowon Butchery*',
        'CHOWON BUTCHERY*',
        'Countdown Akl*',
        'Countdown Albert*',
        'Countdown Online*',
        'Countdown Silverdale*',
        'FOUR SQUARE RED BEAC*',
        'Four Square Red Beach*',
        'Fruit World*',
        'FRUIT WORLD*',
        'Fruit World*',
        'Hanarum Mart*',
        'Imart*',
        'IMART*',
        'Joy Mart*',
        'JOY MART*',
        'MEAT PLAZA*',
        'New World*',
        'New World*',
        'New World*',
        'Pak N Save*',
        'POS W/D FRUIT WORLD*',
        'POS W/D HANYANG*',
        'POS W/D LINK VEGE*',
        'Sams Butchery*',
        'WANG FOOD MARKET*',
        'Wang Food Market*',
        'Warkworth New World*',
        'COUNTDOWN*',
        'Countdown Orewa*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'groceries'

    for m in [
        'Asahi*',
        'Bake And Brew*',
        'BAKE AND BREW*',
        'Bakers Delight*',
        'BAMCHAN-GA*',
        'Blue Elephant*',
        'Brew On Quay*',
        'Burgerfuel Customs*',
        'Cafe Brioche Albany*',
        'Cafe Third Wave*',
        'CENTREWAY DAIRY*',
        'Chargrill 101*',
        'China Castle*',
        'CHINA CASTLE*',
        'City 1 Limited*',
        'CITY 1 LIMITED*',
        'City Convenience*',
        'Coca-Cola Ep Nz*',
        'Custom Mart*',
        'Daruma Sushi*',
        'Dear Coasties*',
        'Devon On The Wharf*',
        'Don Kebab Nz Ltd*',
        'DORURI*',
        'Eat India*',
        'Faridas*',
        'Gloria Jean*',
        'Ground Control Cafe*',
        'GROUND CONTROL CAFE*',
        'Hill Top Dairy*',
        'HOLLYWOOD BAKERY*',
        'Hollywood Bakery*',
        'House Of Boulevard*',
        "INGO'S GERMAN BAKERY*",
        'Jesters-Takapuna*',
        'Kiwi Liquor Silverdale*',
        'Ks Chicken*',
        'Leo Thai Kitchen*',
        'Lieutenant Coffee*',
        'Liquor Spot*',
        'Lord Of The Fries*',
        'Mcdonalds Albany*',
        'Mcdonalds Britomart*',
        'Millies*',
        'Millies Cafe*',
        'Millwater Fine Wines*',
        'Millwater Superette*',
        'MILLWATER SUPERETTE*',
        'Miss Moonshines*',
        'MISS MOONSHINES*',
        'Mojo Little Quay*',
        'Montana Catering*',
        'Moreish Silverdale*',
        'MR BON BAKERY*',
        "MUM'S FOODS NO.2*",
        'Nam Nam Harbour*',
        'NARA SUSHI*',
        'Natural Bake & Coffe*',
        'Nh Liquor*',
        'NO NA BAKERY*',
        'NO1 CHICKEN*',
        'Northern Union*',
        'Ocean Eats*',
        'Olivers Cafe*',
        'Omgoodness Matakana*',
        'Order Meal Ltd*',
        'OREWA BAKERY*',
        'OREWA BEACH FISH*',
        'Paraoa Brewing Co*',
        'Pizza Hut Silverdale*',
        'PIZZA HUT SILVERDALE*',
        'PIZZA HUT WHANGAPARAOA*',
        'POS W/D JAMI JAMI*',
        'POS W/D RED BEACH*',
        'POS W/D St Pierres*',
        'POS W/D WELLBEING*',
        'RED BEACH BAKEHOUSE*',
        'Robert Harris*',
        'Royal Save Mart*',
        'Sals Pizza Fort St*',
        'So French*',
        'SOPHIA DONKATSU*',
        "St Pierre'S Silverdale*",
        'STAR SHOP*',
        'Starks Cafe*',
        'Subway Orewa*',
        'Subway Parnell*',
        'Super Liquor Red Beach*',
        'Subway Orewa*',
        'Subway Parnell*',
        'Super Liquor Red Beach*',
        'THE COFFEE CLUB OREW*',
        'The Coffee Club Orewa*',
        'THE COFFEE CLUB SILV*',
        'The Gourmet Food*',
        'THE ISLAND GELATO*',
        'The White Lady*',
        'Toro Churro Botany*',
        'Wendys Whangaporara*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'eating out'

    for m in [
        'AC ALBANY STADIUM*',
        'Ac Albany Stadium*',
        'Ac Stanmore*',
        'AC STANMORE*',
        'aliexpress*',
        'ALIEXPRESS.COM*',
        'AMAZON WEB SERVICES*',
        'AMCAL SILVERDALE PHA*',
        'AMZN Digital*',
        'Dollartopia*',
        'DR SCISSORS*',
        'Briscoes Silverdale*',
        'Bunnings*',
        'Chemist Warehouse*',
        'Coast Pet Care Chari*',
        'Estuaryarts*',
        'Eventfinda*',
        'EZI*FAILED PAYMENT*',
        'Ezibuy*',
        'EZIBUY*',
        'Farmers Albany*',
        'Fullers Devonport*',
        'Furry Friends Pet*',
        'Game Over Auckland*',
        'Gmarket*',
        'Haggie Yang*',
        'Hallenstein Online*',
        'HARBOUR HOSPICE*',
        'Healthpost*',
        'HEALTHPOST*',
        'HESTIA RODNEY*',
        'Holy Trinty Cathedra*',
        'Huntfish Co New Zealan*',
        'Inflatable World*',
        'Japan Home Mart*',
        'Jeanswest*',
        'Jeanswest.Com*',
        'Jump*',
        'JUMP*',
        'Just Cuts Silverdale*',
        'Kathmandu*',
        'KINDO AUCKLAND*',
        'Kings Plant Barn*',
        'Kmart Albany*',
        'KMART ONLINE*',
        'Life Pharmacy Orewa*',
        'LOOK SHARP ALBANY*',
        'LOTSA GOODIES ALBANY*',
        'Macpac*Silverdale*',
        'Macpac Retail*',
        'MAKASSAR CORNER*',
        'Marine Deals*',
        'Mighty Ape*',
        'NEURON MOBILITY*',
        'NH MALL*',
        'Nz Transport Agency*',
        'NZ TRANSPORT AGENCY*',
        'Nzsale*',
        'NZSALE*',
        'OFFICEMAX AUCKLAND*',
        'OREWA CENTRAL POST*',
        'Orewa Central Post*',
        'PAY*',
        'Paypal *Kmart*',
        'PB TECHNOLOGIES*',
        'PHOTO LIFE STUDIOS*',
        'POS W/D AC STANMORE*',
        'POS W/D Briscoes*',
        'POS W/D Coast Pet Car*',
        'POS W/D DOLLARTOPIA*',
        'Postie - Sil*',
        'Postie Web Store*',
        'Rebel Sport Mt Albert*',
        'Rebel Sport Silverdale*',
        'Red Beach Pharmacy*',
        'SILVERDALE CLINIC*',
        'SPECSAVERS NZ*',
        "St John'S Carpark*",
        'STARZ LIVERPOOL*',
        'STEAM PURCHASE*',
        'SUSHI GALLERY*',
        'Sushi House*',
        'TCS SILVERDALE*',
        'The Civic*',
        'The Doctors Coastcare*',
        'THE DOCTORS RED BEACH*',
        'THE PUMPHOUSE THEATRE*',
        'The Warehouse*',
        'Tm *Ticketmasternz*',
        'TM *TICKETMASTERNZ*',
        'TRADEME*',
        'Trademe*',
        'Udemy*',
        'We-Life*',
        'WE-LIFE*',
        'Whitcoulls Aly*',
        'www.aliexpress.com*',
    ]:
        if fnmatch(tran.description, m):
            budget_tag = 'entertainment & misc'

    if budget_tag:
        tran.budget_tag = budget_tag
        tran.budget_category = 'variable'
        return True


"""
# ----------------------
# what are these?
# JEBI
# jebu kiwibank rev
#  --------------------------------

# Google Auckland ;
# Google Auckland ;
# Google Google          Auckland      Nz
# GOOGLE Google Auckland ;
# GOOGLE Warner Bros Auckland ;

# Rodneykids Ltd         Auckland      Nz
# kingsway junior spor 3ang- ethan
# Kingsway School        Silverdale    Nz
# kingsway junior spor 3ang- ethan
# Kingsway School        Silverdale    Nz

# POS W/D 14.95AUD @ 0.9320 conversion rate ;(INC. $0.40 CURRENCY CONVERSION COMMISSION) Audible Limited AU MELBOURNE
# POS W/D 16.45AUD @ 0.9109 conversion rate ;(INC. $0.45 CURRENCY CONVERSION COMMISSION) Audible Limited AU MELBOURNE
# Audible Limited Au     Melbourne     Au
"""
