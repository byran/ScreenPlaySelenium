from screenplay_selenium.actions import navigate_to, find_element, find_sub_element
from os import path
from selenium.webdriver.common.by import By
from .user_fixture import user  # noqa: F401


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_finding_a_subelement_of_a_stored_element(user):
    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'parent')).and_store_as('parent'),
        find_sub_element((By.ID, 'child')).from_stored_element('parent').and_store_as('child')
    )

    assert returned_value.text == 'child'

    stored_value = user.state['child'].value

    assert stored_value.text == 'child'
