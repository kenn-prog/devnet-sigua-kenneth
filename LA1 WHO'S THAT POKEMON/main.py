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




