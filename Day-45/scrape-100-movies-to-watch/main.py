from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
# print(response)
empire_page = response
soup = BeautifulSoup(empire_page, "html.parser")
all_movies = soup.findAll(name="h3", class_="title")
movie_title =[movie.getText() for movie in all_movies]
# print(movie_title)
# using splice operator to reverse the order of the movies
# https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python#:~:text=Method%201%3A%20Reverse%20in%20place%20with%20obj.&text=reverse()%20function.,returns%20the%20reversed%20list%20back.
# start stop step
movies = movie_title[::-1]
# print(movies)
# using reverse()
# movies = movie_title.reverse()
# print(movies)

# create text file - error because of encodeing on empire site
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")

with open("movies.txt", "w", encoding="UTF-8") as f:
    for movie in movies:
        f.write(movie + "\n")