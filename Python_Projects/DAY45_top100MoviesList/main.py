#### List of Top 100 movies via Web Scraping#####
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web = response.text
soup = BeautifulSoup(yc_web, "html.parser")
# print(soup.title.string)

# Single movie
# movie = soup.find(name='h3', class_="title")
# print(movie)
# print(movie.getText())

# All movies
all100movies = []
movies = soup.find_all(name='h3', class_="title")
all100movies = [movie.getText() for movie in movies]
# print(int(soup.find(name='span', class_="score").getText().split(' ')[0]))
# print(all100movies)
all100movies.reverse()
# all100movies[::-1]

with open("data/movies.txt", mode='a') as fl:
    for movi in all100movies:
        print(f"{movi}\n")
        fl.write(f"{movi}\n")


