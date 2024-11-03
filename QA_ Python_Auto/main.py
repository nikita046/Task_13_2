import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '251eef4ae9485c08b8fd897f2bba34e1'
HEADER = {'Content-Type' : 'application/json', "trainer_token" : TOKEN }
body_create = {
    "name": "777Бульбазавр",
    "photo_id": 1
}
response_create =requests.post(url = f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response_create.text)


pokemon_id = response_create.json()['id']
print(pokemon_id)
