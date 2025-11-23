import requests
import random
import time
from datetime import datetime

# Configurações do InfluxDB
INFLUX_URL = "http://localhost:8086/api/v2/write"
TOKEN = "demo-token"
ORG = "demo_org"
BUCKET = "iot_raw"

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}

# Sensores simulados
sensors = [
    {"id": "S1", "location": "lab"},
    {"id": "S2", "location": "office"},
    {"id": "S3", "location": "warehouse"}
]

print("📡 Enviando dados continuamente para o InfluxDB...")
print("Pressione CTRL + C para parar.\n")

try:
    while True:
        lines = []

        timestamp_ns = int(time.time() * 1e9)

        for s in sensors:
            temperature = round(random.uniform(20, 28), 2)
            humidity = round(random.uniform(40, 65), 1)
            co2 = random.randint(400, 1200)
            battery = round(random.uniform(40, 100), 1)
            status = "ok" if battery > 45 else "low"

            line = (
                f"iot_data,"
                f"sensor_id={s['id']},"
                f"location={s['location']},"
                f"status={status} "
                f"temperature={temperature},"
                f"humidity={humidity},"
                f"co2={co2},"
                f"battery={battery} "
                f"{timestamp_ns}"
            )

            lines.append(line)

        body = "\n".join(lines)

        response = requests.post(
            f"{INFLUX_URL}?org={ORG}&bucket={BUCKET}&precision=ns",
            data=body,
            headers=headers
        )

        if response.status_code != 204:
            print("Erro ao enviar:", response.text)

        # imprime resumo no console
        print(f"{datetime.utcnow()}  ->  dados enviados para 3 sensores")

        time.sleep(1)   # 1 ponto por segundo

except KeyboardInterrupt:
    print("\n🛑 Inserção interrompida pelo usuário.")
