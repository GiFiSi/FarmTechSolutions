import requests

CITY = "Uberaba"
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric'
 
def previsao_chuva():
  r = requests.get(URL)
  dados = r.json()
  if "rain" in dados:
      return True
  return False
 
if previsao_chuva():
  print("Previsão de chuva detectada - Suspender irrigação")
else:
  print("Sem previsão de chuva - Irrigação liberada")
