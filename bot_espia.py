¡Entendido! Olvida el PDF, aquí tienes el código limpio y listo para copiar y pegar directamente en GitHub.

1. El "Cerebro" (Archivo: bot_espia.py)
Crea este archivo en la carpeta principal. He ajustado el código para que sea más "agresivo" buscando esos datos de visitas.

Python
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Forzamos español para que los carteles salgan en nuestro idioma
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            locale="es-ES"
        )
        page = await context.new_page()
        
        url = "https://www.booking.com/hotel/es/marina-d-or-asequible-apartamento.es.html"
        
        print(f"Abriendo: {url}")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Esperamos un poco para que salten los cartelitos de Booking
        await asyncio.sleep(7)
        
        print("--- BUSCANDO INFO DE VISITAS ---")
        
        # Buscamos diferentes tipos de mensajes de popularidad
        try:
            # Opción 1: Cartel de "X personas están mirando"
            visitas = await page.get_by_text("están mirando").all_text_contents()
            # Opción 2: Cartel de "reservado X veces"
            reservas = await page.get_by_text("veces reservado").all_text_contents()
            
            if visitas:
                print(f"POPULARIDAD: {visitas[0]}")
            if reservas:
                print(f"RESERVAS RECIENTES: {reservas[0]}")
            if not visitas and not reservas:
                print("No hay carteles de visitas activos ahora mismo.")
                
        except Exception as e:
            print(f"No se pudo leer la info: {e}")

        # Sacamos la foto para confirmar
        await page.screenshot(path="captura_espia.png", full_page=True)
        print("--- PROCESO COMPLETADO ---")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
