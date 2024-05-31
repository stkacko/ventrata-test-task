from playwright.sync_api import Page


class PaymentPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.card_number_locator = page.frame_locator(
            'iframe[title="Iframe for card number"]'
        ).get_by_placeholder("5678 9012 3456")
        self.expiry_date_locator = page.frame_locator(
            'iframe[title="Iframe for expiry date"]'
        ).get_by_placeholder("MM/YY")
        self.holder_name_locator = page.get_by_placeholder("J. Smith")
        self.pay_button_locator = page.get_by_role("button", name="Pay €")
        self.security_code_locator = page.frame_locator(
            'iframe[title="Iframe for security code"]'
        ).get_by_placeholder("digits")

    def fill_card_number(self, card_number: str) -> None:
        self.card_number_locator.fill(card_number)

    def fill_expiry_date(self, expiry_date: str) -> None:
        self.expiry_date_locator.fill(expiry_date)

    def fill_security_code(self, security_code: str) -> None:
        self.security_code_locator.fill(security_code)

    def fill_holder_name(self, holder_name: str) -> None:
        self.holder_name_locator.fill(holder_name)

    def click_pay_button(self) -> None:
        self.pay_button_locator.click()

    def fill_payment_form(
        self, card_number: str, expiry_date: str, security_code: str, holder_name: str
    ) -> None:
        self.fill_card_number(card_number)
        self.fill_expiry_date(expiry_date)
        self.fill_security_code(security_code)
        self.fill_holder_name(holder_name)
        self.click_pay_button()
