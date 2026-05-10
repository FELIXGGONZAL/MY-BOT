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
        
        for i in range(3): # Hace 3 comprobaciones por cada vez que arranca
            try:
                print(f"--- COMPROBACIÓN {i+1} ---")
                await page.goto(url, wait_until="networkidle", timeout=60000)
                await asyncio.sleep(5)
                
                visitas = await page.get_by_text("están mirando").all_text_contents()
                if visitas:
                    print(f"POPULARIDAD ACTUAL: {visitas[0]}")
                else:
                    print("Sin datos de visitas en este momento.")
                
                # Esperamos 50 segundos para la siguiente vuelta
                if i < 2: 
                    print("Esperando para la siguiente comprobación...")
                    await asyncio.sleep(50)
                    
            except Exception as e:
                print(f"Error: {e}")

        await page.screenshot(path="captura_espia.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
