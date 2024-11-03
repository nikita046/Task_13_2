import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '251eef4ae9485c08b8fd897f2bba34e1'
HEADER = {'Content-Type' : 'application/json', "trainer_token" : TOKEN }
TRAINER_ID = '7029'
BODY_NEW_NAME =  {
    "pokemon_id": "122012",
    "name": "New Name",
    "photo_id": 2
}
BODY_CATCH_A_POKEBOLL = {
    "pokemon_id": "122012"
}



'''def test_status_code():
    response = requests.get(
        url= f'{URL}/pokemons',
        params= {'trainer_id' : TRAINER_ID},
        haders= HEADER
    )
    assert response.status_code == 200'''


'''def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200'''

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == '777Бульбазавр'
# Проверка имени, id, тренер id 
@pytest.mark.parametrize('key, value', [('name', '777Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '122012')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value    
# Смена имени 
def test_changing_the_Pokemon_name():
    response_changing_the_Pokemon_name = requests.put(url=f'{URL}/pokemons', headers= HEADER, json= BODY_NEW_NAME, params = {'trainer_id' : TRAINER_ID})
    assert response_changing_the_Pokemon_name.json()
# отправка в покебол 
def test_catch_a_pokeball():
    response_catch_a_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers= HEADER, json= BODY_CATCH_A_POKEBOLL, params = {'trainer_id' : TRAINER_ID})
    assert response_catch_a_pokeball.json()