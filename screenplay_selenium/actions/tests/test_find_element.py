import pytest
from screenplay_selenium.actions import navigate_to, find_element, set_find_timeout_to
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_finding_an_element_that_exists(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'hello_id')).and_store_as('hello')
    )

    assert returned_value.text == 'hello'

    stored_value = user.state['hello'].value

    assert stored_value.text == 'hello'


@pytest.mark.slow
def test_attempting_to_find_an_element_that_does_not_exists(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        set_find_timeout_to(2).seconds_and_then(
            find_element((By.ID, 'does_not_exist')).and_store_as('hello')
        )
    )

    assert returned_value is None

    stored_value = user.state['hello'].value

    assert stored_value is None
