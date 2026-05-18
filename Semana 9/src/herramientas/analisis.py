def desviacion_estandar(lista):
    n = len(lista)

    if n == 0:
        return None

    promedio = sum(lista) / n
    suma_cuadrados = 0

    for x in lista:
        suma_cuadrados += (x - promedio) ** 2

    varianza = suma_cuadrados / n
    desv = varianza ** 0.5

    return desv

def analizar_valores(lista):
    n = len(lista)

    if n == 0:
        return None, None, None, None

    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista) / n

    suma_cuadrados = 0
    for x in lista:
        suma_cuadrados += (x - promedio) ** 2

    varianza = suma_cuadrados / n
    desv = varianza ** 0.5

    return maximo, minimo, promedio, desv