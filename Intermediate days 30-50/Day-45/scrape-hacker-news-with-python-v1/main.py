from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/").text
# print(response.text)

# get article title and link with the highest points
soup = BeautifulSoup(response, "html.parser")
# print(soup.prettify())
# a tag with class storylink get href and the text of the a tag
# span class of score text shows the point total  (strip off word points)
all_anchor_tags = soup.findAll(name="a", class_="storylink")
all_scores = soup.findAll(name="span", class_="score")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))



print(all_scores.getText())