from selenium import webdriver
from pages.quotes_page import QuotePage
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

author = input("Enter the author you'd like quotes from: ")
tag = input("Enter a tag: ")

chrome = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=chrome_options)

chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotePage(chrome)

print(page.search_quotes(author, tag))
