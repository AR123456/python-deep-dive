import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# TODO Find Stock to message
# Pfizer Inc.
STOCK = "PFE"
CPANY_NAME = "Pfizer Inc"

# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
# STOCK = "MRNA"
# COMPANY_NAME = "Moderna Inc"

# stock end point
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
# alpha Vantage
STOCK_API_KEY = ""
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)

stock_response.raise_for_status()
stock_data = stock_response.json()

# yesterdays closing stock price
time_series_daily=stock_data["Time Series (Daily)"]
# use list comprehension to turn the Time series daily dictionary into a list
time_series_daily_list = [value for (key,value) in time_series_daily.items()][0]
yesterdays_close = [value for key,value in time_series_daily_list.items()][3]
# print(yesterdays_close)
# day before yesterday close
daybefore_yesterday_dic = [value for (key,value) in time_series_daily.items()][1]
daybefore_yesterday_close = [value for (key,value) in daybefore_yesterday_dic.items()][3]
# print(daybefore_yesterday_close)
price_diff = abs(float(yesterdays_close)-float(daybefore_yesterday_close))
percent_diff =   ((price_diff)/float(yesterdays_close)*100)
print(percent_diff)
if percent_diff >0.1:
    print("get news")
else:
    print("no need for news")

# newsapi end point
Newsapi_Endpoint = "https://newsapi.org"

# Twilio end point
Twilio_Endpoint = "https://www.twilio.com"
# TODO

# newsapi
account_sid = "#"
auth_token = "#"

# stock end point
STOCK_ENDPOINT = "https://www.alphavantage.co"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
