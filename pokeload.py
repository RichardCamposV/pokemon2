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

    return new_pokemon


def main():

    print(get_pokemon(1))


if __name__ == "__main__":
    main()
