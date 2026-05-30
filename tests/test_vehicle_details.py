from fixtures.vehicles import VEHICLES
import pytest

@pytest.mark.smoke
def test_user_can_open_vehicle_details_from_dashboard(
        logged_in_page,
        dashboard_page,
        vehicle_page
):
    vehicle = VEHICLES["sprinter_1"]

    assert dashboard_page.is_opened()

    dashboard_page.open_vehicle_by_name(vehicle["name"])

    assert vehicle_page.is_opened_for_vehicle(
        vehicle["name"],
        vehicle["plate"]
    )

    assert vehicle_page.are_tabs_visible()

    vehicle_page.open_trips_tab()
    assert vehicle_page.is_trips_section_visible()

    vehicle_page.open_alerts_tab()
    assert vehicle_page.is_alerts_section_visible()
