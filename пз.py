import requests

# 1.1.2. GET-запрос к открытому API GitHub
url = "https://api.github.com/search/repositories"
params = {
    "q": "html",
}

response = requests.get(url, params=params)

# 1.1.3. статус-код ответа
print("Статус-код:", response.status_code)

# 1.1.4. содержимое ответа в формате JSON
if response.status_code == 200:
    data = response.json()  # Преобразуем ответ в JSON
    print("Содержимое ответа:")
    print(data)
else:
    print("Ошибка при запросе:", response.text)


# 1.2.1 URL API
url = "https://jsonplaceholder.typicode.com/posts"

# 1.2.2. GET-запрос с параметром userId, равным 1
params = {
    "userId": 1
}
response = requests.get(url, params=params)

# 3. полученные записи
print("Статус-код:", response.status_code)

if response.status_code == 200:
    data = response.json()  # Преобразуем ответ в JSON
    print("Полученные записи:")
    for post in data:
        print(post)
else:
    print("Ошибка при запросе:", response.text)

#1.3.1. API для отправки POST-запроса
url = 'https://jsonplaceholder.typicode.com/posts'

# 1.3.2. Словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# 1.3.3. POST-запроса
response = requests.post(url, json=data)

# 1.3.4 статус-коди содержимое ответа
print('Статус-код:', response.status_code)

print('Содержимое ответа:', response.json())


