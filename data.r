
library(httr)
library(jsonlite)

areas <- c(1000000, 3141592.65) 
totais_insumos <- c(300000, 942477.80) 

media_area <- mean(areas) 
desvio_area <- sd(areas)

media_insumos <- mean(totais_insumos) 
desvio_insumos <- sd(totais_insumos) 

cat("_____________________________________________________________________________________________________")
cat("_____________________________________________________________________________________________________")
cat("_____________________________________________________________________________________________________")
cat("_____________________________________________________________________________________________________")
cat("_____________________________________________________________________________________________________")
cat("Estatísticas das áreas plantadas (em m²):\n") 
cat("Média:", media_area, "\nDesvio padrão:", desvio_area, "\n\n") 
cat("Estatísticas dos insumos aplicados (em mL):\n") 
cat("Média:", media_insumos, "\nDesvio padrão:", desvio_insumos, "\n") 

# Usando API Open-Meteo (sem autenticação) 
response <- GET("https://api.open-meteo.com/v1/forecast?latitude=-19.75&longitude=-47.93&current=temperature_2m,precipitation") 
dados <- fromJSON(content(response, "text")) 
cat("Temperatura atual (°C):", dados$current$temperature_2m, "\n") 
cat("Precipitação (mm):", dados$current$precipitation, "\n") 