from bs4 import BeautifulSoup
import requests

url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"

headers = {"User-Agent" : userAgent}

pagina = requests.request('GET', url=url, headers=headers)
html = pagina.text

soup = BeautifulSoup(html, "html.parser")

print(soup) 