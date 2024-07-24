import smtplib

password = "qhyhovphvhlevagh"
email = "fuxnanami@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs="top5everyt@gmail.com", msg="Subject:Testing Mail\n\nTesting Mail for Day 32")
connection.close()

or

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="top5everyt@gmail.com",
        msg="Subject:Testing Mail\n\nTesting Mail for Day 32"
    )


import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
month = now.month
print(month)
hour = now.hour
print(hour)
day_of_week = now.weekday()
print(day_of_week)
