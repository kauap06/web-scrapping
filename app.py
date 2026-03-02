import requests
from bs4 import BeautifulSoup

pagina = requests.get("https://quotes.toscrape.com/")
dados_pagina = BeautifulSoup(pagina.text, "html.parser")

info = dados_pagina.find_all("div", class_="quote")

for frase in info:
    #texto = frase.find("span", class_="text").text
    
    print(texto)