
import pytest
from gestion_libros import Biblioteca

@pytest.fixture
def biblioteca_vacia():
    return Biblioteca()

@pytest.fixture
def biblioteca_con_libros():
    biblio = Biblioteca()
    biblio.agregar_libro("Harry Potter", "J.K. Rowling")
    biblio.agregar_libro("El Señor de los Anillos", "J.R.R. Tolkien")
    return biblio

@pytest.mark.parametrize("titulo, autor", [("Cien años de soledad", "Gabriel Garcia Marquez"), ("1984", "George Orwell")])
def test_agregar_libro(biblioteca_vacia, titulo, autor):
    biblioteca_vacia.agregar_libro(titulo, autor)
    assert len(biblioteca_vacia.libros) == 1

def test_listar_libros(biblioteca_con_libros):
    libros = biblioteca_con_libros.listar_libros()
    assert len(libros) == 2

@pytest.mark.parametrize("titulo_existente, autor", [("Harry Potter", "J.K. Rowling"), ("El Señor de los Anillos", "J.R.R. Tolkien")])
def test_buscar_libro_existente(biblioteca_con_libros, titulo_existente, autor):
    libro = biblioteca_con_libros.buscar_libro_por_titulo(titulo_existente)
    assert libro is not None
    assert libro["titulo"] == titulo_existente
    assert libro["autor"] == autor

@pytest.mark.parametrize("titulo_inexistente", ["El Arte de la Guerra", "El código Da Vinci", "Moby Dick"])
def test_buscar_libro_inexistente(biblioteca_con_libros, titulo_inexistente):
    libro = biblioteca_con_libros.buscar_libro_por_titulo(titulo_inexistente)
    assert libro is None

@pytest.mark.parametrize("titulo_existente", ["Harry Potter", "El Señor de los Anillos"])
def test_eliminar_libro_existente(biblioteca_con_libros, titulo_existente):
    assert biblioteca_con_libros.eliminar_libro(titulo_existente) is True
    assert len(biblioteca_con_libros.libros) == 1

@pytest.mark.parametrize("titulo_inexistente", ["El código Da Vinci", "Moby Dick"])
def test_eliminar_libro_inexistente(biblioteca_con_libros, titulo_inexistente):
    assert biblioteca_con_libros.eliminar_libro(titulo_inexistente) is False
    assert len(biblioteca_con_libros.libros) == 2