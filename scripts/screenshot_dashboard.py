# scripts/screenshot_dashboard.py
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://niloroch.github.io/dashboard-live/"
OUTPUT = Path("assets/dashboard.png")

VIEWPORT = {"width": 1280, "height": 720}  # 16:9
DEVICE_SCALE_FACTOR = 2  # imagem mais nítida (HiDPI)

def run():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=DEVICE_SCALE_FACTOR,
        )
        page = context.new_page()

        # Carrega a página e espera a rede ficar ociosa (JS terminou de puxar recursos)
        page.goto(URL, wait_until="networkidle", timeout=90_000)

        # Aguarda o container principal do seu dashboard (ajuste se quiser outro seletor)
        page.locator(".container").wait_for(timeout=30_000)

        # Dica: se quiser capturar só a área do dashboard:
        # page.locator(".container").screenshot(path=str(OUTPUT))
        # return

        # Screenshot da janela (não full_page pra manter 16:9)
        page.screenshot(path=str(OUTPUT), full_page=False)

        context.close()
        browser.close()

if __name__ == "__main__":
    run()
