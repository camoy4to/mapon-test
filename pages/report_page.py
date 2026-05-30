from playwright.sync_api import Page


class ReportPage:
    def __init__(self, page: Page):
        self.page = page

        self.reports_link = page.get_by_role("link", name="📋 Create Report")

        self.report_type = page.locator("#reportType")
        self.vehicles = page.locator("#reportVehicles")

        self.date_from = page.locator("#dateFrom")
        self.date_to = page.locator("#dateTo")

        self.generate_button = page.locator("#generateBtn")

        self.error_message = page.locator("#formError")

        self.success_card = page.locator("#successCard")
        self.success_title = page.get_by_role(
            "heading",
            name="Report Generated"
        )
        self.error_message = page.locator("#formError")

    def open(self):
        self.reports_link.click()

    def select_report_type(self, value: str):
        self.report_type.select_option(value=value)

    def select_vehicle(self, vehicle_id: str):
        self.vehicles.select_option(value=vehicle_id)

    def set_date_from(self, value: str):
        self.date_from.fill(value)

    def set_date_to(self, value: str):
        self.date_to.fill(value)

    def generate_report(self):
        self.generate_button.click()

    def report_was_generated(self):
        self.success_title.wait_for(state="visible")
        return self.success_title.is_visible()

    def get_error_message(self):
        return self.error_message.inner_text()