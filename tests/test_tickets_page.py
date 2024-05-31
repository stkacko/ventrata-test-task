from playwright.sync_api import expect, sync_playwright

from pages.checkout_modal import CheckoutModal
from pages.landing_page import LandingPage
from pages.tickets_page import TicketsPage


def test_tickets_page():
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
        expect(checkout_modal.title_locator).to_have_text("Tickets")

        tickets_page = TicketsPage(page)

        # Assert that the 'PerBooking' element exist
        expect(tickets_page.extras_per_booking_locator).to_be_visible()

        # Assert that the 'extras-PerTicket' element is not visible before clicking the increase button
        expect(tickets_page.extras_per_ticket_locator).not_to_be_visible()

        tickets_page.click_increase_button(1)

        # Assert that the count is "1"
        expect(tickets_page.count_locator).to_have_text("1")

        # Assert that the 'PerTicket' element exists
        expect(tickets_page.extras_per_ticket_locator).to_be_visible()

        tickets_page.click_increase_button(1)

        # Assert that the count is "2"
        expect(tickets_page.count_locator).to_have_text("2")

        browser.close()
