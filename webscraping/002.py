from bs4 import BeautifulSoup
import requests

link = "https://www.bing.com/search?qs=AS&pq=pre%C3%A7o+do+dola&sk=CSYN1&sc=11-13&q=pre%C3%A7o+do+dolar"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"

headers = {"userAgent": userAgent}

page = requests.request('GET', url = link, headers = headers)

html = page.text

soup = BeautifulSoup(html, "html.parser")

# print(soup.title)

print(soup.find_all('input')[1])