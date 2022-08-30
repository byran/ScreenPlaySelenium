from screenplay_selenium.actions import navigate_to, find_element, drag
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'drag-and-drop-elements.html')


def test_dragging_a_stored_element_onto_another_stored_element(user):
    user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'dragElement')).and_store_as('draggable'),
        find_element((By.ID, 'dropTarget1')).and_store_as('dropTarget'),

        drag().stored_element('draggable').onto_stored_element('dropTarget'),

        find_element((By.CSS_SELECTOR, '#dropTarget1 > #dragElement'))
        .if_nothing_is_found_fail_with_message('Element was not dragged')
    )
