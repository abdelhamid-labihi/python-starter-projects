# Python Currency Converter

This is a simple command-line Currency Converter application written in Python. It's a great project for beginners to get started with Python programming.

## Packages Used

- `requests`: This package allows you to send HTTP requests using Python. In this project, it's used to make a GET request to the currency conversion API.

- `pycountry`: This package provides the ISO databases for countries, languages, and currencies. In this project, it's used to get a list of all currency codes and names.

## Code Explanation

The code is organized into several sections:

- **Currency Codes and Names**: The `currencies` dictionary is created using a dictionary comprehension. It loops over all the currency objects provided by `pycountry.currencies` and uses the `alpha_3` attribute (a three-letter code representing the currency) as the key and the `name` attribute (the full name of the currency) as the value.

```python
currencies = {
    currency.alpha_3: currency.name
    for currency in pycountry.currencies
}
```

- **User Input**: The code asks the user to enter the initial currency code, the target currency code, and the amount to be converted. It checks if the entered currency codes are valid and if the entered amount is a positive number.

- **API Call**: The code constructs the URL for the API call using the entered initial currency, target currency, and amount. It then makes a GET request to the currency conversion API using the `requests` package.

```python
url = ("https://api.apilayer.com/fixer/convert?to="
        + target_currency + "&from=" + init_currency
        + "&amount=" + str(amount))

response = requests.request("GET", url, headers=headers, data = payload)
```

- **Response Handling**: The code checks the status of the response. If the status code is 200, it extracts the converted amount from the response and prints the result. If the status code is not 200, it prints an error message and quits.

## API Key

The API key provided in the code is a free one obtained from [apilayer](https://apilayer.com/marketplace). It's included to give you a chance to try out the code. However, please note that this free API key may not always work due to usage limits.

If you encounter any issues with the API key, you can obtain your own API key from the [apilayer marketplace](https://apilayer.com/marketplace). Once you have your API key, replace the existing API key in the code with your new one to continue using the currency converter.

## Running the Code Locally

To run this code on your local machine, follow these steps:

1. Make sure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).

2. Install the required packages by running `pip install requests pycountry` in your terminal.

3. Save the code in a file named `currency_converter.py`.

4. Open a terminal/command prompt.

5. Navigate to the directory where you saved `currency_converter.py`.

6. Run the command `python currency_converter.py`.

You should now see the prompt "Enter an initial currency code:" and you can start using the currency converter!
