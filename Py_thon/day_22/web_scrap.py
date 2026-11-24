"""
- The internet is full of data which us useful for different purposes.
- To collect this data you need to scrape data from websites.
- Webscraping is extracting data from websites.
- To start scraping websites you need requests, beautifoulSoup4 and a website.
    source .venv/bin/activate
    pip install packagename
    pip list
    pip freeze > requirements.txt
- To scrape data from websites basic understanding of HTML tags and CSS selectors are necessary.
- We target content from a website using HTML tags, classes or/and ids.
"""

import requests
from bs4 import BeautifulSoup

# Declaring the url variable of the website we are scraping
url = "https://www.youtube.com/"

# Using request method to get data from the url

response = requests.get(url)

# Checking the status
status = response.status_code
# print(status)

# To get all the content from a website 
content1 = response.content
soup = BeautifulSoup(content1, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)