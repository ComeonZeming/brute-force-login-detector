# 🔐 BruteForce Login Attempt Detector

This is a simple Python-based tool that simulates brute-force login detection by scanning user login logs for suspicious repeated failures from the same IP address.

---

## 📌 Features

- Detects brute-force behavior based on failed login thresholds
- Parses structured CSV log data
- Highlights suspicious IP addresses
- Easily customizable threshold and log format

---

## 🧪 Sample Output

- [ALERT] Possible brute-force attack detected from IP: 192.168.1.10

  
---

## 🗂 Log Format (CSV)

```csv
timestamp,username,ip_address,status
2025-06-20 10:01:00,john,192.168.1.10,FAIL
2025-06-20 10:01:05,john,192.168.1.10,FAIL
...
