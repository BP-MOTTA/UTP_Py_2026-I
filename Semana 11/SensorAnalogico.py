# Ejemplo: sensor de humedad con escalado y alerta por LEDs

from machine import Pin, ADC
from time import sleep, ticks_ms

# -----------------------------
# CONFIGURACIÓN DEL ADC
# -----------------------------
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)      # Permite leer aproximadamente hasta 3.3 V
adc.width(ADC.WIDTH_12BIT)    # Lectura de 0 a 4095

# -----------------------------
# CONFIGURACIÓN DE LEDS
# -----------------------------
led_alerta = Pin(5, Pin.OUT)  # LED rojo
led_normal = Pin(2, Pin.OUT)  # LED verde

# -----------------------------
# CONSTANTES DEL SISTEMA
# -----------------------------
VREF = 3.3
ADC_MIN = 0
ADC_MAX = 4095

HUMEDAD_MIN = 0
HUMEDAD_MAX = 100

UMBRAL_HUMEDAD = 70  # Porcentaje de humedad

def leer_adc():
    """
    Lee el valor crudo del ADC.
    Retorna un número entre 0 y 4095.
    """
    return adc.read()


def adc_a_voltaje(valor_adc):
    """
    Convierte el valor ADC a voltaje.
    """
    voltaje = valor_adc * VREF / ADC_MAX
    return voltaje


def normalizar(valor, entrada_min, entrada_max):
    """
    Convierte un valor a una escala entre 0 y 1.
    """
    return (valor - entrada_min) / (entrada_max - entrada_min)


def escalar(valor_norm, salida_min, salida_max):
    """
    Convierte un valor normalizado a una escala física.
    """
    return salida_min + valor_norm * (salida_max - salida_min)


def adc_a_humedad(valor_adc):
    """
    Convierte el valor ADC a porcentaje de humedad.
    """
    adc_norm = normalizar(valor_adc, ADC_MIN, ADC_MAX)
    humedad = escalar(adc_norm, HUMEDAD_MIN, HUMEDAD_MAX)
    return adc_norm, humedad


def controlar_leds(humedad):
    """
    Enciende LED rojo si supera el umbral.
    Enciende LED verde si está en estado normal.
    """
    if humedad >= UMBRAL_HUMEDAD:
        led_alerta.on()
        led_normal.off()
        estado = "ALERTA"
    else:
        led_alerta.off()
        led_normal.on()
        estado = "NORMAL"

    return estado


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------

print("Sistema de monitoreo de humedad")
print("muestra,tiempo_ms,adc,voltaje,adc_norm,humedad,estado")

muestra = 1

while True:
    tiempo = ticks_ms()

    valor_adc = leer_adc()
    voltaje = adc_a_voltaje(valor_adc)
    adc_norm, humedad = adc_a_humedad(valor_adc)

    estado = controlar_leds(humedad)

    print(f"{muestra},{tiempo},{valor_adc},{voltaje:.3f},{adc_norm:.3f},{humedad:.2f},{estado}")

    muestra += 1
    sleep(0.5)