from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.authentication_course_title = page.get_by_test_id(
            "authentication-ui-course-title-text"
        )
        self.login_link = page.get_by_test_id("registration-page-login-link")
        self.registration_button = page.get_by_test_id(
            "registration-page-registration-button"
        )
        self.user_again_exists_alert = page.get_by_test_id(
            "registration-page-user-already-exists-alert"
        )

    def click_login_link(self):
        self.login_link.click()

    def click_registration_button(self):
        expect(self.registration_button).to_be_visible()
        self.registration_button.click()

    def check_visible_user_again_exists_alert(self):
        expect(self.user_again_exists_alert).to_be_visible()
        expect(self.user_again_exists_alert).to_have_text("User already exists")
