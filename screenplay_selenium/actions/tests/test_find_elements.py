from screenplay_selenium.actions import navigate_to, find_elements, find_element_with_locator_and_text
from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_finding_element_with_a_filter(user):
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
