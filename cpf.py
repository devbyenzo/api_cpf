import requests

cpf = input("Digite o CPF: ")
url = f'https://api.cpfhub.io/cpf/{cpf}'
headers = {
                'x-api-key': 'API-KEY',
                'Accept': 'application/json'
            }
response = requests.get(url, headers=headers)
data = response.json()
print(data)