# Python Web Scraper

This project is a simple web scraper that fetches data from a book store website. Web scraping is a technique for extracting information from websites. It focuses on the transformation of unstructured data on the web, typically in HTML format, into structured data that can be stored and analyzed.

## Packages Used

- `requests`: This package allows you to send HTTP requests using Python and receive responses. In this project, it's used to fetch the webpage content.
- `beautifulsoup4`: This library is used for parsing HTML and XML documents. It creates parse trees that are helpful to extract the data easily.

## Code Explanation

1. We first import the necessary packages:

   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

2. We define the URL of the webpage we want to scrape:

   ```python
   url = 'https://books.toscrape.com/'
   ```

3. We use `requests.get(url)` to send a GET request to the website and fetch the webpage content:

   ```python
   response = requests.get(url)
   ```

4. We create a BeautifulSoup object and specify the parser library at the same time:

   ```python
   soup = BeautifulSoup(response.text, 'html.parser')
   ```

5. We then find all `article` elements, extract the book title, rating, and price, and print them:

   ```python
   for article in soup.find_all('article'):
       title = article.h3.a.attrs['title']
       rating = article.p.attrs['class'][1]
       price = article.select('.price_color')[0].get_text()
       print(f'\nTitle: {title} | Rating: {rating} | Price: {price}')
   ```

## Customizing the Web Scraper

This web scraper is designed to scrape data from 'https://books.toscrape.com/', but you can customize it to scrape data from any website. To do this, you would replace the URL in the `url` variable with the URL of the website you want to scrape.

However, keep in mind that the structure of webpages can vary greatly. The tags and attributes used in this script are specific to the structure of 'https://books.toscrape.com/'. If you want to scrape a different website, you'll likely need to update these to match the structure of that website.

Here's what each line in the script does:

- `title = article.h3.a.attrs['title']`: This line gets the title of the book. It finds the first `<a>` tag nested inside an `<h3>` tag within the `<article>` tag, and then gets the value of the `title` attribute.

- `rating = article.p.attrs['class'][1]`: This line gets the rating of the book. It finds the first `<p>` tag within the `<article>` tag, and then gets the second value of the `class` attribute (which corresponds to the rating).

- `price = article.select('.price_color')[0].get_text()`: This line gets the price of the book. It uses the `select` method to find the first element with the `price_color` class within the `<article>` tag, and then gets its text.

To find the correct tags and attributes for a different website, you can use the 'Inspect' feature in your web browser. This allows you to see the HTML of the webpage and find the tags that contain the data you want to scrape. For example, if you wanted to scrape a different piece of data, like the book's description, you would find the tag that contains the description and use its tag name and attributes in your script.

## Running the Code Locally

1. Make sure you have Python installed on your machine.

2. Install the necessary Python packages using pip:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the Python script:

   ```bash
   python web_scraper.py
   ```

This will print the title, rating, and price of each book on the webpage.
