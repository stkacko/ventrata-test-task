from playwright.sync_api import expect, sync_playwright

from pages.checkout_modal import CheckoutModal
from pages.landing_page import LandingPage


def test_checkout_modal():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        landing_page = LandingPage(page)
        landing_page.navigate_and_select_product(
            "https://checkout-supplier-preview-page.pages.dev/task_3",
            "51b3fb8a-af79-49b0-b7ec-252be1c56b2b",
        )

        checkout_modal = CheckoutModal(page)
        checkout_modal.wait_for_checkout_modal()

        # Assert that the checkout modal is visible
        expect(checkout_modal.checkout_modal_locator).to_be_visible()

        browser.close()
