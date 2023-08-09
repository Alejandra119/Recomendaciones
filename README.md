<h1 align="center"> Proyecto_ Modelo de Recomendaciones </h1>

### Desarrollado por: Alejandra Salas
Objetivo: Utilizar los datasets de películas y directores para brindar 5 recomendaciones por cada película mediante una API.

## Índice

* [Descripción del proyecto](#descripción-del-proyecto)

* [Procesos realizados](#procesos-realizados)

* [Conclusión](#conclusión)

## Descripción del proyecto
Supongamos que iniciaste a trabajar como Data Scientist para una start-up proveedora de servicios de agregación de plataformas de streaming. Podrás crear tu primer modelo de Machine Learning para mejorar el sistema de recomendación actual del negocio.

Los datos proporcionados no cuentan con la madurez suficiente para trabajarlos 😭(Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas).

Deberás realizar un ETL - desarrollo de una API - despliegue de una API en el caso de *Data Engineer*, un EDA en el caso de *Data Anaslyst* y un Modelo de recomendación en el caso de *Data Science* para lograr obtener un MVP (Minimum Viable Product) para el cierre del proyecto!🤯.
A espantar los miedos y manos a la obra 💪.

## Procesos realizados
:construction: Organización del proyecto :construction:

Aplicaremos las habilidades blandas utilizando las herramientas organizacionales necesarias, en este caso será *Notion*.
![Notion](https://github.com/Alejandra119/Recomendaciones/assets/72637210/01da5206-0311-4a0a-9862-30c1455033c9)

## :hammer:Data Engineer
**`ETL (Extract, Transform and Load)`**
Se encuentra en el archivo **[Desarrollo del ETL](Desarrollo%20del%20ETL.ipynb)**
1. Contamos con los datasets "movies" que contiene una serie de variables con diversas películas, así mismo, tenemos el dataset "credits" que contiene la ista del personal que participó por cada película.

2. Necesitamos realizar las siguientes tareas:

* Algunos campos de los datasets están anidados, se deberán desanidarlos o buscar la manera de acceder a esos datos sin desanidarlos.

* Rellenar con 0 los campos revenue y budget.

* Eliminar los valores nulos del campo release date.

* Las fechas deberán tener el formato AAAA-mm-dd y crear la columna release_year donde se extraerá el año de la fecha de estreno.

* Crear return dividiendo revenue / budget, si no hay datos disponibles, estos deberá ser 0.

* Eliminar las columnas que no serán utilizadas.

**`Desarrollo y Deployment de la API`**

3. Desarrollo de la API.
Se utilizó FAST API para como servidor local para poder visualizar las funciones, esto se encuentra en el archivo **[main.py](main.py)**

4. Despliegue de la API.
Se utilizó RENDER para realizar el deploy de nuestra API local, cpnsiguiendo el siguiente link funcional **[deploy](https://deploy-recomendaciones.onrender.com/docs)**

## :mag:Data Analyst
Se encuentra en el archivo **[Desarrollo del EDA](Desarrollo%20del%20EDA.ipynb)**
1. Análisis de las tareas requeridas:
* Se analizó el dataframe en su estructura, forma, información, valores nulos y demás.
* Se realizó un histograma para obtener una visión general de distribución de las variables del dataframe.
* Se realizaron algunos gráficos para conocer cuáles fueron las películas más rentables y las que tuvieron mayor presupuesto.
* Se realizó un gráfico de los años en los que las películas fueron lanzadas al mercado.

## 📉📈:Data Science
Se encuentra en el archivo **[Desarrollo del Modelo](Desarrollo%20del%20Modelo.ipynb)**
1. Recomendaremos películas basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas.
* Utilizamos las librerías sklearn CountVectorizer y NearestNeighbors para realizar el modelo de recomendaciones basado en K-neighbors.
* K- neighbors funciona encontrando los "k" puntos de datos más cercanos en función de una medida de distancia, tomando una decisión basada en las etiquetas de clase o de los valores de los vecinos más cercanos.
* Se realizó una función integrada al archivo main.py de la API para poder consultarle una película y nos proprocione las 5 recomendaciones de esta basándose en el Modelo aplicado.

## Conclusión
El proyecto es muy completo para poner en prueba los conocimientos adquiridos, en este video tutorial podrán encontrar una explicación general del proyecto, cómo utilizar la aplicación y sus funcionalidades.

Espero les haya gustado el desarrollo de este proyecto, cualquier consulta pueder escribirme a **[LinkedIn](https://www.linkedin.com/in/alejandra-lizeth-salas-talavera/)**
