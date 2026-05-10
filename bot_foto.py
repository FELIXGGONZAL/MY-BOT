import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Lanzamos el navegador (Chrome)
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # --- AQUÍ PEGA TU URL ENTRE LAS COMILLAS ---
        url = "https://www.booking.com/hotel/es/tu-apartamento-aqui.html" 
        # -------------------------------------------

        print(f"Abriendo: {url}")
        
        # Entramos en la web
        await page.goto(url, wait_until="networkidle")
        
        # Esperamos 5 segundos extra para que carguen fotos y precios
        await asyncio.sleep(5) 
        
        # Sacamos la foto de toda la página
        await page.screenshot(path="captura.png", full_page=True)
        print("¡Foto sacada con éxito! Status: 200")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
