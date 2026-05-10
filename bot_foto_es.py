import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Lanzamos el navegador
        browser = await p.chromium.launch(headless=True)
        
        # --- BLOQUE DE IDIOMA ESPAÑOL ---
        # Esto evita el error de "Page Not Found" y pone los precios en €
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            locale="es-ES",
            timezone_id="Europe/Madrid"
        )
        page = await context.new_page()
        
        # URL limpia de tu apartamento
        url = "https://www.booking.com/hotel/es/marina-d-or-asequible-apartamento.es.html"
        
        print(f"Abriendo apartamento en: {url}")
        
        try:
            # Entramos y esperamos a que cargue la red
            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # Esperamos 5 segundos para que aparezcan los precios
            await asyncio.sleep(5)
            
            # Sacamos la foto
            await page.screenshot(path="captura_espanol.png", full_page=True)
            print("¡Captura en español realizada!")
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
