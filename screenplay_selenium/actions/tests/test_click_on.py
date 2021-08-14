from screenplay_selenium.actions import navigate_to, find_element, text_of, click_on
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_clicking_on_a_stored_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'first')).and_store_as('button'),
        click_on().stored_element('button'),
        find_element((By.ID, 'output')).and_store_as('output_div'),
        text_of().stored_element('output_div')
    )

    assert returned_value == 'first'


def test_clicking_on_a_located_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        click_on().element((By.ID, 'first')),
        find_element((By.ID, 'output')).and_store_as('output_div'),
        text_of().stored_element('output_div')
    )

    assert returned_value == 'first'
