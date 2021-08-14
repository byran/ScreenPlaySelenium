from screenplay import Actor, log_message
from screenplay_selenium.abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from ._handle_no_such_element_base_action import handle_no_such_element_base_action


class _click_on_sub_element_of_WebElement(handle_no_such_element_base_action):
    def __init__(self, locator, parentElement):
        super().__init__()
        self._locator = locator
        self._parentElement = parentElement

    @log_message("Clicks on '{self._locator}' of WebElement")
    def perform_as(self, actor: Actor):
        def click_on_element(browser):
            self._parentElement.find_element(*self._locator).click()
            return True

        waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)).until(click_on_element)


class _click_on_sub_element_of_stored_element(handle_no_such_element_base_action):
    def __init__(self, locator, id: str):
        super().__init__()
        self._locator = locator
        self._id = id

    @log_message("Clicks on '{self._locator}' of '{self._id}")
    def perform_as(self, actor: Actor):
        def click_on_element(browser):
            actor.state[self._id].value.find_element(*self._locator).click()
            return True

        waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)).until(click_on_element)


class click_on_sub_element:
    def __init__(self, locator):
        super().__init__()
        self._locator = locator

    def of_WebElement(self, parentElement):
        return _click_on_sub_element_of_WebElement(self._locator, parentElement)

    def of_stored_element(self, id: str):
        return _click_on_sub_element_of_stored_element(self._locator, id)
