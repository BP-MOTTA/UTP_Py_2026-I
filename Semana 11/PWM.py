####################PWM FRECUENCIAS
from machine import Pin, PWM
import time

buzz = PWM(Pin(15))
volumen = 128

# Escala simple de 4 notas (frecuencias aproximadas)
notas = [261, 261, 293 ,261, 349,  329, 261, 261, 293 ,261, 392,  349]  # A4, C5, E5, A5


print("Tocando tonos en buzzer (GPIO15)...")
for f in notas:
    buzz.freq(f)
    buzz.duty(volumen)
    print("frecuencia=", f  ,"Hz")
    time.sleep(0.5)
##########################################PWM para duty
buzz.duty(0)   # apagar
buzz.deinit()

from machine import Pin, PWM
from time import sleep_ms

pwm=PWM(Pin(5),freq=1000, duty=0)

for d in (0, 1, 2, 3, 4, 0):
    pwm.duty(d)
    sleep_ms(1000)

pwm.deinit()