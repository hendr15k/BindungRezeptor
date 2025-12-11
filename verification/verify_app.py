from playwright.sync_api import sync_playwright

def verify_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local server
        page.goto("http://localhost:8080/")

        # Check title
        print(f"Page title: {page.title()}")

        # Take initial screenshot
        page.screenshot(path="verification/initial_load.png")

        # Input SMILES
        # Aspirin
        smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
        page.fill("#smilesInput", smiles)

        # Click Predict
        page.click("button[onclick='predictTargets()']")

        # Wait for results (might take time to fetch pubchem)
        # We can wait for the table rows to appear
        try:
            page.wait_for_selector("#results-body tr", timeout=10000)
            print("Results appeared.")
        except:
            print("Timeout waiting for results.")

        # Take result screenshot
        page.screenshot(path="verification/verification.png")

        browser.close()

if __name__ == "__main__":
    verify_app()
