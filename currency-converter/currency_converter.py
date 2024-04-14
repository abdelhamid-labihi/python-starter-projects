import requests
import pycountry

# Get a list of all currency codes and names
currencies = {
    currency.alpha_3: currency.name
    for currency in pycountry.currencies
}

print("\n~~~~~~\ Welcome to the Currency Converter! ~~~~~~\ \n")

# Get the initial currency from the user
while True:
    init_currency = input("\nEnter an initial currency code: ")
    if init_currency not in currencies:
        print(f"Invalid currency code. Please try again.\n")
        continue
    break

# Get the target currency from the user
while True:
    target_currency = input("Enter a target currency code: ")
    if target_currency not in currencies:
        print(f"Invalid currency code. Please try again.\n")
        continue
    break

# Get the amount from the user
while True:
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("The amount must be a numeric value!\n")
        continue
    if amount <= 0:
        print("The amount must be greater than 0\n")
        continue
    break

# Make the API call
url = ("https://api.apilayer.com/fixer/convert?to="
        + target_currency + "&from=" + init_currency
        + "&amount=" + str(amount))

payload = {}
headers= {
  "apikey": "g9YUi0UZMQr10HS1SiI9Pu2Crt3wnyHb"
}

response = requests.request("GET", url, headers=headers, data = payload)

# Check the status of the response
if response.status_code != 200:
    print("\nSorry, there was a problem. Please try again later.\n")
    quit()

# Extract the converted amount from the response
result = response.json()
converted_amount = result["result"]

# Print the result
print(f"\n{amount} {init_currency} is equal to {converted_amount} {target_currency}.\n")
