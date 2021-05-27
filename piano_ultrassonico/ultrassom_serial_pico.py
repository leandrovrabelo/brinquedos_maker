from machine import Pin, UART
import utime

acionador = Pin(3, Pin.OUT)
eco = Pin(2, Pin.IN)
    
def ultrassom(freq_min=250, freq_max=505, distancia_limite=50, pausa=0.7):
    # Dó (C4) tem a frequência de 261 Hz, vou usar 250 Hz como valor mínimo
    # Sí (B4) tem a frequência de 493 Hz, vou usar 510 Hz como valor máximo
    # A distância limite é usada como base para fazer as divisões das escalas
    acionador.low()
    utime.sleep_us(2)
    acionador.high()
    utime.sleep_us(5)
    acionador.low()
    while eco.value() == 0:
        signal_off = utime.ticks_us()
    while eco.value() == 1:
        signal_on = utime.ticks_us()
    tempo_passado = signal_on - signal_off
    distancia = (tempo_passado * 0.0343) / 2

    if distancia > distancia_limite:
        distancia = distancia_limite

    frequencia = int((freq_max - freq_min) * distancia / distancia_limite) + freq_min
    
    #dados são enviados atraves da função print
    print(frequencia)
    utime.sleep(pausa)
    
while True:

    ultrassom()
