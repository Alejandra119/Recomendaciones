<h1 align="center"> Proyecto_ Modelo de Recomendaciones </h1>

### Desarrollado por: Alejandra Salas
Objetivo: Utilizar los datasets de películas y directores para brindar 5 recomendaciones por cada película mediante una API.

## Índice

* [Descripción del proyecto](#descripción-del-proyecto)

* [Procesos realizados](#Procesos-realizados)

* [Características de la aplicación y demostración](#Características-de-la-aplicación-y-demostración)

* [Acceso al proyecto](#acceso-proyecto)

* [Tecnologías utilizadas](#tecnologías-utilizadas)

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

## :hammer:Data Engeneering
**`ETL (Extract, Transform and Load)`**
1. Contamos con los datasets "movies" que contiene una serie de variables con diversas películas, así mismo, tenemos el dataset "credits" que contiene la ista del personal que participó por cada película.

2. Necesitamos realizar las siguientes tareas:

* Algunos campos de los datasets están anidados, se deberán desanidarlos o buscar la manera de acceder a esos datos sin desanidarlos.

* Rellenar con 0 los campos revenue y budget.

* Eliminar los valores nulos del campo release date.

* Las fechas deberán tener el formato AAAA-mm-dd y crear la columna release_year donde se extraerá el año de la fecha de estreno.

* Crear return dividiendo revenue / budget, si no hay datos disponibles, estos deberá ser 0.

* Eliminar las columnas que no serán utilizadas.

3. Desarrollo de la API.
Se utilizó FAST API para como servidor local para poder visualizar las funciones, esto se encuentra en el archivo **[main.py](dataApi/main.py)**

4. Despliegue de la API.
Se utilizó RENDER para realizar el deploy de nuestra API local.

5.



