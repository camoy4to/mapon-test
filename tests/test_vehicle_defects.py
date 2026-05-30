import pytest
from fixtures.vehicles import VEHICLES


@pytest.mark.defect
def test_driver_should_not_be_removed_without_confirmation(
    logged_in_page,
    dashboard_page,
    vehicle_page
):
    vehicle = VEHICLES["sprinter_1"]

    dashboard_page.open_vehicle_by_name(vehicle["name"])

    initial_driver = vehicle_page.get_assigned_driver()

    vehicle_page.open_change_driver_modal()
    vehicle_page.clear_driver_name()
    vehicle_page.save_driver()

    assert vehicle_page.get_assigned_driver() == initial_driver, (
        "Driver was removed without confirmation"
    )