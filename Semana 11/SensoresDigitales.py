from machine import Pin
from time import sleep, ticks_ms
import dht

sensor = dht.DHT22(Pin(15))
led_normal = Pin(2, Pin.OUT)   # LED verde
led_alerta = Pin(5, Pin.OUT)   # LED rojo

UMBRAL_HUMEDAD = 70

print("Sistema con sensor DHT22")
print("muestra,tiempo_ms,temperatura,humedad,estado")

muestra = 1

while True:
    try:
        tiempo = ticks_ms()

        sensor.measure()
        temperatura = sensor.temperature()
        humedad = sensor.humidity()

        if humedad >= UMBRAL_HUMEDAD:
            led_alerta.on()
            led_normal.off()
            estado = "ALERTA"
        else:
            led_alerta.off()
            led_normal.on()
            estado = "NORMAL"

        print(f"{muestra},{tiempo},{temperatura:.2f},{humedad:.2f},{estado}")

        muestra += 1

    except OSError:
        print("Error al leer el sensor DHT22")

    sleep(0.5)