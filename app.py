from db import obtener_coleccion
from bson.objectid import ObjectId

coleccion = obtener_coleccion()

def agregar_libro():
    libro = {
        "titulo": input("Título: ").strip(),
        "autor": input("Autor: ").strip(),
        "genero": input("Género: ").strip(),
        "estado": input("Estado de lectura (leído / pendiente): ").strip()
    }

    if not all(libro.values()):
        print("Error: Todos los campos son obligatorios")
        return

    coleccion.insert_one(libro)
    print("Libro agregado correctamente")

def listar_libros():
    libros = list(coleccion.find())
    if not libros:
        print("No hay libros registrados")
        return

    for libro in libros:
        print(f"{libro['_id']} | {libro['titulo']} | {libro['autor']} | {libro['genero']} | {libro['estado']}")

def buscar_libro():
    campo = input("Buscar por (titulo / autor / genero): ").strip()
    valor = input("Valor de búsqueda: ").strip()

    resultados = list(coleccion.find({campo: {"$regex": valor, "$options": "i"}}))

    if not resultados:
        print("No se encontraron resultados")
        return

    for libro in resultados:
        print(f"{libro['_id']} | {libro['titulo']} | {libro['autor']} | {libro['genero']} | {libro['estado']}")

def actualizar_libro():
    id_libro = input("ID del libro a actualizar: ").strip()

    campo = input("Campo a modificar (titulo / autor / genero / estado): ").strip()
    nuevo_valor = input("Nuevo valor: ").strip()

    resultado = coleccion.update_one(
        {"_id": ObjectId(id_libro)},
        {"$set": {campo: nuevo_valor}}
    )

    if resultado.matched_count == 0:
        print("Libro no encontrado")
    else:
        print("Libro actualizado correctamente")

def eliminar_libro():
    id_libro = input("ID del libro a eliminar: ").strip()

    resultado = coleccion.delete_one({"_id": ObjectId(id_libro)})

    if resultado.deleted_count == 0:
        print("Libro no encontrado")
    else:
        print("Libro eliminado correctamente")

def menu():
    while True:
        print("\n--- Biblioteca Personal ---")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            listar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            actualizar_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
