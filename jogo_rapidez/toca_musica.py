from machine import Pin, PWM
from utime import sleep

# Frequência dos tons
C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587
DS5 = 622
E5 = 659
F5 = 698
FS5 = 740
G5 = 784
GS5 = 831
A5 = 880
AS5 = 932
B5 = 988

we_are_the_champions = [
    A4, B4, D5, E5, G5, A5, G5, A5, G5, A5, G5, A5, 0, D5, CS5, D5, CS5, A4, 0,
    FS4, B4, FS4, 0, 0, D5, E5, FS5, A5, FS5, B4, CS5, B4, 0, 0, 0, 0, B4, A4, B4,
    A4, G4, 0, G5, FS5, G5, FS5, E5, 0, FS5, 0, D5, G5, FS5, 0, D5, G5, F5, 0, D5,
    G5, F5, 0, D5, 0, C5, A4, D5
    ]

#Fração de segundos
duracao_notas = [
    0.125, 0.125, 0.125, 0.125, 0.125, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25,
    1, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.5, 1, 1, 0.5, 1, 0.25, 0.25, 0.5, 0.5,
    0.25, 0.25, 1, 1, 0.5, 0.25, 0.25, 1, 0.25, 0.25, 0.5, 0.5, 0.5, 1, 0.25, 0.25,
    0.5, 0.5, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25, 0.5, 0.25,
    0.5, 0.25, 1, 1, 0.25, 0.125, 1]

def play_musica(pino, musica, duracao, volume):

    buzina = PWM(Pin(pino))
    buzina.freq(1000)
    buzina.duty_u16(volume) # de 0 a 65535 = 2**16

    for indice, valor in enumerate(musica):
        if valor == 0:
            sleep(duracao[indice])
            buzina.duty_u16(0)
        else:
            buzina.freq(valor)
            buzina.duty_u16(volume)
            sleep(duracao[indice])

    buzina.deinit()   
    print("Fim da música")