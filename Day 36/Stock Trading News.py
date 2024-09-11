import requests
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "4ZELHM3OK8UXX3A6"
NEWS_API_KEY = "0b9db00e82f14dec879c1903df90e3bc"
TWILIO_API_KEY = "Your Twilio Api Key"
TWILIO_AUTH_TOKEN = "Your Twilio Auth Token"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_PARAMS = {
    "sortBy": "popularity",
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

stock_news = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
time_stock_data = stock_news.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in time_stock_data.items()]
yesterday_data = stock_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
positive_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

difference_percentage = (positive_difference / float(yesterday_closing_price)) * 100
if difference_percentage > 0:
    news = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = news.json()["articles"]
    top_articles = articles[:3]

    articles_message = [f"Headline: {articles['title']}. \nBrief: {articles['description']}." for articles in
                        top_articles]
    High_Low = ''
    if difference > 0:
        High_Low = f'{STOCK}: 🔺📈{difference_percentage}%'
    else:
        High_Low = f'{STOCK}: 🔻📉{difference_percentage}%'
    for articles in articles_message:
        client = Client(TWILIO_API_KEY, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=f"{High_Low}\n{articles}",
            to='whatsapp:+918824537921',
            from_='whatsapp:+14155238886'
        )


