from fixtures.users import VALID_USER, INVALID_USER
import pytest

@pytest.mark.smoke
def test_user_can_open_login_page_and_login_successfully(login_page, page):
    login_page.open()

    assert login_page.is_opened()

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    assert "dashboard" in page.url.lower()

@pytest.mark.smoke
def test_user_sees_error_message_after_invalid_login(login_page):
    login_page.open()

    login_page.login(
        INVALID_USER["username"],
        INVALID_USER["password"]
    )

    assert login_page.get_error_message() == "Invalid username or password"