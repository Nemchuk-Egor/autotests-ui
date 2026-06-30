from playwright.sync_api import Page

from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)
import re
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.authentication_course_title = Text(
            page, "authentication-ui-course-title-text", "UI Course"
        )
        self.login_link = Link(page, "registration-page-login-link", "Login")
        self.registration_button = Button(
            page, "registration-page-registration-button", "Registration"
        )
        self.user_again_exists_alert = Text(
            page, "registration-page-user-already-exists-alert", "User already exists"
        )

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(r".*/#/auth/login"))

    def click_registration_button(self):
        self.registration_button.check_visible()
        self.registration_button.click()

    def check_visible_user_again_exists_alert(self):
        self.user_again_exists_alert.check_visible()
        self.user_again_exists_alert.check_have_text("User already exists")
