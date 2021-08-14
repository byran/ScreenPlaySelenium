from screenplay import Actor, log_message
from screenplay_selenium.abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebElement
from ._find_base_action import find_base_action


class find_sub_element(find_base_action):
    def __init__(self, locator):
        super().__init__()
        self._locator = locator
        self._source_id = None
        self._destination_id = None

    def from_stored_element(self, id: str):
        self._source_id = id
        return self

    def and_store_as(self, id: str):
        self._destination_id = id
        return self

    @log_message("Finding element '{self._locator}' from '{self._source_id}' and storing as '{self._destination_id}'")
    def perform_as(self, actor: Actor):
        assert self._source_id is not None, "No source id specified"
        assert self._destination_id is not None, "No destination id specified"

        parent: WebElement = actor.state[self._source_id].value
        self.element = None

        def find_the_sub_element(browser):
            self.element = parent.find_element(*self._locator)
            return True

        waiting_browser = waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException))
        try:
            waiting_browser.until(find_the_sub_element)
        except TimeoutException:
            pass

        if self._destination_id is not None:
            actor.state[self._destination_id].set(self.element)

        return self.element
