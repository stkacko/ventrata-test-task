from playwright.sync_api import expect, sync_playwright

from pages.checkout_modal import CheckoutModal
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

        # Assert that the checkout modal has the correct title
        expect(checkout_modal.title_locator).to_have_text("Select Pickup")

        pickup_selection_page = PickupSelectionPage(page)
        pickup_selection_page.select_pickup_option()

        # Assert that the time of pickup and the pickup name are correct
        expect(pickup_selection_page.selected_pickup_time_locator).to_have_text(
            "We will pick you up between 9:00 AM to 10:00 AM from"
        )
        expect(pickup_selection_page.pickup_name_locator).to_have_text("Pick up - 1")
