# Arquivos necessários para executar a demonstração prática do projeto do Grupo 4 sobre Bancos NoSQL de Séries Temporais (InfluxDB).

## 📁 Conteúdo

### docker-compose.yml
Sobe o InfluxDB já configurado (usuário, senha, organização e bucket).

### insert.sh
Script com comando curl para inserir dados de sensores (ex.: temperatura).

### query.flux
Consulta básica usando Flux para recuperar os dados recém-inseridos.

## ▶️ Como executar a demo
### 1) Subir o InfluxDB
docker-compose up -d

 Acesse a interface:
http://localhost:8086
Copie o token gerado pelo InfluxDB.

### 2) Inserir dados

Edite o script insert.sh e coloque o token:

TOKEN="SEU_TOKEN_AQUI"
./insert.sh


Isso envia um ponto de dados, por exemplo:

temperatura,sensor=livingroom value=23.4 <timestamp>

### 3) Rodar a consulta

Abra o InfluxDB na interface web:

Data Explorer → Script Editor → cole o conteúdo de query.flux:

from(bucket: "sensores")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "temperatura")


Execute e visualize os dados.

## ✔️ Pré-requisitos

Docker + Docker Compose

InfluxDB rodando via docker-compose

Token da organização/bucket criado automaticamente
