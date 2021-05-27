//Define os pinos para o trigger e echo
#define acionador 4
#define eco 5
#define freq_min 250
#define freq_max 505
#define distancia_limite 50
#define pausa 700

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(acionador, OUTPUT);
  pinMode(eco, INPUT);
}

void loop() {
  digitalWrite(acionador, LOW);
  delayMicroseconds(2);
  digitalWrite(acionador, HIGH);
  delayMicroseconds(10);
  digitalWrite(acionador, LOW);

 const unsigned long duracao = pulseIn(eco, HIGH);
 int distancia = duracao/29/2;
 
 if(distancia > distancia_limite){
  distancia = distancia_limite;
 }

 int frequencia = (freq_max - freq_min) * distancia / distancia_limite + freq_min;
 Serial.println(frequencia);
 delay(pausa);
 }
