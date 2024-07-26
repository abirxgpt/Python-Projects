import requests
import smtplib
from datetime import datetime

LAT_BWM = 24.401800
LONG_BWM = 75.809303
password = #use your password here
email = #use your email here
receive_address = #use your Receiver Address here
LOCATION = "Asia/Kolkata"

iss_data = requests.get("http://api.open-notify.org/iss-now.json")
iss_data.raise_for_status()

data = iss_data.json()

latitude_iss = float(data["iss_position"]["latitude"])
longitude_iss = float(data["iss_position"]["longitude"])


parameter = {
    "lat": LAT_BWM,
    "lng": LONG_BWM,
    "formatted": 0,
    "tzid": LOCATION
}

day = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
day.raise_for_status()

day_data = day.json()

sunrise = int(day_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(day_data["results"]["sunset"].split("T")[1].split(":")[0])

print(latitude_iss)
print(LAT_BWM)
print(longitude_iss)
print(LONG_BWM)

print(sunrise)
print(sunset)

today = datetime.now()
right_now = today.hour
print(right_now)

if (LAT_BWM-5) <= latitude_iss <= (LAT_BWM+5) and (LONG_BWM-5) <= longitude_iss <= (LONG_BWM+5):
    if sunset <= right_now <= 24 or 00<= right_now <= sunrise:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=receive_address,
                msg=f"Subject:ISS TIMER\n\nHey!!, It's Time to Watch the International Space Station Over the Head"
            )



