
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# Шаг 1. Создание покемона
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

respons_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(respons_create.text)

# Проверяем успешность создания и извлекаем id покемона
if respons_create.status_code == 201:
    response_json = respons_create.json()
    pokemon_id = response_json['id']  # Сохраняем id созданного покемона
else:
    print("Ошибка при создании покемона:", respons_create.text)
    exit()

# Шаг 2. Изменение имени покемона
body_change = {
    "pokemon_id": pokemon_id,
    "name": "Flait",  # Новое имя
    "photo_id": 12
}

respons_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)

print(respons_change.text)

# Шаг 3. Добавление покемона в покеболл
body_add_pokeboll = {
    "pokemon_id": pokemon_id
}

respons_add_pokeboll = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeboll)

print(respons_add_pokeboll.text)
