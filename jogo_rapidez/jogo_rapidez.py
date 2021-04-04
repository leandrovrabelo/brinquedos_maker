from machine import Pin, PWM
import utime
import urandom
from toca_musica import we_are_the_champions, duracao_notas, play_musica

# Configurando LEDs
led_jogo = Pin(18, Pin.OUT) # Led principal que vai acender e apagar para dar inicio ao jogo
led_vermelho = Pin(17, Pin.OUT) # Vai mostrar se o jogador foi mais rápido ou ganhou
led_azul = Pin(16, Pin.OUT) # Vai mostrar se o jogador foi mais rápido ou ganhou

# Configurando Botões
botao_vermelho = Pin(19, Pin.IN, Pin.PULL_DOWN)
botao_azul = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Essas variáveis vão registrar a hora que clicou o botão
clique_vermelho = 0 
clique_azul = 0

# Registrador os pontos
pontos = {"Vermelho":0, "Azul":0}

botao_mais_rapido = None
agora = utime.ticks_ms()
pausa = int(urandom.uniform(3, 10) * 1000) # em milisegundos
hora_led_apaga = utime.ticks_add(agora, pausa)
        
def grava_tempo(pino):
    #print("Pino",pino)
    global hora_led_apaga
    global botao_mais_rapido, botao_vermelho, botao_azul
    global clique_vermelho, clique_azul
    botao_mais_rapido = pino
    hora_clique = utime.ticks_ms()
    # Não pode fazer operações matemáticas neste módulo de utime, por isso a função ticks_diff abaixo
    dif_horarios = utime.ticks_diff(hora_clique, hora_led_apaga) 
    if dif_horarios < 0:
        print("Apertou o botão muito cedo jovem!")
    
    elif botao_mais_rapido == botao_vermelho and dif_horarios > 0:
        clique_vermelho = utime.ticks_ms()
        
    elif botao_mais_rapido == botao_azul and dif_horarios > 0:
        clique_azul = utime.ticks_ms()
    else:
        print("Bugou!")

def blink(led, pausa, vezes):
    for i in range(vezes):
        led.high()
        utime.sleep(pausa)
        led.low()
        utime.sleep(pausa)

# Criando as interrupções
botao_vermelho.irq(trigger=Pin.IRQ_RISING, handler=grava_tempo)
botao_azul.irq(trigger=Pin.IRQ_RISING, handler=grava_tempo)

while True:
    # Atualizando as variáveis em cada loop
    agora = utime.ticks_ms()
    pausa = int(urandom.uniform(3, 10) * 1000) # em milisegundos
    hora_led_apaga = utime.ticks_add(agora, pausa)
    
    # Começou o jogo
    print("Acendendo o LED")
    led_jogo.high()
    utime.sleep(pausa/1000)
    led_jogo.low()
    print("APEEERTA!!!!")
    
    # Espera um pouco pra clicar
    utime.sleep(1.5)
    
    checa_tempos = utime.ticks_diff(clique_vermelho, clique_azul)

    if checa_tempos > 0:
        pontos["Azul"] += 1
        print("Azul foi mais rápido! Pontos:", pontos["Azul"])
        blink(led=led_azul, pausa=0.5, vezes=3)
        
    elif checa_tempos < 0:
        pontos["Vermelho"] += 1
        print("Vermelho foi mais rápido! Pontos:", pontos["Vermelho"])
        blink(led=led_vermelho, pausa=0.5, vezes=3)
        
    else:
        print("EMPATARAM!!!")
        for i in range(10):
            led_azul.high()
            led_vermelho.high()
            utime.sleep(0.05)
            led_azul.low()
            led_vermelho.low()
            utime.sleep(0.05)
    
    # Ganha quem fizer 3 pontos primeiro, vamos checar:
    for key, valor in pontos.items():
        if valor == 3:
            print(key.upper(), "GANHOU O JOGO!!!\n")
            # Zerando pontos
            pontos["Vermelho"] = 0
            pontos["Azul"] = 0
            if key == "Vermelho":
                blink(led_vermelho, pausa=0.05, vezes=20)
            else:
                blink(led_azul, pausa=0.05, vezes=20)

    utime.sleep(1)

    # Reiniciando variáveis
    botao_mais_rapido = None
    # tempo alto pra não ganhar no novo loop se não apertarem
    clique_vermelho = 10_000_000 
    clique_azul = 10_000_000 
