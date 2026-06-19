#la histerersis permite evitar que cerca del umbral se geneneren tintineos, relacionado a la sensibilidad del sensor
#normalmente sih histeresis harias lo siguientes
#Si humedad >= 70% → ALERTA,  Si humedad < 70%  → NORMAL
#con histeresis tenemos que crear un intervalo de accion
#Si humedad >= 70% → entra en ALERTA / Humedad sube hasta 70%  → activa alerta
#Si humedad <= 60% → vuelve a NORMAL ? Humedad baja hasta 60%  → desactiva alerta


# Sistema analógico con:
# - Conversión ADC a humedad
# - Buffer circular
# - Promedio móvil
# - Histéresis
# - LEDs de estado
# - Pantalla OLED SSD1306
# - Salida CSV

from machine import Pin, ADC, I2C
from time import sleep, ticks_ms
import ssd1306

#configuracion de ADC|
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)      # Permite leer aprox. hasta 3.3 V
adc.width(ADC.WIDTH_12BIT)    # Lectura de 0 a 4095
#configuracion de outputs
led_normal = Pin(2, Pin.OUT)   # LED verde
led_alerta = Pin(5, Pin.OUT)   # LED rojo
# CONFIGURACIÓN DE LA PANTALLA OLED
i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(
    128,
    64,
    i2c,
    addr=0x3C
)


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

# buffer circular para suavizado de datos.
K = 8 #la cantidad de datos que se van a guardar provisionalmente 
buf = [0.0] * K #generar los espacios
idx = 0
suma = 0.0
count = 0

def actualizar_buffer(nueva_muestra):
    global idx, suma, count

    valor_antiguo = buf[idx]
    suma -= valor_antiguo

    buf[idx] = nueva_muestra
    suma += nueva_muestra

    idx += 1

    if idx >= K:
        idx = 0

    if count < K:
        count += 1

    promedio = suma / count

    return promedio

# ==================================================
# PANTALLA OLED
# ==================================================

def actualizar_pantalla(
    valor_adc,
    voltaje,
    humedad,
    humedad_promedio,
    estado
):
    """
    Muestra los datos del sistema en la pantalla OLED.
    """

    # Limpiar la memoria gráfica.
    oled.fill(0)

    # Escribir información.
    oled.text("MONITOR HUMEDAD", 4, 0)

    oled.text(
        "ADC: %4d" % valor_adc,
        0,
        12
    )

    oled.text(
        "Volt: %.2f V" % voltaje,
        0,
        22
    )

    oled.text(
        "Hum: %.1f %%" % humedad,
        0,
        32
    )

    oled.text(
        "Prom: %.1f %%" % humedad_promedio,
        0,
        42
    )

    oled.text(
        "Estado: " + estado,
        0,
        54
    )

    # Enviar la información a la pantalla.
    oled.show()


# ==================================================
# MENSAJE INICIAL EN LA OLED
# ==================================================

oled.fill(0)
oled.text("SISTEMA INICIADO", 0, 18)
oled.text("ESP32 + SSD1306", 0, 34)
oled.show()

sleep(2)



print("Sistema analógico con histéresis")
print("muestra,tiempo_ms,adc,voltaje,humedad,estado")
muestra = 1 #para la creacion del csv
alerta = False
while True:
    tiempo = ticks_ms()

    valor_adc = leer_adc()
    voltaje = adc_a_voltaje(valor_adc)
    humedad = adc_a_humedad(valor_adc)
    humedad_estable = actualizar_buffer(humedad)

    alerta_humedad = aplicar_histeresis(humedad_estable,alerta)
    estado = controlar_leds(alerta_humedad)

    # Actualizar pantalla.
    actualizar_pantalla(
        valor_adc,
        voltaje,
        humedad,
        humedad_estable,
        estado
    )
    print(f"{muestra},{tiempo},{valor_adc},{voltaje:.3f},{humedad:.2f},{estado}")
    muestra += 1
    sleep(0.5)
