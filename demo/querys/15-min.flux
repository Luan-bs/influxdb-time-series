```flux
from(bucket: "iot_raw")
  |> range(start: -15m)