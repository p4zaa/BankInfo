import json

# Parse the JSON string into a Python dictionary
banks = json.loads('BankInfo/banks.json')

def get_bank_info(country_code, bank_code):
    return banks.get(country_code).get(bank_code)