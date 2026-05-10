import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            locale="es-ES"
        )
        page = await context.new_page()
        
        url = "https://www.booking.com/hotel/es/marina-d-or-asequible-apartamento.es.html"
        
        print(f"Abriendo: {url}")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        await asyncio.sleep(7)
        
        print("--- BUSCANDO INFO DE VISITAS ---")
        
        try:
            # Buscamos si hay gente mirando
            visitas = await page.get_by_text("están mirando").all_text_contents()
            # Buscamos si se ha reservado mucho
            reservas = await page.get_by_text("veces reservado").all_text_contents()
            
            if visitas:
                print(f"POPULARIDAD: {visitas[0]}")
            if reservas:
                print(f"RESERVAS RECIENTES: {reservas[0]}")
            if not visitas and not reservas:
                print("No hay carteles de visitas activos ahora mismo.")
                
        except Exception as e:
            print(f"No se pudo leer la info: {e}")

        await page.screenshot(path="captura_espia.png", full_page=True)
        print("--- PROCESO COMPLETADO ---")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
