# Projeto – Banco de Dados de Séries Temporais com InfluxDB (Time-Series)

Demonstração prática para o trabalho da disciplina **Armazenamento de Dados e Otimização IA/CD 2025/2**.
O cenário simulado é um sistema de **monitoramento IoT**, com três sensores enviando leituras contínuas ao InfluxDB.

---

## 📌 1. Requisitos

### Sistema

* Docker e Docker Compose instalados
* Python 3.9+
* Navegador web (para acessar o InfluxDB)

---

## 📌 2. Arquivos do Projeto

| Arquivo                     | Descrição                                          |
| --------------------------- | -------------------------------------------------- |
| `docker-compose.yml`        | Sobe o InfluxDB já configurado automaticamente     |
| `insert_loop.py`            | Envia dados contínuos de 3 sensores                |
| `README.md`                 | Documentação do projeto                            |
| `consultas.flux` (opcional) | Apenas as 3 primeiras consultas utilizadas na demo |

---

## 📌 3. Subir o InfluxDB

Na pasta do projeto, execute:

```bash
docker-compose up -d
```

Acesse no navegador:

👉 **[http://localhost:8086](http://localhost:8086)**

Credenciais geradas automaticamente:

* **User:** admin
* **Password:** admin123
* **Organization:** demo_org
* **Bucket:** iot_raw

Para parar:

```bash
docker-compose down
```

Para resetar tudo (inclusive volumes):

```bash
docker-compose down -v
```

---

## 📌 4. Gerar dados contínuos (loop de sensores)

O script envia **1 leitura/segundo** para **3 sensores (S1, S2, S3)**.

Execute:

```bash
python insert_loop.py
```

Para parar:

```
CTRL + C
```

---

## 📌 5. Reproduzir as Consultas (Flux)

Acesse:

**Data → Explore → Script Editor**

Cole as consultas abaixo.

---

### ✔️ Consulta 1 – Dados dos últimos 15 minutos

```flux
from(bucket: "iot_raw")
  |> range(start: -15m)
```

---

### ✔️ Consulta 2 – Filtrar por um sensor (usa TAG / INDEX)

```flux
from(bucket: "iot_raw")
  |> range(start: -1h)
  |> filter(fn: (r) => r.sensor_id == "S1")
```

---

### ✔️ Consulta 3 – Apenas o campo temperatura

```flux
from(bucket: "iot_raw")
  |> range(start: -1h)
  |> filter(fn: (r) => r._field == "temperature")
```

---

## 📌 6. Como limpar ou resetar os dados

### Método mais simples (interface web)

1. Menu → **Buckets**
2. Escolha `iot_raw`
3. Clique em ⋮ → **Delete Data**
4. Selecione **All Time**

### Para resetar tudo pelo Docker

```bash
docker-compose down -v
docker-compose up -d
```

---

## 📌 7. Notas importantes sobre modelagem (Índices)

* **Tags = índices automáticos no InfluxDB**
* Tags usadas: `sensor_id`, `location`, `status`
* **Fields não são indexados**
* Fields usados: temperatura, umidade, co₂, bateria

Isso melhora filtros e agrupamentos em consultas temporais.

---

## 📚 Referências Oficiais

* [https://docs.influxdata.com](https://docs.influxdata.com)
* [https://github.com/influxdata/influxdb](https://github.com/influxdata/influxdb)

---
