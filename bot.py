
import requests
import os

def visitar():
    url = "https://www.booking.com/hotel/es/marina-d-or-asequible-apartamento.es.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    try:
        res = requests.get(url, headers=headers, timeout=20)
        print(f"Visita OK. Status: {res.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    visitar()
