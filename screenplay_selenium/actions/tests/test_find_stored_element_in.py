from screenplay_selenium.actions import navigate_to, find_elements, find_stored_element_in
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_finding_a_sub_element_by_its_text(user):
    user.attempts_to(
        navigate_to(test_page),
        find_elements((By.CSS_SELECTOR, '#list li')).and_store_as('list_elements')
    )

    returned_value = user.attempts_to(
        find_stored_element_in('list_elements').with_text_equal_to('third_li').and_store_as('found')
    )

    assert returned_value.text == 'third_li'

    stored_value = user.state['found'].value

    assert stored_value.text == 'third_li'
