from playwright.sync_api import Page

from config import BASE_URL, PRODUCT_ID
from pages.checkout_modal import CheckoutModal
from pages.landing_page import LandingPage


def navigate_to_landing_page_and_open_checkout(page: Page) -> CheckoutModal:
    landing_page = LandingPage(page)
    landing_page.navigate_and_select_product(BASE_URL, PRODUCT_ID)

    checkout_modal = CheckoutModal(page)
    checkout_modal.checkout_modal_locator.wait_for(state="visible")

    return checkout_modal
