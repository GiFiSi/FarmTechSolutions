# Objetivo do Sistema

O sistema foi desenvolvido para automatizar a irrigação agrícola utilizando:

- Sensores ambientais (umidade do solo, pH e NPK)
- Previsão meteorológica (chuva)
- Atuação automática de uma bomba d’água (via relé)
- Monitoramento das variáveis ambientais em tempo real

---

## 1. Esquema Eletrônico

**Componentes:**
- **ESP32:** microcontrolador central
- **DHT22:** sensor de umidade e temperatura (usado apenas umidade relativa do ar)
- **Botões (3):** simulam sensores de nutrientes N (Nitrogênio), P (Fósforo) e K (Potássio)
  - Botão pressionado = nutriente suficiente
  - Solto = nutriente baixo
- **LDR:** sensor de luminosidade (simula leitura de pH)
  - Leitura analógica (0–4095) convertida para escala de 0 a 14
- **Módulo Relé:** chave para ligar/desligar bomba d’água
- **LED:** indicação visual da bomba ligada

**Principais conexões:**
- DHT22 → pino digital 15
- Botões NPK → pinos 4, 5 e 18 (entrada com pull-up)
- LDR (pH) → pino analógico 34
- Relé (bomba/LED) → pino 2

---

## 2. Lógica do Código – Arduino (.ino)

### 2.1 Leitura dos sensores

- Umidade do ar: `dht.readHumidity()`
- Nutrientes (N, P, K): cada botão retorna `true` quando pressionado (nível adequado)
- pH: leitura analógica convertida em escala de 0 a 14

### 2.2 Condições para irrigação

A bomba só é ligada se **todas** as condições forem satisfeitas:
- Umidade do ar < 60%
- Nitrogênio OK
- Fósforo OK
- Potássio OK
- pH entre 5.5 e 6.5

Se todas forem verdadeiras → ativa irrigação  
Caso contrário → mantém bomba desligada

### 2.3 Controle da bomba

```cpp
digitalWrite(RELE_PIN, irrigar ? HIGH : LOW);
```
- `HIGH`: liga relé (bomba ligada, LED aceso)
- `LOW`: desliga relé (bomba desligada, LED apagado)

---

## 3. Lógica do Código – Python (API do Clima)

### 3.1 Consulta à previsão

A API OpenWeatherMap retorna os dados meteorológicos da cidade configurada (Uberaba).

### 3.2 Condição

```py
if "rain" in dados:
    print("Previsão de chuva detectada - Suspender irrigação")
else:
    print("Sem previsão de chuva - Irrigação liberada")
```

Esse código é complementar: antes de irrigar, o sistema pode verificar se haverá chuva para evitar desperdício de água.

---

## 4. Resumo da Lógica do Sistema

1. **Coleta de dados locais**
   - Umidade do ar (DHT22)
   - Nutrientes (botões NPK)
   - pH (simulado pelo LDR)
2. **Verificação climática**
   - API do clima indica possibilidade de chuva
3. **Decisão**
   - Se chuva prevista → não irrigar
   - Se sem chuva e condições locais adequadas → liga a bomba
4. **Ação**
   - Relé aciona bomba/LED, irrigando a plantação

---

## 5. Fórmula pH (LDR)

```cpp
int ldrValue = analogRead(LDR_PIN);
float ph = map(ldrValue, 0, 4095, 0, 14);
```
