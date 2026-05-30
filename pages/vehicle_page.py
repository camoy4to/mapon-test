from playwright.sync_api import Page


class VehiclePage:
    def __init__(self, page: Page):
        self.page = page

        self.back_to_fleet_link = page.get_by_text("← Back to fleet")
        self.details_tab = page.get_by_text("Details", exact=True)
        self.trips_tab = page.get_by_text("Trips", exact=True)
        self.alerts_tab = page.get_by_text("Alerts", exact=True)
        self.driver_info = page.locator("#driverInfo")
        self.change_driver_button = page.locator("#editDriverBtn")
        self.driver_name_input = page.locator("#driverName")
        self.save_driver_button = page.locator("#saveDriver")

    def is_opened_for_vehicle(self, vehicle_name: str, plate_number: str):
        return self.page.get_by_role(
            "heading",
            name=f"{vehicle_name} ({plate_number})"
        ).is_visible()

    def are_tabs_visible(self):
        return (
            self.details_tab.is_visible()
            and self.trips_tab.is_visible()
            and self.alerts_tab.is_visible()
        )

    def open_trips_tab(self):
        self.trips_tab.click()

    def open_alerts_tab(self):
        self.alerts_tab.click()

    def is_trips_section_visible(self):
        return self.page.get_by_role("heading", name="Today's Trips").is_visible()

    def is_alerts_section_visible(self):
        return self.page.get_by_role("heading", name="Vehicle Alerts").is_visible()

    def get_assigned_driver(self):
        return self.driver_info.inner_text()

    def open_change_driver_modal(self):
        self.change_driver_button.click()

    def clear_driver_name(self):
        self.driver_name_input.fill("")

    def save_driver(self):
        self.save_driver_button.click()