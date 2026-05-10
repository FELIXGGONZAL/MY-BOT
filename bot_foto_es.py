name: Bot_Fotografo_Espanol_5min

on:
  workflow_dispatch: # Botón manual
  schedule:
    - cron: "*/5 * * * *"  # <--- ORDEN DE CADA 5 MINUTOS

jobs:
  captura_es:
    runs-on: ubuntu-latest
    steps:
      - name: Descargar codigo
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Instalar Playwright y Navegador
        run: |
          pip install playwright
          playwright install chromium

      - name: Ejecutar Bot Foto Español
        # Asegúrate de que el archivo .py se llame exactamente bot_foto_es.py
        run: python bot_foto_es.py 

      - name: Guardar la captura
        uses: actions/upload-artifact@v4
        with:
          name: captura-espanol-5min
          path: captura_espanol.png
