#la histerersis permite evitar que cerca del umbral se geneneren tintineos, relacionado a la sensibilidad del sensor
#normalmente sih histeresis harias lo siguientes
#Si humedad >= 70% → ALERTA,  Si humedad < 70%  → NORMAL
#con histeresis tenemos que crear un intervalo de accion
#Si humedad >= 70% → entra en ALERTA / Humedad sube hasta 70%  → activa alerta
#Si humedad <= 60% → vuelve a NORMAL ? Humedad baja hasta 60%  → desactiva alerta
from machine import Pin, ADC
from time import sleep, ticks_ms


#configuracion de ADC|
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)      # Permite leer aprox. hasta 3.3 V
adc.width(ADC.WIDTH_12BIT)    # Lectura de 0 a 4095
#configuracion de outputs
led_normal = Pin(2, Pin.OUT)   # LED verde
led_alerta = Pin(5, Pin.OUT)   # LED rojo
#valor de constantes
VREF = 3.3
ADC_MAX = 4095

UMBRAL_ALTO = 70   # Activa alerta
UMBRAL_BAJO = 60   # Desactiva alerta

def leer_adc():
    return adc.read()


def adc_a_voltaje(valor_adc):
    return valor_adc * VREF / ADC_MAX


def adc_a_humedad(valor_adc):
    humedad = valor_adc * 100 / ADC_MAX
    return humedad

def aplicar_histeresis(humedad, estado_actual):
    """
    estado_actual:
    False → NORMAL
    True  → ALERTA
    """
    if estado_actual == False and humedad >= UMBRAL_ALTO:
        estado_actual = True

    if estado_actual == True and humedad <= UMBRAL_BAJO:
        estado_actual = False
    return estado_actual

def controlar_leds(alerta):
    if alerta:
        led_alerta.on()
        led_normal.off()
        return "ALERTA"
    else:
        led_alerta.off()
        led_normal.on()
        return "NORMAL"

print("Sistema analógico con histéresis")
print("muestra,tiempo_ms,adc,voltaje,humedad,estado")
muestra = 1 #para la creacion del csv
alerta = False
while True:
    tiempo = ticks_ms()

    valor_adc = leer_adc()
    voltaje = adc_a_voltaje(valor_adc)
    humedad = adc_a_humedad(valor_adc)

    alerta_humedad = aplicar_histeresis(humedad,alerta)
    estado = controlar_leds(alerta_humedad)

    print(f"{muestra},{tiempo},{valor_adc},{voltaje:.3f},{humedad:.2f},{estado}")
    muestra += 1
    sleep(0.5)
