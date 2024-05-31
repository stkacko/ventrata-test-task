from playwright.sync_api import Page


class TravelDatesPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.calendar_date_active_locator = page.locator(
            '[data-cy="calendar-date-active"]'
        )
        self.date_and_time_locator = page.get_by_role(
            "button", name="Select date & time"
        )
        self.notices_continue_button_locator = page.get_by_role(
            "button", name="Ok, got it"
        )
        self.save_button_locator = page.get_by_role("button", name="Save")
        self.select_time_locator = page.get_by_role("heading", name="Select time")
        self.selected_counter_locator = page.locator('[data-cy="selected-counter"]')
        self.time_label_locator = page.get_by_text(":57 PM")

    def click_date_and_time_button(self) -> None:
        self.date_and_time_locator.first.click()

    def click_save_button(self) -> None:
        self.save_button_locator.click()

    def select_time(self) -> None:
        self.time_label_locator.click()

    def click_notices_continue_button(self) -> None:
        self.notices_continue_button_locator.click()
