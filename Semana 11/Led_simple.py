# Ejemplo 1: Blink + botón (cambia velocidad) - Control de frecuencia de pulso segun dos valores
# Rapidos y lentos
from machine import Pin
import time
#configuraciones de pines
LED = Pin(2, Pin.OUT)
BTN = Pin(4, Pin.IN, Pin.PULL_UP)
#definir la velocidad de apagado (segundos)
fSLOW = 2
SLOW = 1/fSLOW
fFASt = 10
FAST = 1/fFASt
Periodo = SLOW

print("Arrancando ... Presione el boton para cambiar de velocidad")

while True:
    if BTN.value() == 0:
        Periodo = FAST if Periodo == SLOW else SLOW
        print("Velocidad:", "Rapido" if Periodo == FAST else "Lento")
        #Precaucion - antirebote 
        time.sleep(0.25)
        while BTN.value() == 0:
            time.sleep(0.01)
    LED.value(1)
    time.sleep(Periodo)
    LED.value(0)
    time.sleep(Periodo)