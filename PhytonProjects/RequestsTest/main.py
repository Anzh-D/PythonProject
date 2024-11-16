import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fa68d101940cb1ab3e0276edba412dde'
HEADER = {'Content-Type':'application/json','trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN ,
    "email": "anzh-122@yandex.ru",
    "password": "Iloveqa1"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER ,json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

# Мои запросы ниже :)

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers=HEADER, json={"name": "generate","photo_id": 75})
print(response_create_pokemon.json())

response_change_pokemon_name = requests.put(url = f'{URL}/pokemons', headers=HEADER, json={"pokemon_id": "135433", "name": "Alex", "photo_id": 2})
print(response_change_pokemon_name.json())

response_pokemon_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json={"pokemon_id": "135433"})
print(response_pokemon_catch.json())