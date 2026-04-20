#diccionarios - son mutables y le dan un nombre a cada indice 
#COD04524=["Juan",33,"Ingenieria Ambiental",975555675,True,0.35]
COD04524={"nombre":"Juan","edad":33,"carrera":"Ingenieria Ambiental","contacto":975555675,"descuento":0.35}
print(f"la edad de {COD04524['nombre']} es: {COD04524['edad']}, su numero es el {COD04524['contacto']} y es {COD04524['carrera']}")
COD04524["carrera"]="Mg en Ingenieria Ambiental"
print(f"la edad de {COD04524['nombre']} es: {COD04524['edad']}, su numero es el {COD04524['contacto']} y es {COD04524['carrera']}")

#datos de una fuente de voltaje
fuente_voltaje={
    "voltaje":220,
    "corriente":10,
    "potencia":2200,
    "frecuencia":60
}

print(f"la potencia de la fuente de voltaje es: {fuente_voltaje['potencia']} W, su voltaje es de {fuente_voltaje['voltaje']} V y su corriente es de {fuente_voltaje['corriente']} A")

medicion={
    "componente":"resistencia",
    "codigo":"R2",
    "valor_nominal":1000,
    "valor_medido":980,
}
error=(medicion["valor_nominal"]-medicion["valor_medido"])/medicion["valor_nominal"]*100
print(f"el error porcentual del componente {medicion['componente']} ({medicion['codigo']}) es: {error:.2f}%")

#para varios componentes
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
        "potencia":2200,
        "frecuencia":60
    }
}

print("Marca del multimetro:", laboratorio["multimetro"]["marca"])
print("Canales del osciloscopio:", laboratorio["osciloscopio"]["canales"])