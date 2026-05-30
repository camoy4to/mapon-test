from fixtures.vehicles import VEHICLES
import pytest

@pytest.mark.smoke
def test_user_can_filter_vehicles_by_status(
    logged_in_page,
    dashboard_page
):
    offline_vehicle = VEHICLES["sprinter_3"]
    moving_vehicle = VEHICLES["sprinter_1"]

    dashboard_page.filter_by_status(offline_vehicle["status"])

    assert dashboard_page.vehicle_is_visible(offline_vehicle["name"])
    assert dashboard_page.vehicle_is_not_visible(moving_vehicle["name"])

    visible_statuses = dashboard_page.get_visible_statuses()
    assert visible_statuses
    assert all(status == offline_vehicle["status"] for status in visible_statuses)