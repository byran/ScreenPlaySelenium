from screenplay.log import Log
from screenplay_selenium.actions import navigate_to, find_element, text_of, click_on, enter_text
from os import path
from selenium.webdriver.common.by import By
from .test_helpers import capture_log_messages
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_entering_text_into_a_stored_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'third_text')).and_store_as('textbox'),
        enter_text('Hello World').into_stored_element('textbox'),
        click_on().element((By.ID, 'third')),
        find_element((By.ID, 'output')).and_store_as('output_div'),
        text_of().stored_element('output_div')
    )

    assert returned_value == 'Hello World'


def test_entering_text_into_a_located_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        enter_text('Hello World').into_element((By.ID, 'third_text')),
        click_on().element((By.ID, 'third')),
        find_element((By.ID, 'output')).and_store_as('output_div'),
        text_of().stored_element('output_div')
    )

    assert returned_value == 'Hello World'


def test_hiding_the_text_from_the_log_when_entering_text_into_a_stored_element(user):
    user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'third_text')).and_store_as('textbox')
    )

    Log.to_actions()

    log_text = capture_log_messages(
        user,
        enter_text('Hello World').into_stored_element('textbox').and_do_not_log_text()
    )

    assert len(log_text) == 1, "Only expected 1 log message, actually {n} message(s)".format(n=len(log_text))
    assert log_text[0].strip() == 'Enter text "**hidden**" into element "textbox"'


def test_hiding_the_text_from_the_log_when_entering_text_into_a_located_element(user):
    user.attempts_to(
        navigate_to(test_page)
    )

    Log.to_actions()

    log_text = capture_log_messages(
        user,
        enter_text('Hello World').into_element((By.ID, 'third_text')).and_do_not_log_text()
    )

    assert len(log_text) == 1, "Only expected 1 log message, actually {n} message(s)".format(n=len(log_text))
    assert log_text[0].strip() == 'Enter text "**hidden**" into element "(\'id\', \'third_text\')"'
