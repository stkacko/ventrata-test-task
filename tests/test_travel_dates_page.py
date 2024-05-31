from playwright.sync_api import expect

from pages.checkout_modal import IncludedProductBox
from pages.tickets_page import TicketsPage
from pages.travel_dates_page import TravelDatesPage
from utils.helpers import navigate_to_landing_page_and_open_checkout


def test_travel_dates_page(page):
    checkout_modal = navigate_to_landing_page_and_open_checkout(page)

    included_product_box = IncludedProductBox(page)

    tickets_page = TicketsPage(page)
    tickets_page.click_increase_button(2)

    checkout_modal.click_footer_button()

    # Assert that the checkout modal has the correct title
    expect(checkout_modal.title_locator).to_have_text("Travel Dates")

    # Assert that all the selected products are visible
    expect(included_product_box.booking_product_title).to_have_text(
        "Product 14 - MDP - VD0"
    )
    expect(included_product_box.booking_unit_locator).to_have_text("2× Adult")
    expect(included_product_box.ticket_extras_locator).to_have_text("2× PerTicket")
    expect(included_product_box.booking_extras_locator).to_have_text("1× PerBooking")

    travel_dates_page = TravelDatesPage(page)

    # Assert that the counter is visible and has the correct value
    expect(travel_dates_page.selected_counter_locator).to_be_visible()
    expect(travel_dates_page.selected_counter_locator).to_have_text("0/3 Selected")

    travel_dates_page.click_date_and_time_button()
    travel_dates_page.click_save_button()

    # Assert that the counter is visible and has the correct value and the selected product is visible
    expect(travel_dates_page.selected_counter_locator).to_have_text("1/3 Selected")
    expect(included_product_box.product_5_locator).to_be_visible()

    travel_dates_page.click_date_and_time_button()
    travel_dates_page.select_time_locator.wait_for(state="visible")
    travel_dates_page.select_time()
    travel_dates_page.click_save_button()
    travel_dates_page.click_notices_continue_button()

    # Assert that the counter has the correct value and the selected product is visible
    expect(travel_dates_page.selected_counter_locator).to_have_text("2/3 Selected")
    expect(included_product_box.product_9_locator).to_be_visible()

    included_product_box.notices_locator.wait_for(state="visible")

    # Assert that the notices are visible
    expect(included_product_box.notices_locator).to_be_visible()

    travel_dates_page.click_date_and_time_button()
    travel_dates_page.click_save_button()

    # Assert that the counter has the correct value
    expect(travel_dates_page.selected_counter_locator).to_have_text("3/3 Selected")
