
import random
import time
import pandas as pd

from datetime import datetime

# Generate sensor measurements
def generate_sensor_data():

    # Normal operating conditions
    temperature = random.uniform(40, 65)
    vibration = random.uniform(1, 4)
    current = random.uniform(5, 10)

    # Simulate abnormal operating conditions
    if random.random() < 0.20:

        anomaly_type = random.choice([
            "high_temperature",
            "high_vibration",
            "high_current"
        ])

        if anomaly_type == "high_temperature":
            temperature = random.uniform(75, 100)

        elif anomaly_type == "high_vibration":
            vibration = random.uniform(7, 12)

        elif anomaly_type == "high_current":
            current = random.uniform(12, 18)

    # Determine machine status
    if temperature > 70 or vibration > 6 or current > 11:
        status = "anomaly"
    else:
        status = "normal"

    data = {
        "timestamp": datetime.now(),
        "temperature": round(temperature, 2),
        "vibration": round(vibration, 2),
        "current": round(current, 2),
        "status": status
    }

    return data


# Main simulation
try:
    while True:

        sensor_data = generate_sensor_data()

        print(sensor_data)

        df = pd.DataFrame([sensor_data])

        df.to_csv(
            "data/raw/sensor_data.csv",
            mode="a",
            header=not pd.io.common.file_exists(
                "data/raw/sensor_data.csv"
            ),
            index=False
        )

        time.sleep(1)

except KeyboardInterrupt:
    print("\nSimulation stopped.")
