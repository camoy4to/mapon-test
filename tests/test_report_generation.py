import pytest


@pytest.mark.smoke
def test_user_can_generate_report(
    logged_in_page,
    report_page
):
    report_page.open()

    report_page.select_report_type("daily")
    report_page.select_vehicle("1")

    report_page.generate_report()

    assert report_page.report_was_generated()