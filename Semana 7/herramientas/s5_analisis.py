def clasificacion(valor,umbral=5):
    """Devuelve 'ALERTA' si valor > umbral, si no 'OK'"""
    return "ALERTA" if valor > umbral else "OK" #if corto

def analizar_valores(lista):
    """entrega los valores maximos, minimos y promedios de una lista de datos de analisis

    Args:
        lista (list): lista de datos a estudiar

    Returns:
        floats: _description_
    """
    if len(lista) == 0:
        return None, None, None
    
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum(lista) / len(lista)
    
    return maximo, minimo, promedio