import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
# get my header info from http://myhttpheader.com/
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
#  get headers with python requests library get method
# https://stackoverflow.com/questions/6260457/using-headers-with-the-python-requests-librarys-get-method
response = requests.get(url, headers=header)
# need to use lxml to parse not html, import lxml - html5
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
# use split method to get the price
# https://www.w3schools.com/python/ref_string_split.asp
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)