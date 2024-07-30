from requests import *
from twilio.rest import Client


API_KEY = "032fd7682b4c79b9edea4c0ebc5f7e1a"
LAT = 26.458990
LONG = 74.636421
account_sid = #Use your Own Account SID from Twilio
auth_token = #Use your Own Auth Token from Twilio

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4
}

client = Client(account_sid, auth_token)

call = get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
call.raise_for_status()
result = call.json()
Weather_id = []
is_rain = False
for i in result["list"]:
    Hourly_Weather = i["weather"][0]["id"]
    if Hourly_Weather < 700:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="It's Going to Rain Today!, Bring an Umbrella with you!☔🌦️",
            to=#Your Number Where to Send
        )

        print(message.sid)
