import requests

parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}
question = requests.get("https://opentdb.com/api.php", params=parameters)
data = question.json()
question_data = data['results']
