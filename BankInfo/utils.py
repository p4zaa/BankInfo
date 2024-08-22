from BankInfo import banks_info

def get_bank_info(country_code, bank_code, value=None):
    # Safely retrieve the bank information
    country_data = banks_info.get(country_code, {})
    bank_data = country_data.get(bank_code, {})
    
    # If a specific value is provided, get that value; otherwise, return the whole bank data
    return bank_data.get(value) if value else bank_data