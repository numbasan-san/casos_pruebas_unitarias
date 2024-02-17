# En el archivo estadisticas.py

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    if not numeros:
        raise ValueError("La lista de números está vacía")
    return sum(numeros) / len(numeros)

def encontrar_maximo(numeros):
    """Encuentra el valor máximo en una lista de números."""
    if not numeros:
        raise ValueError("La lista de números está vacía")
    return max(numeros)

def encontrar_minimo(numeros):
    """Encuentra el valor mínimo en una lista de números."""
    if not numeros:
        raise ValueError("La lista de números está vacía")
    return min(numeros)

def calcular_suma(numeros):
    """Calcula la suma de una lista de números."""
    if not numeros:
        raise ValueError("La lista de números está vacía")
    return sum(numeros)
