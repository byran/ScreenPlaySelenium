from screenplay import Actor, log_message
from screenplay_selenium.abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from ._find_base_action import find_base_action


class find_element(find_base_action):
    def __init__(self, locator):
        super().__init__()
        self._locator = locator
        self._id = 'Id not specified'

    def and_store_as(self, id: str):
        self._id = id
        return self

    @log_message("Finding element '{self._locator[1]}' and storing as '{self._id}'")
    def perform_as(self, actor: Actor):
        element = None
        try:
            element = waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)) \
                .find_element(*self._locator)
        except TimeoutException:
            pass

        if self._id is not None:
            actor.state[self._id].set(element)

        return element
