# gestion_libros.py

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        self.libros.append({"titulo": titulo, "autor": autor})

    def listar_libros(self):
        return self.libros

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro["titulo"] == titulo:
                return libro
        return None

    def eliminar_libro(self, titulo):
        for i, libro in enumerate(self.libros):
            if libro["titulo"] == titulo:
                del self.libros[i]
                return True
        return False
