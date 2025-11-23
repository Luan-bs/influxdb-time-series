from(bucket: "iot_raw")
  |> range(start: -1h)
  |> filter(fn: (r) => r._field == "temperature")