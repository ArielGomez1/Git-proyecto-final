# Importamos las librerias que vamos a utilizar.
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Variables
num = 51
url = 'https://www.imdb.com/search/title/?groups=top_1000'
url1 = f'https://www.imdb.com/search/title/?groups=top_1000&start={num}&ref_=adv_nxt'
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

# Inicializar el almacenamiento de datos
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []
# Anidamos el scrap
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

def metodo(div,titulo,anio,tiempo,rating,metascores):
# Bucle FOR para recorrer todo el sitio.
    for container in movie_div:
    # Nombre
        name = container.h3.a.text
        titles.append(name)
    # Año
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)
    # Duracion de la pelicula
        runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
        time.append(runtime)
    # IMDB Rating
        rating = float(container.strong.text)
        imdb_ratings.append(rating)
    # Metascore
        meta = container.find('span', class_='metascore').text
        metascores.append(meta)


metodo(movie_div,titles,years,time,imdb_ratings,metascores)

for i in range(2):
    url1 = f'https://www.imdb.com/search/title/?groups=top_1000&start={num}&ref_=adv_nxt'
    resultado = requests.get(url1, headers=headers)
    soup1 = BeautifulSoup(resultado.text, "html.parser")
    movie_div = soup1.find_all('div', class_='lister-item mode-advanced')
    metodo(movie_div,titles,years,time,imdb_ratings,metascores)
    num = num +50

#print(titles)
#print(years)
#print(time)
#print(imdb_ratings)
print(metascores)

#diccionario = {'Titulo':titles, 'Año':years, 'Duracion':time, 'Raiting':imdb_ratings, 'Metascores':metascores, 'Votos':votes, 'recaudado':us_gross}
#Tabla = pd.DataFrame(diccionario)
#print(Tabla)