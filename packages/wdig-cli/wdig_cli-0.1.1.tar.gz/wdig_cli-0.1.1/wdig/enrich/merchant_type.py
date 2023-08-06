from typing import List


class MerchantTypeMatcher:
    def __init__(self, merchant_type: str, keywords: List[str]) -> None:
        self._keywords = keywords
        self._merchant_type = merchant_type

    @property
    def merchant_type(self):
        return self._merchant_type

    def is_match(self, description: str) -> bool:
        for keyword in self._keywords:
            if keyword.lower() in description.lower():
                return True
        return False


def determine_merchant_type(description: str) -> str:
    matchers = [
        MerchantTypeMatcher('groceries', ['new world', 'countdown', 'millwater superette', 'four square', 'Joy Mart']),
        MerchantTypeMatcher('petrol', ['Mobil Red Beach']),
        MerchantTypeMatcher('retail', ['Warehouse', 'ALIEXPRESS']),
        MerchantTypeMatcher('eatingout', ['Hollywood', 'Liquor Spot', 'Pizza Hut', 'Subway', 'China Castle', 'Olivers Cafe', 'Nam Nam', 'Mojo', 'Moreish', 'THE ISLAND GELATO', 'Tabak', 'Montana Catering', 'Starbucks', 'Sals Pizza', 'RED BEACH BAKEHOUSE', 'French Rendez-Vous', 'Wendys', 'Don Kebab', 'St Pierre', 'Devon On The Wharf', 'NO NA BAKERY', 'The Gourmet Food', 'Super Liquor', 'Hanarum', 'The Bakehouse Cafe'])
    ]
    matches = [matcher for matcher in matchers if matcher.is_match(description)]
    if len(matches) > 1:
        raise LookupError(f'too many matchers for {description} - found {len(matchers)}')
    elif len(matches) == 1:
        return matches[0].merchant_type
    return 'unknown'
