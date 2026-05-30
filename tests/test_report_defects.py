import pytest


@pytest.mark.defect
def test_report_generation_should_be_blocked_for_invalid_date_range(
    logged_in_page,
    report_page
):
    report_page.open()

    report_page.select_report_type("daily")
    report_page.select_vehicle("1")

    report_page.set_date_from("2026-05-30")
    report_page.set_date_to("2026-05-01")

    report_page.generate_report()

    assert not report_page.report_was_generated(), (
        "Report was generated even though Date From is later than Date To"
    )