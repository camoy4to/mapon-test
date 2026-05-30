import pytest
from utils.config import BASE_URL
from pages.login_page import LoginPage
from fixtures.users import VALID_USER
from pages.dashboard_page import DashboardPage
from pages.vehicle_page import VehiclePage
from pages.report_page import ReportPage
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def login_page(page, base_url):
    return LoginPage(page, base_url)

@pytest.fixture
def logged_in_page(page, base_url):
    login_page_object = LoginPage(page, base_url)

    login_page_object.open()
    login_page_object.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    yield page

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def vehicle_page(page):
    return VehiclePage(page)

@pytest.fixture
def report_page(page):
    return ReportPage(page)