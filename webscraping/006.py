import requests
import os   
from bs4 import BeautifulSoup

# URL base do site
url = "https://books.toscrape.com/"
nomePasta = "imagensLivros"

# Criar a pasta se não existir
os.makedirs(nomePasta, exist_ok=True)

# Criar sessão e baixar a página
sessao = requests.Session()
resposta = sessao.get(url, timeout=10)

# Verificar se a página foi acessada com sucesso
if resposta.status_code != 200:
    raise Exception(f"Erro ao acessar site. Código: {resposta.status_code}")

# Processar o HTML
pagina = BeautifulSoup(resposta.text, 'html.parser')

# Lista para armazenar os links das imagens
bancoImagens = []

# Buscar todas as tags <img>
for imagem in pagina.find_all('img', src=True):
    src = imagem['src']

    # Corrigir URL da imagem
    imagemUrl = url + src.replace("../", "")
    bancoImagens.append(imagemUrl)

# Se não encontrou imagens, dispara erro
if not bancoImagens:
    raise Exception("Nenhuma imagem encontrada.")

# Baixar imagens
for imgUrl in bancoImagens:
    nomeArquivo = os.path.join(nomePasta, imgUrl.split("/")[-1])

    with open(nomeArquivo, "wb") as arquivo:
        imgResposta = sessao.get(imgUrl, stream=True)
        for chunk in imgResposta.iter_content(8192):
            arquivo.write(chunk)

    print(f"Imagem salva: {nomeArquivo}")

print("\n✅ Download de imagens finalizado!")
