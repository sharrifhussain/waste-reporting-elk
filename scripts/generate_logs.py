import random
import time
from datetime import datetime

methods = ["GET", "POST", "PUT", "DELETE"]

endpoints = [
    "/api/reports",
    "/api/report",
    "/api/reports/101",
    "/api/login",
    "/api/users",
    "/api/collection-status"
]

statuses = [200, 201, 400, 401, 404, 500]

while True:
    timestamp = datetime.now().isoformat(timespec="seconds")
    ip = f"192.168.1.{random.randint(10, 50)}"
    method = random.choice(methods)
    endpoint = random.choice(endpoints)
    status = random.choice(statuses)
    response_time = random.randint(20, 500)

    log = f"{timestamp} {ip} {method} {endpoint} {status} {response_time}"

    print(log)

    with open("logs/waste-app.log", "a") as file:
        file.write(log + "\n")

    time.sleep(2)
