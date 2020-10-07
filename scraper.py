import requests
# Essentially allows us to access a URl/ URL's.
from bs4 import BeautifulSoup
# BeautifulSoup allows us to parse that website data.

url = 'https://www.amazon.co.uk/Canon-1-2L-USM-Lens-Black/dp/B000I2J2S6/ref=sr_1_5?crid=2MWU8TLJB6W7V&dchild=1&keywords=canon+1.4+50mm&qid=1601990115&sprefix=canon+1.4%2Caps%2C147&sr=8-5'

# Giving some information about our browser.
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

# This is collecting all that data from the website.
page = requests.get(url, headers=headers)

# Here we create another variable called soup and pass in two arguments.
# Additional note. I substitued out html.parser for html5lib as either this or lxml has the capability to fix
# botched html elements which in this case were not letting me parse the title.
soup = BeautifulSoup(page.content, 'html5lib')


# Created a variable called title and using BeautifulSoup, returns the product title as it is called.
# For price we are converting from text to numbers, then targeting specifically the first 6 numbers.
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[0:6]

print(converted_price)
print(title.strip())
