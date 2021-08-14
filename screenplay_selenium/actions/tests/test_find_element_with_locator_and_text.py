import pytest
from screenplay_selenium.actions import navigate_to, find_element_with_locator_and_text, set_find_timeout_to
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_finding_an_element_by_locator_and_text(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element_with_locator_and_text((By.CSS_SELECTOR, '#list li'), 'fourth_li').and_store_as('fourth')
    )

    assert returned_value.text == 'fourth_li'

    stored_value = user.state['fourth'].value

    assert stored_value.text == 'fourth_li'


def test_finding_an_element_by_locator_and_text_without_storing_it(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element_with_locator_and_text((By.CSS_SELECTOR, '#list li'), 'fourth_li')
    )

    assert returned_value.text == 'fourth_li'


@pytest.mark.slow
def test_trying_to_find_an_element_that_does_not_exist(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        set_find_timeout_to(2).seconds_and_then(
            find_element_with_locator_and_text((By.CSS_SELECTOR, '#does_not_exist'), 'fourth_li').and_store_as('fourth')
        )
    )

    assert returned_value is None

    stored_value = user.state['fourth'].value

    assert stored_value is None
