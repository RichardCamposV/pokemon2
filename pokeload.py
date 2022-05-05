URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_pokemon&pk="


def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)


def main():

    pokemon_base = {
        "name": "",
        "current_health": 100,
        "base_health": 100,
        "level": 1,
        "current_exp": 0
    }


if __name__ == "__main__":
    main()
