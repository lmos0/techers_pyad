import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    return exchange_rate

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    """
    This function is the entry point of the Currency Converter program.
    It prompts the user to enter the base currency, target currency, and amount to convert.
    It then calculates the converted amount using the exchange rate and displays the result.
    """

    print("Welcome to Currency Converter!")
    base_currency = input("Enter your base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter your target currency (e.g., USD, EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)

    print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
