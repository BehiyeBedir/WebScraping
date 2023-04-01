import requests
from bs4 import BeautifulSoup
import statistics


imdb_url = "https://www.imdb.com/chart/top/"
r = requests.get(imdb_url)

soup = BeautifulSoup(r.content, "html.parser")
coming_data = soup.find_all("table", {"class": "chart full-width"})

table_film = (coming_data[0].contents)[len( coming_data[0].contents) - 2]
table_film = table_film.find_all("tr")

for film in table_film:
    heads_film = film.find_all("td", {"class": "titleColumn"})
    name_film = heads_film[0].text.strip()
    name_film = name_film.replace("\n"," ")
    print(name_film)
    imdb_rating = film.find_all("td", {"class": "ratingColumn imdbRating"})
    puanlar = imdb_rating[0].text.strip()
    print(puanlar)
    print("------------------------------------------")

ratings = []
for film in table_film:
    rating = float(film.find("td", {"class": "ratingColumn imdbRating"}).get_text(strip=True))
    ratings.append(rating)

#wanted informations
mode = statistics.mode(ratings)
average = statistics.mean(ratings)
max_value = max(ratings)
min_value = min(ratings)
median = statistics.median(ratings)
standard_deviation = statistics.stdev(ratings)

print("Some numerical information about imdb Top 250")

print("max value: ",max_value)
print("min Value: ",min_value)
print("average all of films: ",average)
print("Median: ", median)
print("Standart Deviation: ",standard_deviation)
print("Mode: ",mode)

