from playwright.sync_api import Page


class ThankYouPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.order_summary_locator = page.locator('[data-cy="order-summary"]')
