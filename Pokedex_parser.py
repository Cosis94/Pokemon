from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.pokewiki.de/index.php?title=Pokémon-Liste&action=edit")

doc = BeautifulSoup(r.text, "html.parser")#

doc_view = doc.find_all("textarea")

for elements in doc_view:
    with open('Pokedex.txt', 'w', encoding="utf-8") as f:
        f.write(elements.text)
