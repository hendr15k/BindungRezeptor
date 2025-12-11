from playwright.sync_api import sync_playwright
import os

def verify_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html file directly
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Click the "Vorhersagen" button
        page.click("button:text('Vorhersagen')")

        # Wait for the results to appear (waiting for the table rows)
        # This confirms that either prediction or fallback worked
        page.wait_for_selector("#results-body tr")

        # Wait for properties to appear
        page.wait_for_selector("#properties-container")

        # Take a full page screenshot
        page.screenshot(path="verification/verification_full.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_app()
