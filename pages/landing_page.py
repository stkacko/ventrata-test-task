from playwright.sync_api import Page


class LandingPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click_product_button(self, product_id: str) -> None:
        self.page.click(f"[data-config*='{product_id}']")

    def navigate_and_select_product(self, url: str, product_id: str) -> None:
        self.navigate(url)
        self.click_product_button(product_id)
