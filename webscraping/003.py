from bs4 import BeautifulSoup
import requests

link = "https://news.ycombinator.com/"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"

headers = {"user-Agent": userAgent}

pagina = requests.request('GET', url=link, headers=headers)
html = pagina.text

soup = BeautifulSoup(html, "html.parser")

titulos = soup.find_all('a')

for titulo in titulos :
    print(titulo.text)