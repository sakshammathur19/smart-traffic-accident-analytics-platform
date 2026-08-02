import json
import boto3
import random
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="eu-north-1"
)

# ==========================
# Master Data
# ==========================

roads = [
    "Tonk Road",
    "MI Road",
    "Ajmer Road",
    "C Scheme",
    "Vaishali Nagar"
]

weather_conditions = [
    "Sunny",
    "Rain",
    "Fog",
    "Cloudy"
]

output_folder = "traffic_events"
os.makedirs(output_folder, exist_ok=True)

event_id = 1

# ==========================
# Continuous Traffic Simulator
# ==========================

while True:

    # Accident Probability (10%)
    accident_status = random.choices(
        [True, False],
        weights=[10, 90]
    )[0]

    # Speed Logic
    if accident_status:
        avg_speed = random.randint(5, 18)
    else:
        avg_speed = random.randint(20, 90)

    traffic_event = {
        "event_id": event_id,
        "road_name": random.choice(roads),
        "vehicle_count": random.randint(50, 700),
        "avg_speed": avg_speed,
        "weather": random.choice(weather_conditions),
        "accident_status": accident_status,
        "latitude": round(random.uniform(26.85, 26.95), 4),
        "longitude": round(random.uniform(75.70, 75.85), 4),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # UNIQUE FILE NAME (IMPORTANT)
    unique_file = f"traffic_event_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.json"

    filename = os.path.join(output_folder, unique_file)

    with open(filename, "w") as file:
        json.dump(traffic_event, file, indent=4)

    s3.upload_file(
        filename,
        BUCKET_NAME,
        f"landing/traffic_events/{unique_file}"
    )

    print(f"Generated and Uploaded: {unique_file}")

    event_id += 1

    time.sleep(10)