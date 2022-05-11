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


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elige con que pokemon lucharás")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cuál eliges? "))]
        except (ValueError, IndexError):
            print("Opcion invalida")


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"], pokemon["level"], pokemon["current_health"],
                                           pokemon["base_health"])


def player_attack(player_pokemon, enemy_pokemon):
    """Implementate multipliers for pokemon type base
    Normal: Debil frente a Lucha
    Fuego: debil frente a Agua, Tierra, Roca
    Agua: debil frente a planta, electrico
    Planta: debil frente a fuego, hielo, veneno, volador, bicho
    Electrico: debil frente a Tierra
    Hielo: debil frente a fuego, lucha, roca, acero
    Lucha: debil frente a volador, psiquico, hada
    Veneno: debil frente a tierra, psiquico
    Tierra: debil frente a Agua, planta, hielo
    Volador: debil frente a electrico, hielo, roca
    Psiquico: debil frente a bicho, fantasma, siniestro
    Bicho: debil frente a volador, roca, fuego
    Roca: debil frente a agua, planta, lucha, tierra, acero
    Fantasma: debil frente a fantasma, siniestro
    Dragon: debil frente a Hielo, Dragon, Hada
    Siniestro: debil frente a lucha, bicho, hada
    Acero: debil frente a fuego, lucha, tierra
    Hada: debil frente a veneno, acero

    Multipliers = * 1.25
    When the user select attacks, only show the available attacks for that level 
    """
    pass


def enemy_attack(enemy_pokemon, player_pokemon):
    pass


def assign_experience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

        while pokemon["current_exp"] > 20:
            pokemon["current_exp"] -= 20
            pokemon["level"] += 1
            pokemon["current_healt"] = pokemon["base_health"]
            print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon)))


def cure_pokemon(player_profile, player_pokemon):
    pass


def capture_with_pokeball(player_profile, enemy_pokemon):
    pass


def fight_nate(player_profile, enemy_pokemon):
    print("--- NUEVO COMBATE ---")

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    print("Contrincantes: {} VS {}".format(get_pokemon_info(player_pokemon), get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("Que deseas hacer: [A]tacar, [P]okeball, Poción de [V]ida, [C]ambiar")

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "V":
            # If the user have cures in the inventory, aplicate, health 50 life upon to 100
            # If the user doesn't have, not cure
            cure_pokemon(player_profile, player_pokemon)
        elif action == "P":
            # If the user have pokeballs in the inventory, roll one, it have a probability to capture
            # relative for the pokemon remaining health, when is capture, pass to the inventory with the same health
            # it had
            capture_with_pokeball(player_profile, enemy_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        enemy_attack(enemy_pokemon, player_pokemon)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)

    if enemy_pokemon["current_health"] == 0:
        print("Has ganado!")
        assign_experience(attack_history)

    print("--- FIN DEL COMBATE ---")
    input("Presiona ENTER para continuar")


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

    print("--- NUEVO COMBATE ---\n")
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
        print("\n--- FIN DEL COMBATE ---\n\n")
    elif actual_pokemon[0]["current_health"] <= 0:
        print("\n---Enemy Win---\n"
              "{} murio!\n".format(actual_pokemon[0]["name"]))
        print("\n--- FIN DEL COMBATE ---\n\n")


def item_lottery(player_profile):
    """ Random factor, the player could get a pokeball or a cure """
    pass


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        # fight_rcv(player_profile, enemy_pokemon)
        fight_nate(player_profile, enemy_pokemon)
        item_lottery(player_profile)
    print("Has perdido en el combate n°{}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()
