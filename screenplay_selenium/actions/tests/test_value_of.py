from screenplay_selenium.actions import navigate_to, find_element, enter_text, value_of
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_accessing_the_value_of_a_stored_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'fourth_text')).and_store_as('textbox'),
        value_of().stored_element('textbox')
    )

    assert returned_value == 'fourth textbox'


def test_stripping_the_whitespace_of_the_accessed_value(user):
    locator = (By.ID, 'third_text')

    returned_value = user.attempts_to(
        navigate_to(test_page),
        enter_text('  text  ').into_element(locator),
        find_element(locator).and_store_as('textbox'),
        value_of().stored_element('textbox').stripped_of_whitespace()
    )

    assert returned_value == 'text'
