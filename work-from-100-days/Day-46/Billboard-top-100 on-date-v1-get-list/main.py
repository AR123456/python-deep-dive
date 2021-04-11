import requests
from bs4 import BeautifulSoup

# travel_date = input("What date do you want to travel to in fromat YYYY-MM-DD ?")
#
# URL = "https://www.billboard.com/charts/hot-100/"+ travel_date
URL = "https://www.billboard.com/charts/hot-100/2008-08-25"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
# ranking is in span with class = chart-element__rank__number
# song is in span with class = chart-element__information__song text--truncate color--primary
# artist is in span with class = chart-element__information__artist text--truncate color--secondary

song_titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = [song.getText() for song in song_titles]
print(song_names)
