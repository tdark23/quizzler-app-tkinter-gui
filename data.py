import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
# response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
response.raise_for_status()
datas = response.json()['results']

question_data = datas