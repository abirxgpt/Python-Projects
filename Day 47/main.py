from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

URLofProduct = input("Please Enter The Url of the Product: ")


response = requests.get(URLofProduct)
amazon_webpage = response.text
load_dotenv()


pricetotrack = int(input("Please Input the price to track!: "))

soup = BeautifulSoup(amazon_webpage, "html.parser")

price = soup.select_one(selector="div span .a-price-whole")
name = soup.select_one(selector="div #titleSection")

correctedprice = ''
for i in price.text:
    if i.isnumeric():
        correctedprice += i
    elif i==".":
        correctedprice += i

if float(correctedprice) <= pricetotrack:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["email"], password=os.environ["password"])
        connection.sendmail(
            from_addr=os.environ["email"],
            to_addrs="abir.guptaaa@gmail.com",
            msg=f"Subject:Target Price Dropped to {pricetotrack} or Low\n\n{name.text}\n Order Now: {URLofProduct}"
        )