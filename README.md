# influxdb-time-series
Projeto do Grupo 4 sobre bancos NoSQL de Séries Temporais, incluindo slides, demonstração prática com InfluxDB, Fit Map, scripts e vídeo de apresentação.

📌 Sugestão para o grupo: InfluxDB (melhor para demonstração curta + tem CLI + API + UI + bom material visual).

# 2) Divisão de tarefas entre as 5 pessoas

## Pessoa 1 – Motivação Slides iniciais 

Explicar problemas que séries temporais resolvem:

alta taxa de escrita

compressão

consultas por janelas

retenção e TTL

dados ordenados por tempo

Gravar o video


## Pessoa 2 – Modelo de Dados (InfluxDB)

Explicar o modelo:

Measurement

Tags

Fields

Timestamp

Explicar estrutura em disco (TSM + WAL) de forma simples.


## Pessoa 3 – Fit Map (melhores locais + onde evitar)

Preencher a tabela Ótimo / Bom / Aceitável / Ruim.

Incluir anti-padrões, por exemplo:

JOINs complexos → ruim

leituras ad-hoc não temporais → ruim

alta cardinalidade extrema nas tags → ruim

dashboards, métricas e logs → ótimo

## Pessoa 4 – Demonstração prática
## Luan

Criar um mini-cenário: “monitoramento de sensores IoT” ou “métricas de servidores”.

Preparar:

docker-compose para rodar InfluxDB

script de inserção (curl ou Python)

consultas Flux/InfluxQL

índice = tags (justificar)


## Pessoa 5 – Otimização, tuning + conclusão e referências

Falar sobre:

retenção (Retention Policies)

shard duration

compressão TSM

cache de tags

métricas de monitoramento

Fazer as conclusões e juntar links da documentação.

