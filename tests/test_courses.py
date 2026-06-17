from playwright.sync_api import expect, sync_playwright, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    h6_courses_toolbar_title = chromium_page_with_state.get_by_test_id(
        "courses-list-toolbar-title-text"
    )
    expect(h6_courses_toolbar_title).to_be_visible()
    expect(h6_courses_toolbar_title).to_have_text("Courses")

    icon_courses_empty = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-icon"
    )
    expect(icon_courses_empty).to_be_visible()

    courses_empty_title_text = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-title-text"
    )
    expect(courses_empty_title_text).to_be_visible()
    expect(courses_empty_title_text).to_have_text("There is no results")

    courses_empty_description_text = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    expect(courses_empty_description_text).to_be_visible()
    expect(courses_empty_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )
 
