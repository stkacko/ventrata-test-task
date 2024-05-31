from playwright.sync_api import expect

from utils.helpers import navigate_to_landing_page_and_open_checkout


def test_checkout_modal(page):
    checkout_modal = navigate_to_landing_page_and_open_checkout(page)
    expect(checkout_modal.checkout_modal_locator).to_be_visible()
