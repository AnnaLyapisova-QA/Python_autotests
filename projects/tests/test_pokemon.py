
import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ad9cd1291ad684d21d1dec2302de7905'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = "46697"

def test_status_code ():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_respons ():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    print(response_get.text)
    assert response_get.json()['data'][0]['trainer_name']=='Nezuko'