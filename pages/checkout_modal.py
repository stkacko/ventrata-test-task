from playwright.sync_api import Page


class CheckoutModal:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_modal_locator = page.locator('[data-cy="checkout-modal"]')
        self.footer_button_locator = page.locator('[data-cy="footer-button"]')
        self.title_locator = page.locator('[data-cy="title"]')

    def wait_for_checkout_modal(self) -> None:
        self.checkout_modal_locator.wait_for(state="visible")

    def click_footer_button(self) -> None:
        self.footer_button_locator.click()


class IncludedProductBox:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.booking_extras_locator = page.locator("#additional-section").get_by_text(
            "× PerBooking"
        )
        self.booking_product_title = page.locator('[data-cy="booking-product-title"]')
        self.booking_unit_locator = page.locator("#additional-section").get_by_text(
            "× Adult"
        )
        self.notices_locator = page.locator('[data-cy="notices"]').nth(0)
        self.product_5_locator = page.locator("#additional-section").get_by_text(
            "Product 5 - Questions"
        )
        self.product_9_locator = page.locator("#additional-section").get_by_text(
            "Product 9 - Timeslot Notices"
        )
        self.product_box_locator = page.locator('[data-cy="included-product-box"]')
        self.ticket_extras_locator = page.locator("#additional-section").get_by_text(
            "× PerTicket"
        )
