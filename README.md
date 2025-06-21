# BruteForce Login Attempt Detector

This Python tool simulates log monitoring to detect brute-force login attempts based on failed logins from the same IP address.

## 🔧 Features
- Counts failed login attempts per IP
- Flags suspicious IPs after configurable threshold
- Can be extended to include timestamps, alerts, or log parsing from real files

## 🗂 Log Format
```csv
timestamp,username,ip_address,status
 
