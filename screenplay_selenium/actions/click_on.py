from screenplay import Action, Actor, log_message
from screenplay_selenium.abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from ._handle_no_such_element_base_action import handle_no_such_element_base_action


class _click_on_element(handle_no_such_element_base_action):
    def __init__(self, locator):
        super().__init__()
        self._locator = locator

    @log_message("Clicks on {self._locator}")
    def perform_as(self, actor: Actor):
        def click_on_element(browser):
            browser.find_element(*self._locator).click()
            return True

        waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)).until(click_on_element)


class _click_on_stored_element(Action):
    def __init__(self, id):
        super().__init__()
        self._id = id

    @log_message("Clicks on {self._id}")
    def perform_as(self, actor: Actor):
        actor.state[self._id].value.click()


class click_on:
    def element(self, locator):
        return _click_on_element(locator)

    def stored_element(self, id):
        return _click_on_stored_element(id)
