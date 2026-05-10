import asyncio
from playwright.async_api import async_playwright

async def entrar_y_salir():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        url = "https://www.booking.com/hotel/es/marina-d-or-asequible-apartamento.es.html"
        
        # Hace 6 entradas rápidas
        for i in range(6):
            try:
                print(f"Visita {i+1}: Entrando...")
                await page.goto(url, wait_until="commit", timeout=30000)
                await asyncio.sleep(10) # Aquí están tus 10 segundos
            except Exception as e:
                print(f"Error: {e}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(entrar_y_salir())
