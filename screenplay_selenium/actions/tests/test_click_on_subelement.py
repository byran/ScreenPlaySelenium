from screenplay_selenium.actions import navigate_to, find_element, text_of, click_on_sub_element
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_clicking_on_a_subelement_of_a_stored_element(user):
    user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'second_div')).and_store_as('second_div')
    )

    user.attempts_to(
        click_on_sub_element((By.ID, 'second')).of_stored_element('second_div')
    )

    returned_value = user.attempts_to(
        find_element((By.ID, 'output')).and_store_as('output_div'),
        text_of().stored_element('output_div')
    )

    assert returned_value == 'second'


def test_clicking_on_a_subelement_of_a_WebElement_can_be(user):
    element = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'second_div'))
    )

    user.attempts_to(
        click_on_sub_element((By.ID, 'second')).of_WebElement(element),
    )

    returned_value = user.attempts_to(
        find_element((By.ID, 'output')).and_store_as('output_div'),
        text_of().stored_element('output_div')
    )

    assert returned_value == 'second'
