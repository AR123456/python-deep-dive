from bs4 import BeautifulSoup
#if the html.parser is not working may need to use lxml
# import lxml
with open("website.html",encoding="utf-8") as file:
    contents = file.read()
#soup object
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
print(soup.prettify())
print(soup.a)