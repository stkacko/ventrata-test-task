from playwright.sync_api import expect, sync_playwright

from pages.checkout_modal import CheckoutModal
from pages.contact_details_page import ContactDetailsPage
from pages.landing_page import LandingPage
from pages.pickup_page import PickupSelectionPage
from pages.tickets_page import TicketsPage
from pages.travel_dates_page import TravelDatesPage


def test_pickup_selection_page():
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

        tickets_page = TicketsPage(page)
        tickets_page.click_increase_button(2)

        checkout_modal.click_footer_button()

        travel_dates_page = TravelDatesPage(page)
        travel_dates_page.click_date_and_time_button()
        travel_dates_page.click_save_button()
        travel_dates_page.click_date_and_time_button()
        travel_dates_page.select_time_locator.wait_for(state="visible")
        travel_dates_page.select_time()
        travel_dates_page.click_save_button()
        travel_dates_page.click_notices_continue_button()
        travel_dates_page.click_date_and_time_button()
        travel_dates_page.click_save_button()

        checkout_modal.click_footer_button()
        pickup_selection_page = PickupSelectionPage(page)
        pickup_selection_page.select_pickup_option()

        checkout_modal.click_footer_button()

        # Assert that the checkout modal has the correct title
        expect(checkout_modal.title_locator).to_have_text("Checkout")

        contact_details_page = ContactDetailsPage(page)

        contact_details_page.fill_out_contact_details(
            "John", "Doe", "john.doe@gmail.com"
        )

        # Assert that the promo code button is visible and the total due is correct
        expect(contact_details_page.promo_code_open_button_locator).to_be_visible()
        expect(contact_details_page.total_due_locator).to_have_text("€5.00")

        checkout_modal.click_footer_button()
