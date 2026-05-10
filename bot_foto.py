import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Configuración para que salga en ESPAÑOL y EUROS
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            locale="es-ES",
            timezone_id="Europe/Madrid"
        )
        page = await context.new_page()
        url = "https://www.booking.com/hotel/es/marina-d-or-asequible-apartamento.es.html"
        
        print(f"Capturando imagen en: {url}")
        try:
            await page.goto(url, wait_until="networkidle", timeout=60000)
            # Esperamos un poco para que carguen bien las fotos y precios
            await asyncio.sleep(5)
            
            # Sacamos la foto de pantalla completa
            await page.screenshot(path="captura_final.png", full_page=True)
            print("¡Foto guardada con éxito!")
            
        except Exception as e:
            print(f"Error al sacar la foto: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
