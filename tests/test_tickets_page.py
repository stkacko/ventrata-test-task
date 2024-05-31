from playwright.sync_api import expect

from pages.tickets_page import TicketsPage
from utils.helpers import navigate_to_landing_page_and_open_checkout


def test_tickets_page(page):
    checkout_modal = navigate_to_landing_page_and_open_checkout(page)

    # Assert that the checkout modal has the correct title
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
