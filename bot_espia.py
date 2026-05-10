name: Bot_Espia_5min

on:
  workflow_dispatch: # Permite darle al botón manual si quieres
  schedule:
    - cron: "*/5 * * * *"  # <--- EJECUCIÓN AUTOMÁTICA CADA 5 MINUTOS

jobs:
  espionaje:
    runs-on: ubuntu-latest
    steps:
      - name: Descargando archivos
        uses: actions/checkout@v4

      - name: Instalando Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Instalando Navegador y Playwright
        run: |
          pip install playwright
          playwright install chromium

      - name: Ejecutar Bot Espia
        # Asegúrate de que tu archivo de Python se llame exactamente bot_espia.py
        run: python bot_espia.py

      - name: Guardar Captura
        uses: actions/upload-artifact@v4
        with:
          name: reporte-espia-5min
          path: captura_espia.png
