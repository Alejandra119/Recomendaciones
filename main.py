import pandas as pd
import numpy as np
import sklearn
from typing import Union
from fastapi import FastAPI
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

app=FastAPI()

datos=pd.read_csv('datos_main.csv')

@app.get("/")
async def root():
    return {"message": "Proyecto #1 Predicciones_ Alejandra Salas "}

# 1. Peliculas_idioma: Cantidad de películas en un idioma
@app.get('/peliculas_idioma/{lenguaje}')
def peliculas_idioma(lenguaje: str):
    peliculas_por_idioma = datos.loc[datos['original_language'] == lenguaje, 'id'].drop_duplicates()
    cantidad = len(peliculas_por_idioma)
    return {'lenguaje': lenguaje, 'cantidad': cantidad}


# 2. Películas_duración: Cantidad de duración y año

# Se define una función para estandarizar el tiempo de la duración
def tiempo_duracion(x):
    hours = x // 60
    minutes = x % 60
    return f'{hours} h {minutes} m'


@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    peliculas = datos.loc[datos['title'] == pelicula, ['runtime', 'release_year']].drop_duplicates()
    duracion = [tiempo_duracion(x) for x in peliculas['runtime']]
    anio = [i for i in peliculas['release_year']]
    return {'pelicula': pelicula, 'coincidencias': len(peliculas), 'duracion': duracion, 'anio': anio}


# 3. Franquicia: Franquicia, cantidad de películas y ganancia total y ganancia promedio

@app.get('/peliculas_franquicia/{franquicia}')
def peliculas_franquicia(franquicia: str):
    peliculas = datos.loc[datos['collection_names'] == franquicia, 'revenue'].drop_duplicates()
    cantidad = len(peliculas)
    ganancia_total = int(peliculas.sum())
    ganancia_promedio = ganancia_total // cantidad
    return {'franquicia': franquicia, 'cantidad_peliculas': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}


# 4. Pais: Cantidad de películas en país.

@app.get('/peliculas_pais{pais}')
def peliculas_pais(pais:str):
    peliculas_pais = datos.loc[datos['countries'] == pais, 'id'].drop_duplicates()
    cantidad = len(peliculas_pais)
    return {'pais': pais, 'cantidad': cantidad}

# 5. Productoras_exitosas: Productora, revenue total y cantidad de películas.

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    productoras_exitosas = datos.loc[datos['companies'] == productora, 'id'].drop_duplicates()
    revenue_total = datos.loc[datos['companies'] == productora, 'revenue'].sum()
    cantidad = len(productoras_exitosas)
    return {'productora': productora, 'cantidad': cantidad, 'revenue_total': int(revenue_total)}

# 6. Director: Nombre del director, nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia de la misma en lista.

@app.get('/peliculas_director/{director}')
def peliculas_director(director: str):
    peliculas_director = datos.loc[datos['Director'] == director, 'id'].drop_duplicates()
    peliculas_data = datos.loc[datos['Director'] == director].drop_duplicates(subset='title', keep='first')
    
    peliculas = peliculas_data['title'].tolist()
    fecha_lanzamiento = peliculas_data['release_year'].tolist()
    retorno_individual = peliculas_data['return'].tolist()
    costo = peliculas_data['budget'].tolist()
    ganancia = peliculas_data['revenue'].tolist()

    return {
        'director': director,
        'peliculas': peliculas,
        'fecha_lanzamiento': fecha_lanzamiento,
        'retorno_individual': retorno_individual,
        'costo': costo,
        'ganancia': ganancia
    }

# 7. Sistema de recomendaciones
datos['title'] = datos['title'].fillna('').astype('str')
datos['genres'] = datos['genres'].fillna('').astype('str')
datos['companies'] = datos['companies'].fillna('')
datos['companies'] = datos['companies'].fillna('').astype('str')

datos['caracteristicas_comunes'] = datos['title'] + ' ' + datos['genres'] + ' ' + datos['companies']
datos['caracteristicas_comunes'] = datos['caracteristicas_comunes'].str.lower()
contar = CountVectorizer(stop_words='english', max_features=5000)
count_matrix = contar.fit_transform(datos['caracteristicas_comunes'])
modelo_k = NearestNeighbors(metric='cosine', algorithm='brute')
modelo_k.fit(count_matrix)
indices = pd.Series(datos.index, index=datos['title']).drop_duplicates()

@app.get('/recomendaciones/{titulo}')
def recomendaciones(titulo:str):
    if titulo not in datos['title'].values:
        return 'La pelicula no se encuentra en el conjunto de la base de datos.'
    else:
        index = indices[titulo]

        distances, indices_knn = modelo_k.kneighbors(count_matrix[index], n_neighbors=6)  

        movie_indices = indices_knn[0][1:]  

        return {'lista recomendada': datos['title'].iloc[movie_indices].tolist()}
