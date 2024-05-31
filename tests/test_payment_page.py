from playwright.sync_api import expect

from pages.contact_details_page import ContactDetailsPage
from pages.payment_page import PaymentPage
from pages.pickup_page import PickupSelectionPage
from pages.thank_you_page import ThankYouPage
from pages.tickets_page import TicketsPage
from pages.travel_dates_page import TravelDatesPage
from utils.helpers import navigate_to_landing_page_and_open_checkout
from config import CARD_NUMBER, CARD_EXPIRY, CARD_CVC, CARD_HOLDER


def test_pickup_selection_page(page):
    checkout_modal = navigate_to_landing_page_and_open_checkout(page)

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

    contact_details_page = ContactDetailsPage(page)

    contact_details_page.fill_out_contact_details("John", "Doe", "john.doe@gmail.com")

    checkout_modal.click_footer_button()

    # Assert that the checkout modal has the correct title
    expect(checkout_modal.title_locator).to_have_text("Payment", timeout=15000)

    payment_page = PaymentPage(page)

    # Assert that the pay button has the correct value
    expect(payment_page.pay_button_locator).to_have_text("Pay €5.00")

    payment_page.fill_payment_form(CARD_NUMBER, CARD_EXPIRY, CARD_CVC, CARD_HOLDER)

    thank_you_page = ThankYouPage(page)
    thank_you_page.order_summary_locator.wait_for(state="visible")

    # Assert that the order summary is visible on the "thank you" page
    expect(thank_you_page.order_summary_locator).to_be_visible()
