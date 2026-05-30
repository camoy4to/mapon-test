from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.get_by_role("heading", name="Fleet Overview")
        self.vehicles_section = page.get_by_role("heading", name="Vehicles")
        self.search_input = page.get_by_placeholder("Search by plate, name, or driver...")
        self.status_filter = page.locator("select").first
        self.vehicles_table = page.locator("tbody")
        self.next_button = page.get_by_role("button", name="Next →")

    def is_opened(self):
        return self.page_title.is_visible() and self.vehicles_section.is_visible()

    def open_vehicle_by_name(self, vehicle_name: str):
        self.vehicles_table.get_by_text(vehicle_name, exact=True).click()

    def filter_by_status(self, status: str):
        self.status_filter.select_option(label=status)

    def vehicle_is_visible(self, vehicle_name: str):
        return self.vehicles_table.get_by_text(vehicle_name, exact=True).is_visible()

    def go_to_next_page(self):
        self.next_button.click()

    def vehicle_is_not_visible(self, vehicle_name: str):
        return self.vehicles_table.get_by_text(vehicle_name, exact=True).count() == 0

    def get_visible_statuses(self):
        return self.vehicles_table.locator("td:nth-child(4)").all_inner_texts()