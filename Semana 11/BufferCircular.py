# Sistema de control de voltaje a 3 niveles: OK, WARN, ALERT
# Usa ADC, buffer circular, media móvil, histéresis y salida CSV

from machine import Pin, ADC, Timer
from time import ticks_ms

# -----------------------------
# CONFIGURACIÓN DE PINES
# -----------------------------
ADC_PIN = 34

LED_G = Pin(2, Pin.OUT)    # Verde  -> OK
LED_Y = Pin(15, Pin.OUT)   # Amarillo -> WARN
LED_R = Pin(5, Pin.OUT)    # Rojo -> ALERT

# -----------------------------
# CONFIGURACIÓN ADC
# -----------------------------
adc = ADC(Pin(ADC_PIN))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

VREF = 3.3

# -----------------------------
# UMBRALES CON HISTÉRESIS
# -----------------------------
WARN_ON   = 2.30
WARN_OFF  = 2.20
ALERT_ON  = 2.80
ALERT_OFF = 2.70

# Estados:
# 0 = OK
# 1 = WARN
# 2 = ALERT
state = 0

# -----------------------------
# BUFFER CIRCULAR
# -----------------------------
FS_HZ = 10
PERIOD_MS = int(1000 / FS_HZ)

K = 8
buf = [0.0] * K
idx = 0
suma = 0.0
vavg = 0.0
count = 0

# -----------------------------
# BANDERAS DE COMUNICACIÓN
# -----------------------------
sample_ready = False
last_sample_ms = 0
last_raw = 0
last_v = 0.0

# -----------------------------
# FUNCIÓN DE MUESTREO CON TIMER
# -----------------------------
def isr_sample(timer):
    global idx, suma, vavg, count
    global sample_ready, last_sample_ms, last_raw, last_v

    raw = adc.read()
    v = raw * VREF / 4095

    old = buf[idx]
    suma -= old

    buf[idx] = v
    suma += v

    idx += 1
    if idx >= K:
        idx = 0

    if count < K:
        count += 1

    vavg = suma / count

    last_raw = raw
    last_v = v
    last_sample_ms = ticks_ms()
    sample_ready = True

# -----------------------------
# FUNCIÓN PARA SEMÁFORO
# -----------------------------
def set_semaforo(st):
    LED_G.off()
    LED_Y.off()
    LED_R.off()

    if st == 0:
        LED_G.on()
    elif st == 1:
        LED_Y.on()
    else:
        LED_R.on()

def nombre_estado(st):
    if st == 0:
        return "OK"
    elif st == 1:
        return "WARN"
    else:
        return "ALERT"

# -----------------------------
# INICIAR TIMER
# -----------------------------
tm = Timer(0)
tm.init(period=PERIOD_MS, mode=Timer.PERIODIC, callback=isr_sample)

# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
print("Sistema iniciado")
print("muestra,tiempo_ms,raw,voltaje,vavg,estado")

counter = 0

while True:
    if not sample_ready:
        continue

    sample_ready = False
    counter += 1

    # -----------------------------
    # LÓGICA DE HISTÉRESIS
    # -----------------------------
    if state == 0:
        if vavg >= WARN_ON:
            state = 1

    elif state == 1:
        if vavg >= ALERT_ON:
            state = 2
        elif vavg <= WARN_OFF:
            state = 0

    elif state == 2:
        if vavg <= ALERT_OFF:
            state = 1

    set_semaforo(state)

    print("{},{},{},{:.3f},{:.3f},{}".format(
        counter,
        last_sample_ms,
        last_raw,
        last_v,
        vavg,
        nombre_estado(state)
    ))
