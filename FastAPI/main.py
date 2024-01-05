from fastapi import FastAPI

app= FastAPI() #aqui creo una variablle llamada app y llamo a una clase llamada FastAPI()


@app.get("/") #con @app accedo al contexto de fastapi, y estoy haciendo un get a una ruta (/) en este caso
async def root(): #la funcion que usamos para llamar al servidor tiene que ser asincrona
    return "Hola FastAPI ..!" #aca defino una funcion en python que me devuelve una cadena

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"} #esto es un json, basicamente un elemento clave - valor

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL + C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# POST: para crear datos.
# GET: para leer datos.
# PUT: para actualizar datos.
# DETELE: para borrar datos.