from bs4 import BeautifulSoup
#if the html.parser is not working may need to use lxml
# import lxml
with open("website.html",encoding="utf-8") as file:
    contents = file.read()
#soup object
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
#print(soup.prettify())
# print(soup.a)
#findAll returns a list of the elements found
all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
# getting text of all the anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText())
# getting the href
# for tag in all_anchor_tags:
#     print(tag.get("href"))
## find the first h1 tag with an id of name
# heading = soup.find(name="h1", id="name")
# print(heading)
## find hte first h3 with a classname of heading
section_heading = soup.find(name="h3", class_ ="heading")
print(section_heading.getText())