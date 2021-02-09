import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# TODO Find Stock to message
# Pfizer Inc.
# NYSE:PFE
# Moderna Inc
# NASDAQ MRNA
# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
STOCK = "MRNA"
COMPANY_NAME = "Moderna Inc"

# stock end point
Alpha_Endpoint = "https://www.alphavantage.co/query?"
# alpha Vantage
Alpha_api_key = "#"
parameters = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": Alpha_api_key,
}
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo
stock_response = requests.get(Alpha_Endpoint, params=parameters)

stock_response.raise_for_status()
stock_data = stock_response.json()
print(stock_data)

# newsapi end point
Newsapi_Endpoint = "https://newsapi.org"

# Twilio end point
Twilio_Endpoint = "https://www.twilio.com"
# TODO

# newsapi
account_sid = "#"
auth_token = "#"

# stock end point
Alpha_Endpoint = "https://www.alphavantage.co"

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
