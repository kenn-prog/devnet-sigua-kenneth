import requests 
import random

api1 = requests.get('https://pokeapi.co/api/v2/pokemon/1/')
api2 = requests.get('https://pokeapi.co/api/v2/pokemon/2/')
api3 = requests.get('https://pokeapi.co/api/v2/pokemon/3/')
api4 = requests.get('https://pokeapi.co/api/v2/pokemon/4/')
api5 = requests.get('https://pokeapi.co/api/v2/pokemon/5/')

pokemon1 = api1.json()
name1 = pokemon1['name']
height1 =pokemon1['height']
weight1 = pokemon1['weight']

pokemon2 = api2.json()
name2 = pokemon2['name']
height2 =pokemon2['height']
weight2 = pokemon2['weight']

pokemon3 = api3.json()
name3 = pokemon3['name']
height3 =pokemon3['height']
weight3 = pokemon3['weight']

pokemon4 = api4.json()
name4 = pokemon4['name']
height4 =pokemon4['height']
weight4 = pokemon4['weight']

pokemon5 = api5.json()
name5 = pokemon5['name']
height5 =pokemon5['height']
weight5 = pokemon5['weight']

pokemons = [
    {
        'name': name1,
        'height': height1,
        'weight': weight1
    },
    {
        'name': name2,
        'height': height2,
        'weight': weight2
    },
    {
        'name': name3,
        'height': height3,
        'weight': weight3
    },
    {
        'name': name4,
        'height': height4,
        'weight': weight4
    },
    {
        'name': name5,
        'height': height5,
        'weight': weight5
    }
]

def play():
    trial = 3
    guess = random.choice(pokemons)

    while trial > 0:
        print(f"\nTrial:{trial}")
        print("\nOur pokemon is:")

        for pokemon in pokemons:
            print(f"{pokemon['name']}")

        print(f"\nThis pokemon weight is {guess['weight']}, while its height is {guess['height']}.")

        choice = str(input("Who's that pokemon?").lower().strip())
    
        if choice == guess['name']:
            print(f"You are correct. The pokemon is {guess['name']}")
            return
        elif choice == "":
            print("Please input your answer.")
        else:
            print("You are incorrect. Try again")
            trial -= 1

    print("\nYour trials have run out.")
    print(f"The pokemon is {guess['name']}. You did great guessing. Better luck next time!\n")

def main():

    print("="*20)
    print("Who is that Pokemon".center(20))
    print("Welcome to the Guessing Game.".center(20))

    while True:
        print("="*20)

        print("\nChoose 1 or 2:")
        print("[1] Play\n[2]Exit")

        choice = input("\nChoose between 1-2: ")

        if choice == "1":
            play()
        elif choice == "2":
            break
        else:
            print("Choice only number 1 or 2")

main()



