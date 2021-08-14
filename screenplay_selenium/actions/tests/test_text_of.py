from screenplay_selenium.actions import navigate_to, find_element, text_of
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_accessing_the_text_of_a_stored_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'hello_id')).and_store_as('hello'),
        text_of().stored_element('hello').and_store_as('text')
    )

    assert returned_value == 'hello'

    stored_value = user.state['text'].value

    assert stored_value == 'hello'


def test_accessing_the_text_of_a_stored_element_without_storing_it(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'hello_id')).and_store_as('hello'),
        text_of().stored_element('hello')
    )

    assert returned_value == 'hello'


def test_stripping_whitespace_from_the_text(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'world_id')).and_store_as('world'),
        text_of().stored_element('world').stripped_of_whitespace().and_store_as('text')
    )

    assert returned_value == 'world'

    stored_value = user.state['text'].value

    assert stored_value == 'world'
