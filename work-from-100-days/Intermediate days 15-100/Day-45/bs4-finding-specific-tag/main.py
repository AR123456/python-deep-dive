from bs4 import BeautifulSoup
#if the html.parser is not working may need to use lxml
# import lxml
with open("website.html",encoding="utf-8") as file:
    contents = file.read()
#soup object
soup = BeautifulSoup(contents, "html.parser")

# use css selector to narrow down
company_url = soup.select_one(selector="p a")
print(company_url)
# selecting an ID
name = soup.select_one(selector="#name")
print(name)
# selecting by class
headings= soup.select(".heading")
print(headings)