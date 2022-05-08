import pickle
from requests_html import HTMLSession
from selenium import webdriver
import re

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_pokemon&pk="
pokemon_base = {
        "name": "",
        "current_health": 100,
        "base_health": 100,
        "level": 1,
        "type": None,
        "current_exp": 0
    }
TOTAL_POKEMONS = 151


def check_status_web(url):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)


def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)
    # Find pokemon name with Regex
    pokemon_scraping = pokemon_page.html.find(".mini", first=True).text
    pokemon_name = re.findall("(^[A-Za-z]+)", pokemon_scraping)
    new_pokemon["name"] = pokemon_name[0]
    # Find type pokemon
    new_pokemon["type"] = []

    for img in pokemon_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    new_pokemon["attacks"] = []
    # Find pokemon attacks
    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a")[1].text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min_level": attack_item.find("td")[2].text,
            "damage": int(attack_item.find("td")[2].text)
        }
        new_pokemon["attacks"].append(attack)

    return new_pokemon


def get_all_pokemons():
    try:
        print("Cargando el archivo de pokemons...")
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)
    except FileNotFoundError:
        print("Archivo no encontrado! Cargando de internet...")
        all_pokemons = []
        for index in range(TOTAL_POKEMONS):
            all_pokemons.append(get_pokemon(index + 1))
            print("*", end="")
        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
        print("\n¡Todos los pokemons han sido descargados!")
    print("¡Lista de pokemons cargada!")
    return all_pokemons


def main():

    print(get_all_pokemons())


if __name__ == "__main__":
    main()
