import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa68d101940cb1ab3e0276edba412dde'
HEADER = {'Content-Type':'application/json','trainer_token' : TOKEN}
TRAINER_ID = '7683'
DATA = {"name": "generate","photo_id": 75}

def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id' :TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response(): 
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '134307')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value

# Мои тесты ниже :)

def test_trainers_get_status_code(): 
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' :TRAINER_ID})
    assert response.status_code == 200

def test_trainers_get(): 
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' :TRAINER_ID})
    assert response.json()["data"][0]['id'] == TRAINER_ID