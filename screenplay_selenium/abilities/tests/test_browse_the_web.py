from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from screenplay import Actor
from screenplay_selenium.abilities.browse_the_web import browse_the_web
from screenplay_selenium.actions.navigate_to import navigate_to
from screenplay_selenium.actions.find_element import find_element

test_page = 'file://' + path.join(path.dirname(__file__), 'index.html')


def test_The_callback_is_called_when_the_browser_is_created_and_allows_access_to_the_owning_actor():
    def created_callback(actor: Actor):
        actor.attempts_to(
            navigate_to(test_page)
        )

    user = Actor.named('user').who_can(browse_the_web.using_Chrome().after_browser_started(created_callback))

    try:
        element = user.attempts_to(
            find_element((By.ID, 'first'))
        )

        assert isinstance(element, WebElement), "Could not find the element, this indicates the callback was not called"
    finally:
        user.clean_up()
