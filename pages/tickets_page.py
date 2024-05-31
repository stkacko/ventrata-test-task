from playwright.sync_api import Page


class TicketsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.count_locator = page.locator('[data-cy="count"]')
        self.extras_per_booking_locator = page.locator('[data-cy="extras-PerBooking"]')
        self.extras_per_ticket_locator = page.locator('[data-cy="extras-PerTicket"]')
        self.increase_button_locator = page.locator('[data-cy="increase-button"]')

    def click_increase_button(self, times) -> None:
        for _ in range(times):
            self.increase_button_locator.click()
