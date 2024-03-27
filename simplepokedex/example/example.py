from simplepokedex import pokedex

def main():
    print("Piplup's type is: ")
    print(pokedex.pokemonLookup("piplup")['data']['name'])

    print("\nThe ability Disguise does: ")
    print(pokedex.abilityLookup("disguise")['data'])

    print("\nGenerate a random pokemon from Generation V: ")
    print(pokedex.generate_pokemon(5, 3)['data']['name'])

    print("\nWhat are Fire-type Pokemon strong against? ")
    print(pokedex.poketypes("fire")['data']['double_damage_to'])

    print("\nWhat is weak against Dragon-type Pokemon? ")
    print(pokedex.poketypes("dragon")['data']['no_damage_to'])
    print(pokedex.poketypes("dragon")['data']['half_damage_to'])

if __name__ == "__main__":
    main()
