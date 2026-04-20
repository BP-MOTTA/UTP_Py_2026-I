import json
try:
    with open("componentes.json", "r", encoding="utf-8") as archivo:
        componentes = json.load(archivo)
    numero_componentes = len(componentes)

    print("Componentes cargados desde componentes.json:")
    for componente in componentes: #esto carga todos los diccionarios hasta terminar
            print(f"Código   : {componente['codigo']}")
            print(f"Nombre   : {componente['nombre']}")
            print(f"Valor    : {componente['valor']}")
            print(f"Unidad   : {componente['unidad']}")
            print(f"Cantidad : {componente['cantidad']}")
            print("-" * 30)
    print(f"Total de componentes cargados: {numero_componentes}")
    
except FileNotFoundError:
    print("Error: El archivo componentes.json no se encontró.")
    print("Si desea crear un nuevo archivo use el programa S4-exp1-Recordatorio.py para generar un nuevo archivo con datos de ejemplo.")
except json.JSONDecodeError:
    print("Error: El archivo componentes.json tiene un formato inválido.")