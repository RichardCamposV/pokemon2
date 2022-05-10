import random
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

    def show_current_healt():
        print("\nEnemy\n"
              "{} health: {}\n"
              "Player\n"
              "{} health: {}".format(enemy_pokemon["name"], enemy_pokemon["current_health"],
                                     actual_pokemon[0]["name"], actual_pokemon[0]["current_health"]))

    def show_attack_and_damage(identify_user, attack_name, attack_damage):
        print("\n{} ataca con: {}\n"
              "Daño: {}".format(identify_user, attack_name, attack_damage))

    pokemons_user = []
    actual_pokemon = []
    attacks_pokemon_user = []

    print("Te has encontrado con {}, y quiere pelear!!!\n".format(enemy_pokemon["name"]))
    print("Selecciona un pokemon para pelear: ")
    for pokemon in player_profile["pokemon_inventory"]:
        print(pokemon["name"])
        pokemons_user.append(pokemon["name"])
    select_pokemon_user = input("Pokemon: ")
    while select_pokemon_user not in pokemons_user:
        select_pokemon_user = input("Pokemon: ")

    print("\n---{} vs {}---\n\n".format(enemy_pokemon["name"], select_pokemon_user))
    for pokemon in player_profile["pokemon_inventory"]:
        if select_pokemon_user == pokemon["name"]:
            actual_pokemon.append(pokemon)
    for attack in actual_pokemon[0]["attacks"]:
        attacks_pokemon_user.append([attack["name"], attack["damage"]])

    while enemy_pokemon["current_health"] > 0 and actual_pokemon[0]["current_health"] > 0:
        # Show current health both players
        show_current_healt()
        # Random enemy attack
        random_attack_enemy = random.choice(enemy_pokemon["attacks"])
        show_attack_and_damage(enemy_pokemon["name"], random_attack_enemy["name"], random_attack_enemy["damage"])
        actual_pokemon[0]["current_health"] -= random_attack_enemy["damage"]

        show_current_healt()

        if actual_pokemon[0]["current_health"] > 0:
            # Select player attack
            print("\nEs tu turno...\n"
                  "Selecciona un ataque:\n")
            for attack in attacks_pokemon_user:
                print("Ataque: {} | Daño: {}".format(attack[0], attack[1]))
            attack_player = input("Attack player: ")
            confirm_attack = True
            while confirm_attack:
                for attack in attacks_pokemon_user:
                    if attack_player in attack:
                        show_attack_and_damage(actual_pokemon[0]["name"], attack[0], attack[1])
                        enemy_pokemon["current_health"] -= attack[1]
                        show_current_healt()
                        confirm_attack = False
                if confirm_attack:
                    attack_player = input("Attack player: ")

    if enemy_pokemon["current_health"] <= 0:
        print("\n---Player Win---\n"
              "{} murio!\n".format(enemy_pokemon["name"]))
    elif actual_pokemon[0]["current_health"] <= 0:
        print("\n---Enemy Win---\n"
              "{} murio!\n".format(actual_pokemon[0]["name"]))


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight_rcv(player_profile, enemy_pokemon)
    print("Has perdido en el combate n°{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
