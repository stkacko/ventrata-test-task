from playwright.sync_api import Page


class ContactDetailsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_address_locator = page.locator('[data-cy="emailAddress-input"]')
        self.first_name_locator = page.locator('[data-cy="firstName-input"]')
        self.last_name_locator = page.locator('[data-cy="lastName-input"]')
        self.promo_code_open_button_locator = page.locator(
            '[data-cy="promo-code-open-button"]'
        )
        self.total_due_locator = page.locator('[data-cy="total-due-value"]')

    def enter_first_name(self, first_name: str) -> None:
        self.first_name_locator.fill(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.last_name_locator.fill(last_name)

    def enter_email_address(self, email_address: str) -> None:
        self.email_address_locator.fill(email_address)

    def fill_out_contact_details(
        self, first_name: str, last_name: str, email_address: str
    ) -> None:
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_address(email_address)
