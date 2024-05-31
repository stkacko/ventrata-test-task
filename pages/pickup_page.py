from playwright.sync_api import Page


class PickupSelectionPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.pickup_name_locator = page.locator('[data-cy="pickup-name"]')
        self.pickup_option_locator = page.get_by_role("option", name="Pick up - 1")
        self.pickup_select_locator = page.locator('[data-cy="select-wrapper"]')
        self.selected_pickup_time_locator = page.locator(
            '[data-cy="selected-pickup-time"]'
        )

    def select_pickup_option(self) -> None:
        self.pickup_select_locator.click()
        self.pickup_option_locator.click()
