from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

heading_movies = []
h2_head = soup.select(selector="h2 strong")
for i in h2_head:
    text = i.getText()
    heading_movies.append(text)
heading_movies.reverse()

with open("movies100.txt",mode="a") as file:
    for i in heading_movies:
        file.write(i)
        file.write("\n")