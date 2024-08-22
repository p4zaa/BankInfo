from BankInfo import banks_info

def get_bank_info(country_code, bank_code, value=None):
    if value:
        data = banks_info.get(country_code).get(bank_code).get(value)
    else:
        data = banks_info.get(country_code).get(bank_code)
    return data