from bs4 import BeautifulSoup
import requests

link = "https://books.toscrape.com/"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"

headers = {"User-Agent" : userAgent}

pagina = requests.request('GET', url=link, headers=headers)
html = pagina.text

soup = BeautifulSoup(html, "html.parser")

livros = soup.find_all("article", class_="product_pod")

for livro in livros :
    textos = (livro.text)
    titulo = soup.find_all('a')

    valor = soup.find('p', class_='price_color').text

    print(f"{textos}{valor}")




    