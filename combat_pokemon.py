import random
from pprint import pprint
from pokeload import get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def fight_nate(player_profile, enemy_pokemon):
    pass


def fight_rcv(player_profile, enemy_pokemon):
    pass


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight_rcv(player_profile, enemy_pokemon)
    print("Has perdido en el combate n°{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
