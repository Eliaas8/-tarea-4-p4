from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def obtener_coleccion():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["biblioteca"]
        return db["libros"]
    except ConnectionFailure:
        print("Error: No se pudo conectar a MongoDB")
        exit()
