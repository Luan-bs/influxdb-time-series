from(bucket: "iot_raw")
  |> range(start: -1h)
  |> filter(fn: (r) => r.sensor_id == "S1")