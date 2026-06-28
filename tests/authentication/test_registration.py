import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(
        self, dashboard_page: DashboardPage, registration_page: RegistrationPage
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        registration_page.registration_form.fill(
            email="user.name@gmail.com", username="username", password="password"
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()

    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
        )
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(
            email="", username="", password=""
        )
