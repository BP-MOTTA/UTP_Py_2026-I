import json
componentes = [
    {
        "codigo": "C001",
        "nombre": "Resistencia",
        "valor": 220,
        "unidad": "ohm",
        "cantidad": 5   
    },
    {
        "codigo": "C002",
        "nombre": "Condensador",
        "valor": 1100,
        "unidad": "microfaradios",
        "cantidad": 20
    },
    {
        "codigo": "L001",
        "nombre": "Inductor",
        "valor": 10,
        "unidad": "mH",
        "cantida": 3
    }
]
#datos guardados en un archivo Json
with open("componentes.json", "w", encoding="utf-8") as archivo:
    json.dump(componentes, archivo, indent=4, ensure_ascii=False)
print("Datos guardados en componentes.json")