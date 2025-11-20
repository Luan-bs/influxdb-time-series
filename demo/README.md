# Demonstração prática — exemplo pronto

Cenário sugerido: sensores IoT enviando temperatura e umidade.

## docker-compose.yml (exemplo simples):
version: '3'
services:
  influxdb:
    image: influxdb:2.7
    ports:
      - "8086:8086"
    environment:
      - DOCKER_INFLUXDB_INIT_MODE=setup
      - DOCKER_INFLUXDB_INIT_USERNAME=admin
      - DOCKER_INFLUXDB_INIT_PASSWORD=admin123
      - DOCKER_INFLUXDB_INIT_ORG=grupo4
      - DOCKER_INFLUXDB_INIT_BUCKET=sensores


## Inserção de dados (curl):
curl -X POST http://localhost:8086/api/v2/write?org=grupo4&bucket=sensores&precision=s \
  -H "Authorization: Token <token>" \
  --data-raw "temperatura,sensor=livingroom value=23.4 $(date +%s)"

## Consulta (Flux):
from(bucket: "sensores")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "temperatura")

## Mostre como tags viram índices, explicando porque “sensor=livingroom” permite buscas rápidas.
