from pathlib import Path
from playwright.sync_api import sync_playwright
import imageio.v2 as imageio
import time

URL = "https://niloroch.github.io/dashboard-live/"
OUTPUT = Path("assets/dashboard.gif")
TEMP_DIR = Path("assets/frames")
DURATION = 7          # segundos de captura
INTERVAL = 0.3        # intervalo entre frames (s)

VIEWPORT = {"width": 1280, "height": 720}
DEVICE_SCALE_FACTOR = 1.5

def run():
    # Pasta para frames temporários
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=DEVICE_SCALE_FACTOR,
        )
        page = context.new_page()
        page.goto(URL, wait_until="networkidle", timeout=90_000)

        # Espera o dashboard carregar
        page.locator(".container").wait_for(timeout=30_000)

        # Captura frames
        frames = []
        start = time.time()
        i = 0
        while time.time() - start < DURATION:
            filename = TEMP_DIR / f"frame_{i:03}.png"
            page.screenshot(path=str(filename), full_page=False)
            frames.append(imageio.imread(filename))
            i += 1
            time.sleep(INTERVAL)

        browser.close()

    # Monta GIF
    imageio.mimsave(OUTPUT, frames, duration=0.2, loop=0)

    # Limpa frames temporários
    for f in TEMP_DIR.glob("*.png"):
        f.unlink()
    TEMP_DIR.rmdir()

    print(f"GIF salvo em {OUTPUT}")

if __name__ == "__main__":
    run()

