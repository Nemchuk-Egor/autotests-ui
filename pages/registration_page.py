from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("registration-form-email-input").locator(
            "input"
        )
        self.password_input = page.get_by_test_id(
            "registration-form-password-input"
        ).locator("input")
        self.username_input = page.get_by_test_id(
            "registration-form-username-input"
        ).locator("input")
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

    def fill_registration_form(self, email: str, username: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.username_input).to_be_visible()

        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_link(self):
        self.login_link.click()

    def click_registration_button(self):
        expect(self.registration_button).to_be_visible()
        self.registration_button.click()

    def check_visible_user_again_exists_alert(self):
        expect(self.user_again_exists_alert).to_be_visible()
        expect(self.user_again_exists_alert).to_have_text("User already exists")
