import requests
from bs4 import BeautifulSoup

pagina = requests.get("https://quotes.toscrape.com/")
dados_pagina = BeautifulSoup(pagina.text, "html.parser")

def filter(classe_css):
    return classe_css is not None and len(classe_css) < 8

info = dados_pagina.find_all("div", class_=filter)

for frase in info:
    print(frase['class'])