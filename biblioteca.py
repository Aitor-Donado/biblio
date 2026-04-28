"""
La clase Biblioteca (El gestor central)

Tarea a realizar:

Crear la clase Biblioteca que tenga una lista de recursos y una lista de usuarios.
Métodos como agregar_recurso(recurso), registrar_usuario(usuario).
Búsqueda: Un método buscar_por_titulo(titulo) que devuelva una lista con los recursos que coincidan (usando if titulo.lower() in recurso.titulo.lower()).
Préstamo seguro: Un método realizar_prestamo(id_usuario, titulo_recurso) que busque al usuario, busque el recurso, y llame a las funciones correspondientes manejando los try...except para avisar si el usuario no existe o el recurso no está disponible.

"""

from recurso import Libro, DVD, Revista
from usuarios import Usuario

class Biblioteca:
    def __init__(self):
        self.recursos = []
        self.usuarios = []

    def agregar_recurso(self):
        print("""
            Elige el tipo de recurso:
              1. Libro
              2. DVD
              3. Revista
        """)
        tipo = input("Opción: ")
        # Lógica simplificada para el ejemplo
        if tipo == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            genero = input("Género del libro: ")
            anio = input("Año de publicación: ")
            num_paginas = input("Número de páginas: ")
            recurso = Libro(titulo, autor, genero, anio, num_paginas, isbn)
        elif tipo == "2":
            titulo = input("Título del DVD: ")
            autor = input("Autor del DVD: ")
            genero = input("Género del DVD: ")
            anio = input("Año de publicación: ")
            duracion_minutos = input("Duración en minutos: ")
            recurso = DVD(titulo, autor, genero, anio, duracion_minutos)
        elif tipo == "3":
            titulo = input("Título de la revista: ")
            autor = input("Autor del artículo: ")
            genero = input("Género de la revista: ")
            anio = input("Año de publicación: ")
            numero_edicion = input("Número de edición: ")
            recurso = Revista(titulo, autor, genero, anio, numero_edicion)
        else:
            print("Opción no válida.")
            return
        self.recursos.append(recurso)
        print(f"Recurso '{recurso.titulo}' agregado correctamente.")

    def registrar_usuario(self):
        nombre = input("Nombre del usuario: ")
        email = input("Email del usuario: ")
        nuevo_usuario = Usuario(nombre, email)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre} agregado correctamente.")

    def buscar_por_titulo(self):
        titulo = input("Ingrese el título a buscar: ")
        resultados = [r for r in self.recursos if titulo.lower() in r.titulo.lower()]
        for resultado in resultados:
            print(resultado)

    def prestar_recurso(self):
        nombre_usuario = input("Nombre del usuario: ")
        titulo_recurso = input("Título del recurso a prestar: ")
        # Completa el código
        usuario = next((u for u in self.usuarios if u.nombre.lower() == nombre_usuario.lower()), None)
        recurso = next((r for r in self.recursos if r.titulo.lower() == titulo_recurso.lower() and r.disponible), None)
        if usuario and recurso and recurso.disponible:
            recurso.disponible = False
            usuario.recursos_prestados.append(recurso)
            print(f"Recurso '{recurso.titulo}' prestado a {usuario.nombre}.")
        else:
             print("No se han encontrado") 

    def mostrar_recursos(self):
        for recurso in self.recursos:
            print(recurso)  
    
    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario) 

if __name__ == "__main__":
    biblio=Biblioteca()
    libro1 = Libro(titulo = "Viaje al centro de la Tierra", autor = "Julio Verne", genero = "aventuras", anio = "1864", num_paginas= 250, isbn = "978-0140449167")
    print(libro1)
    libro2 = Libro(titulo = "El Señor de los Anillos", autor = "J.R.R. Tolkien", genero = "fantasía", anio = 1954, num_paginas= 1178, isbn = "978-0618640157")
    print(libro2)
    biblio.recursos.append(libro1)
    biblio.recursos.append(libro2)
    # biblio.agregar_recurso()
    biblio.mostrar_recursos()
    usuario1 = Usuario("Juan Pérez", "juanperez@hotmail.com")
    biblio.usuarios.append(usuario1)
    # biblio.registrar_usuario()
    biblio.mostrar_usuarios()
    biblio.prestar_recurso()