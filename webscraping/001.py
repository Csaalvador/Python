from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/" 
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"

headers = {"user-Agent": userAgent}

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.a.text)

page = requests.request('GET', url = url, headers = headers)

# print(f"Status da requisição: {page.status_code}")
html = page.text

soup = BeautifulSoup(html, 'html.parser')

for i in soup.find_all('h3'):
    print(i.text)

    # print (soup.find_all('p', attrs={'class' : 'star-rating'})[i].get('class')[1])
