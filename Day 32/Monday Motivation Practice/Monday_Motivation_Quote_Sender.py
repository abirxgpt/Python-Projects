import smtplib
import datetime as dt
import random

# Mail Credentials
password = #Add Your Password Here
email = #Add Your Email Here

# To Extract Quotes to List
with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()

# Current Date
today = dt.datetime.now()
current_week_day = today.weekday()

# Code Implementation
if current_week_day == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=# Anyone you want to send your Mail to.
            ,msg=f"Subject:Motivational Quote\n\n{random.choice(quotes_list)}"
        )
