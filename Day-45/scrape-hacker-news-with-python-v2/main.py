from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/").text
# print(response.text)
hn_web_page = response
# get article title and link with the highest points
soup = BeautifulSoup(hn_web_page, "html.parser")
articles = soup.find_all(name="a", class_ ="storylink")
# 2 new lists to hold the article text and links
article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    # append list  of text
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    #append ist of article lomls
    article_links.append(article_link)
# use list comprehension to make article upvote into a list
article_upvote = [score.getText() for score in soup.find_all(name="span", class_ ="score")]
# get the article upvotes as an intiger - split string on space
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ ="score")]
# need to get the index of the item with the highest value, since all the lists are ordered in the same way can then
# the coresponing index of the other arrays
high_vote_article_index = article_upvote.index(max(article_upvote))
print(high_vote_article_index)

print((article_texts)[high_vote_article_index])
print((article_links)[high_vote_article_index])
print((article_upvote)[high_vote_article_index])



# print(article_texts)
# print(article_links)
# print(article_upvote)
# print(article_upvote[0])
# print(article_upvote[0].split())
#get first item en the split which is the number
# print(article_upvote[0].split()[0])
# print(int(article_upvote[0].split()[0]))


# print(soup.prettify())
# # a tag with class storylink get href and the text of the a tag
# # span class of score text shows the point total  (strip off word points)
# all_anchor_tags = soup.findAll(name="a", class_="storylink")
# all_scores = soup.findAll(name="span", class_="score")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
#
#
# print(all_scores.getText())