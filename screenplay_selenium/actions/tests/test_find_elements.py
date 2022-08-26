from screenplay_selenium.actions import navigate_to, find_elements, find_element_with_locator_and_text
from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_elements_can_be_filtered_after_they_are_found(user):
    found_elements = user.attempts_to(
        navigate_to(test_page),
        find_elements((By.CLASS_NAME, 'filter_parent'))
        .only_elements_where_something_is_found_using(
            find_element_with_locator_and_text((By.CSS_SELECTOR, 'span'), 'First')
        )
    )

    assert len(found_elements) == 1, "Incorrect number of elements found"
    element: WebElement = found_elements[0]
    assert element.get_property('id') == 'filter_target', "Incorrect element filtered"


def test_finding_no_elements_before_applying_the_filter_results_in_None(user):
    found_elements = user.attempts_to(
        navigate_to(test_page),
        find_elements((By.CLASS_NAME, 'does_not_exist'))
        .only_elements_where_something_is_found_using(
            find_element_with_locator_and_text((By.CSS_SELECTOR, 'span'), 'First')
        )
    )

    assert found_elements is None, "Something was returned when it shouldn't have been"


def test_finding_elements_then_filter_them_all_away_results_in_None(user):
    found_elements = user.attempts_to(
        navigate_to(test_page),
        find_elements((By.CLASS_NAME, 'filter_parent'))
        .only_elements_where_something_is_found_using(
            find_element_with_locator_and_text((By.CLASS_NAME, 'does_not_exist'), 'First')
        )
    )

    assert found_elements is None, "Something was returned when it shouldn't have been"
