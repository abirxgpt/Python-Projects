import datetime
import json

import requests

API_KEY = "3009fbc8588c965c46eee4e0af3dbaa0"
API_ID = "afff5ac6"
GENDER = 'male'
WEIGHT_KG = '56.00'
HEIGHT_CM = '5.8'
AGE = 21

query_to_input = input("Enter Exersice Query to Input: ")

sheety_endpoint = "https://api.sheety.co/a7da94ebf7d80e5c4455ca81222a64a8/myWorkouts/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

sheety_authentications = {
    "Authorization": "Bearer AnythingThatCanBeDone06092004"
}

params = {
    "query": query_to_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
data = response.json()


dates = datetime.datetime.now()
current_date = dates.strftime("%d/%m/%Y")
current_time = dates.strftime("%I:%M:%S %p")


for i in data["exercises"]:
    Sheet_data = {
        "workout": {
        "date": current_date,
        "time": current_time,
        "exercise": i["name"].title(),
        "duration": i["duration_min"],
        "calories": i["nf_calories"]
    }
    }

    sheets_response = requests.post(url=sheety_endpoint, json=Sheet_data, headers=sheety_authentications)
    print(sheets_response.text)
