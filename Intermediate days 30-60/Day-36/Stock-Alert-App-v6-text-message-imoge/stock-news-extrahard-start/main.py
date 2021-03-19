import requests
from datetime import date
from datetime import timedelta

import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# TODO Find Stock to message
# Pfizer Inc.
# STOCK = "PFE"
# COMPANY_NAME = "Pfizer Inc"

# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
STOCK = "MRNA"
COMPANY_NAME = "Moderna Inc"

# stock end point
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
# alpha Vantage
STOCK_API_KEY = ""
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
# https://stackoverflow.com/questions/30483977/python-get-yesterdays-date-as-a-string-in-yyyy-mm-dd-format/30484112
# date.timedelta to get yesterday
today = date.today()
# Yesterday date
yesterday = today - timedelta(days=1)
# print("Yesterday was: ", yesterday)
# yesterday.strftime("%Y-%m-%d")

YESTERDAY = yesterday.strftime("%Y-%m-%d")
print(YESTERDAY)

# newsapi end point
NEWSAPI_ENDPOINT = "https://newsapi.org/V2/everything?"
NEWS_API_KEY = ""

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
# yesterdays closing stock price
time_series_daily = stock_data["Time Series (Daily)"]
# use list comprehension to turn the Time series daily dictionary into a list
time_series_daily_list = [value for (key, value) in time_series_daily.items()][0]
yesterdays_close = [value for key, value in time_series_daily_list.items()][3]
# print(yesterdays_close)
# day before yesterday close
daybefore_yesterday_dic = [value for (key, value) in time_series_daily.items()][1]
daybefore_yesterday_close = [value for (key, value) in daybefore_yesterday_dic.items()][3]
# print(daybefore_yesterday_close)
diff_for_updown = float(yesterdays_close) - float(daybefore_yesterday_close)
up_down = None
if diff_for_updown > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
price_diff = abs(float(yesterdays_close) - float(daybefore_yesterday_close))
percent_diff = round((price_diff) / float(yesterdays_close) * 100)
print(percent_diff)
if percent_diff > 1:
    print("get news")
    news_params = {
        "q": COMPANY_NAME,
        "from": YESTERDAY,
        "to": YESTERDAY,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWSAPI_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    # articles key is a list
    articles = news_response.json()["articles"]
    # each article is a dictionary in the articles list
    # use slice operator to get first 3
    # print(articles)
    #  a[start:stop:step] # start through not past stop, by step
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK}:{up_down}{percent_diff}%\n Headline: {article['title']}. \n Brief:{article['url']}"
                          for article in three_articles]

    # Twilio end point
    Twilio_Endpoint = "https://www.twilio.com"
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_="+1",
            to="+"
        )
        print(message.sid)

else:
    print("no need for news")
