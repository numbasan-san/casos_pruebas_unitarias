# En el archivo test_estadisticas.py
import pytest
from estadisticas import *

def test_calcular_promedio_con_lista_vacia():
    with pytest.raises(ValueError):
        calcular_promedio([])

def test_calcular_promedio_con_valores_positivos():
    assert calcular_promedio([1, 2, 3, 4, 5]) == 3

def test_calcular_promedio_con_valores_negativos():
    assert calcular_promedio([-1, -2, -3, -4, -5]) == -3

def test_encontrar_maximo_con_lista_vacia():
    with pytest.raises(ValueError):
        encontrar_maximo([])

def test_encontrar_maximo_con_valores_positivos():
    assert encontrar_maximo([1, 2, 3, 4, 5]) == 5

def test_encontrar_maximo_con_valores_negativos():
    assert encontrar_maximo([-1, -2, -3, -4, -5]) == -1

def test_encontrar_minimo_con_lista_vacia():
    with pytest.raises(ValueError):
        encontrar_minimo([])

def test_encontrar_minimo_con_valores_positivos():
    assert encontrar_minimo([1, 2, 3, 4, 5]) == 1

def test_encontrar_minimo_con_valores_negativos():
    assert encontrar_minimo([-1, -2, -3, -4, -5]) == -5

def test_calcular_suma_con_lista_vacia():
    with pytest.raises(ValueError):
        calcular_suma([])

def test_calcular_suma_con_valores_positivos():
    assert calcular_suma([1, 2, 3, 4, 5]) == 15

def test_calcular_suma_con_valores_negativos():
    assert calcular_suma([-1, -2, -3, -4, -5]) == -15
