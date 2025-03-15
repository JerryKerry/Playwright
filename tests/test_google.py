import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def browser_page(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()

def test_google_search(browser_page:Page):
    browser_page.goto("https://www.google.com")
    search_box = browser_page.locator("textarea[title='Поиск']")
    search_box.fill("Playwright Python")
    search_box.press("Enter")

    browser_page.wait_for_load_state("domcontentloaded")
    assert "Playwright" in browser_page.title()
    print("✅ Тест успешно пройден!")
