from playwright.sync_api import Page

from constants import OUTPUT_SCREENSHOT_FOLDER, SITE_URL


def test_counters_display_with_header(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-wrapper-OutiE").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}1.png")


def test_header(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-title-vTYAX").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}2.png")


def test_auth_description(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-description-lPXN_").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}3.png")


def test_auth_button(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-button-wrapper-K8ki0").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}4.png")


def test_water_counter(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-impact-item-eeQO3 >> nth=3").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}5.png")


def test_c02_counter(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-impact-item-eeQO3 >> nth=1").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}6.png")


def test_electricity_counter(page: Page):
    page.goto(SITE_URL)
    page.locator(".desktop-impact-item-eeQO3 >> nth=5").screenshot(path=f"{OUTPUT_SCREENSHOT_FOLDER}7.png")
