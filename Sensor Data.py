import requests
import time
import random
url = "https://ngrkeuhmpqurckehhdkw.supabase.co/rest/v1/data_sensor"
anon_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5ncmtldWhtcHF1cmNrZWhoZGt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIxOTYyNjIsImV4cCI6MjA5Nzc3MjI2Mn0.Y8Kbp8UzLFjx3mDHCtKmEz5lTZnLZtNc4-B8VJnVWUI"
headers = {
    "apikey": anon_key,
    "Authorization": f"Bearer {anon_key}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}
print("Memulai simulasi pengiriman data HTTPS ke Supabase...")

while True:
    # Berpura-pura mengambil data acak dari sensor DHT22
    kelembapan_simulasi = random.randint(35, 55)
    data = {"kelembapan": kelembapan_simulasi}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Data Terkirim! Kelembapan: {kelembapan_simulasi}% | HTTP Status: {response.status_code}")
    except Exception as e:
        print(f"Eror: {e}")    
    time.sleep(10) 