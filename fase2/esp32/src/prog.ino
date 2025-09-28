#include "DHT.h"
 
#define DHTPIN 15
#define DHTTYPE DHT22
 
// Botões NPK
#define BTN_N 4
#define BTN_P 5
#define BTN_K 18
 
// LDR (pH)
#define LDR_PIN 34
 
// Relé (bomba d'água)
#define RELE_PIN 2
 
DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
Serial.begin(115200);
dht.begin();
 
pinMode(BTN_N, INPUT_PULLUP);
pinMode(BTN_P, INPUT_PULLUP);
pinMode(BTN_K, INPUT_PULLUP);
pinMode(RELE_PIN, OUTPUT);
}
 
void loop() {
// Leitura de umidade
float umidade = dht.readHumidity();
 
// Leitura NPK (botões)
bool nivelN = !digitalRead(BTN_N); // pressionado = true
bool nivelP = !digitalRead(BTN_P);
bool nivelK = !digitalRead(BTN_K);
 
// Leitura pH via LDR
int ldrValue = analogRead(LDR_PIN);
float ph = map(ldrValue, 0, 4095, 0, 14); // escala 0-14
 
// Exibir dados
Serial.print("Umidade: "); Serial.print(umidade); Serial.println("%");
Serial.print("N: "); Serial.print(nivelN ? "OK" : "Baixo");
Serial.print(" | P: "); Serial.print(nivelP ? "OK" : "Baixo");
Serial.print(" | K: "); Serial.println(nivelK ? "OK" : "Baixo");
Serial.print("pH: "); Serial.println(ph);
 
// Lógica de irrigação
bool irrigar = false;
 
if (umidade < 60 && nivelN && nivelP && nivelK && ph >= 5.5 && ph <= 6.5) {
  irrigar = true;
}
 
// Controle da bomba
digitalWrite(RELE_PIN, irrigar ? HIGH : LOW);
 
if (irrigar) {
  Serial.println("Bomba LIGADA - Irrigando...");
} else {
  Serial.println("Bomba DESLIGADA");
}
 
delay(2000);
}
