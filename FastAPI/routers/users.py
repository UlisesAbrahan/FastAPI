#En este archivo desarrollaremos una API de usuarios.
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()


@app.get("/usersjson") #asi se trabaja con una api, pero seria tedioso hacer esto con cada usuario, entonces vamos a utilizar objetos
async def usersjson():
    return [{"name":"User1" , "surname": "surname1", "url":"https://google.com", "age":35},
            {"name":"User2" , "surname": "surname2", "url":"https://github.com", "age":35},
            {"name":"User3" , "surname": "surname3", "url":"https://devox.me", "age":35}]

# Dado que Python es un lenguaje orientado a objetos es mejor usar clases y objetos para trabajar con usuarios.
# Para eso creamos una clase User(usuario),

# Entidad User
class User(BaseModel): #Al usar basemodel, no necesitamos crear un constructor, este se encarga de todo, lo unico que necesitamos
    # es definir la clase y los atributos que va a tener la misma, sin necesidad de encapsulamiento y demas.
    
    # atributos de la clase
    id: int
    name: str
    surname: str
    url: str
    age: int

# Como voy a devolver una lista de usuario, creo una lista

users_list = [User(id = 1, name = "User1", surname = "surname1", url= "https://google.com", age = 35),
         User(id = 2, name = "User1", surname = "surname1", url = "https://google.com", age = 35),
         User(id=3, name = "User1", surname = "surname1", url = "https://google.com", age =35)]

@app.get("/users")
async def users():
    return users_list

# --- PARAMETROS POR PATH --- (ir por el path significa que va a ir por el path de la url)
# ejemplo de una funcion para buscar por id, pasando el parametro por path.

@app.get("/user/{id}")  #aca estoy generando una api para buscar un usuario por id
async def user(id: int): # le paso como parametro a la funcion el id del usuario
    search_user(id)
    
# --- PARAMETROS POR QUERY ---
# ejemplo la misma funcion para buscar por id, pasando el parametro por query.
    
@app.get("/userquery/")
async def user(id: int):
    search_user(id)

    
def search_user(id):
    # usamos una funcion de python llamada filter, la cual le pasamos una funcion lambda para filtrar un usuario por un id determinado
    # la funcion filter devuelve un tipo objeto, por eso lo guardo en una variable users
    users = filter(lambda user: user.id == id, users_list) # para obtener el id utilizamos una funcion lambda
    try:
        return list(users)[0] # como obtengo mas de un resultado, devuelvo una lista con todos los objetos
                              # y el [0] lo pongo para que devuelva solamente el primer resultado del id que paso en el path.
    except:
        return {"error":"No se ha encontrado el usuario"}
      # si no pusiera el [0], me devolveria una lista vacia.


# ------------------- OPERACIONES POST -----------------
# POST Se utiliza para insertar un nuevo dato, en este caso vamos a insertar un usuario en nuestra base de datos (users_list)

@app.post("/users/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe en la base de datos") #manejo de excepciones  con fastApi
        #en vez de utilizar el return utilizamos el raise para retornar la excepcion en este caso.
    else:
        users_list.append(user)
        return {"Confirmacion":"Usuario ingresado correctamente"}

#------------ OPERACION PUT -------------
# La operacion PUT, actualiza los datos
    
@app.put("/users/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list): #recorro la lista con un for y uso enumerate para obtener el indice de cada elemento
        # con el indice de cada elemento puedo reemplazar dicho indice por el valor que yo quiera.
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return {"Exito":"El usuario fue actualizado correctamente en la base de datos"}

    if not found:
        return {"Error":"No se ha podido actualizar el usuario"}
    
    #--------OPERACION DELETE----------
    # sirve para eliminar un dato.

@app.delete("/user/{id}")
async def user(id: int):

    found = False
    for index, saved_user in enumerate(users_list): #Recorro la lista de usuarios por indice
            if saved_user.id == id:
                del users_list[index] #Si encuentra el id que le mando en el path dentro de la lista, uso la funcion del para eliminar dicho elemento.
                found = True
                return {"Exito":"Usuario eliminado correctamente"}
    if not found:
            return {"Error", "No se pudo eliminar el usuario"}    
