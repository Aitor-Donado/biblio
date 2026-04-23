from datetime import date, timedelta
from usuarios import Usuario

class Recurso:
    def __init__(self, titulo, autor, genero, anio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio = self.verifica_anio(anio)
        # Atributos de estado
        self.disponible = True
        self.prestado_a = None
        self.fecha_prestamo = None
        self.fecha_devolucion = None
        
    def prestar(self, usuario):
        if not self.disponible:
            raise Exception(f"El recurso '{self.titulo}' no está disponible para préstamo.")
        self.disponible = False
        self.prestado_a = usuario
        self.fecha_prestamo = date.today()
        # Devolver en tres días        
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=3)
        # Guardar evento en log_biblioteca.txt
        with open("log_biblioteca.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{self.fecha_prestamo}: '{self.titulo}' prestado a {usuario.nombre} hasta {self.fecha_devolucion}.\n")
        usuario.recursos_prestados.append(self.titulo)

    def devolver(self):
        if self.disponible:
            raise Exception(f"El recurso '{self.titulo}' no está prestado.")
        self.disponible = True
        self.fecha_prestamo = None
        self.fecha_devolucion = None
        # Guardar evento en log_biblioteca.txt
        with open("log_biblioteca.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{date.today()}: '{self.titulo}' devuelto por {self.prestado_a.nombre}.\n")
        self.prestado_a.recursos_prestados.remove(self.titulo)
        self.prestado_a.historial_prestamos.append(self.titulo)
        self.prestado_a = None


    def __str__(self):
        return f"""Título: {self.titulo}
            Autor: {self.autor}
            Año: {self.anio}
            Género: {self.genero}
            Disponible: {'Sí' if self.disponible else 'No'}"""


    def verifica_anio(self, anio):
        """
        Verifica que el año sea un número entero positivo entre 1800 y 2050.
        Si el valor no es válido lanza un error ValueError con un mensaje descriptivo.
        """
        if isinstance(anio, str) and anio.isdigit():
            anio = int(anio)
        if not isinstance(anio, int):
            raise ValueError("El año debe ser un número entero.")
        if anio < 1800 or anio > 2050:
            raise ValueError("El año debe estar entre 1800 y 2050.")
        return anio


if __name__ == "__main__":
    libro1 = Recurso(titulo = "Viaje al centro de la Tierra", autor = "Julio Verne", genero = "aventuras", anio = "1864")
    print(libro1)
    libro2 = Recurso(titulo = "El Señor de los Anillos", autor = "J.R.R. Tolkien", genero = "fantasía", anio = 1954)
    print(libro2)
    # Prueba de préstamo
    usuario1 = Usuario(nombre="Juan Pérez", email="juan.perez@example.com")
    libro2.prestar(usuario1)
    print(f"El libro '{libro2.titulo}' ha sido prestado a {libro2.prestado_a} el {libro2.fecha_prestamo} hasta el {libro2.fecha_devolucion}.")
    print(libro2)
    print(f"Recursos prestados a {usuario1.nombre}: {usuario1.recursos_prestados}")
    # Prueba de devolución
    libro2.devolver()
    print(f"El libro '{libro2.titulo}' ha sido devuelto.")
    print(libro2)
    print(f"Recursos prestados a {usuario1.nombre}: {usuario1.recursos_prestados}")
    print(f"Historial de préstamos de {usuario1.nombre}: {usuario1.historial_prestamos}")
