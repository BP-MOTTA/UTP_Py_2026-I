import json

with open("componentes.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    
print("Nombre:", datos["nombre"])
print("Resistencia:", datos["resistencia_ohm"], "ohm")
print("Tolerancia:", datos["tolerancia"])
print("Potencia:", datos["potencia_w"], "W")

with open("sensores.json", "r", encoding="utf-8") as archivo2:
    sensores = json.load(archivo2)

print("Tipo de sensor 1:", sensores["sensor1"]["tipo"])
print("Rango del sensor 1:", sensores["sensor1"]["rango_c"], "°C")
print("Tipo de sensor 2:", sensores["sensor2"]["tipo"])

laboratorio = {
    "multimetro": {
        "marca": "Fluke",
        "modelo": "117",
        "precision": "0.5%"
    },
    "osciloscopio": {
        "marca": "Rigol",
        "canales": 2,
        "frecuencia_mhz": 100
    },
    "fuente_voltaje": {
        "marca":"Agilent",
        "voltaje":220,
        "corriente":10,
        "potencia":1100,
        "frecuencia":60
    }
}
with open("laboratorio.json", "w", encoding="utf-8") as archivo:
    json.dump(laboratorio, archivo, indent=4)