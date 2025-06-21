import csv
from collections import defaultdict
import os

THRESHOLD = 5
failures_by_ip = defaultdict(int)

log_path = os.path.join("..", "logs", "sample_login_logs.csv")

print(f"Reading from: {log_path}")

try:
    with open(log_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Log Entry: {row}")
            if row['status'] == 'FAIL':
                ip = row['ip_address']
                failures_by_ip[ip] += 1
                if failures_by_ip[ip] == THRESHOLD:
                    print(f"[ALERT] Possible brute-force attack detected from IP: {ip}")
except FileNotFoundError:
    print(f"[ERROR] Log file not found at: {log_path}")
