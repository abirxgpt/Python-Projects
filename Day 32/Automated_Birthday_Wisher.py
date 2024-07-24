import smtplib
import datetime as dt
import random as r
import pandas

# Constants
password = # Add your Mail Password here
email = # Add your Email ID here

# Defining Send Function
def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=people['email'],
            msg=f"Subject:Happy Birthday!!\n\n{Completed_letter}"
        )


birthday_list = pandas.read_csv("./Birthday_Data/birthdays.csv")
birthday_dict = birthday_list.to_dict('records')

# Current Date
today = dt.datetime.now()

# Checking if Birthday is Today
for people in birthday_dict:
    if today.month == people["month"]:
        if today.day == people["day"]:

            # After Checking Opening one random Letter
            with open(f"./letter_templates/letter_{r.randint(1,10)}.txt") as letter:
                Letter = letter.read()
                Completed_letter = Letter.replace("[NAME]", people['name'])

            # Sending the mail on the Lucky person's Email Address
            send_mail()






