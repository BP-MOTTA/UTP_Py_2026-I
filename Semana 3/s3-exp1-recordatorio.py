#sistema de control de temperatura
#ingresar el valor de la temperatura y determina si ha activado o no un sensor
valor_txt=input("Ingrese el valor de la temperatura: ")
#condicion de error
try:
    valor_temp=float(valor_txt)   
    #condicionales para determinar el estado del sensor
    if valor_temp >= 10:
        print("ALERTA TEMPERATURA ALTA")
    elif valor_temp <= 0:
        print("ALERTA TEMPERATURA BAJA")
    else:
        print("Temperatura adecuada")
except ValueError:
    print("Error: Ingrese un valor numérico para la temperatura, por ejemplo: 25.5")