from screenplay import Actor, log_message
from screenplay_selenium.abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from ._find_base_action import find_base_action


class find_elements(find_base_action):
    def __init__(self, locator):
        super().__init__()
        self._locator = locator
        self._id = 'Id not specified'

    def and_store_as(self, id: str):
        self._id = id
        return self

    @log_message("Finding elements '{self._locator[1]}' and storing as '{self._id}'")
    def perform_as(self, actor: Actor):
        elements = None
        try:
            elements = waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)) \
                .find_elements(*self._locator)
        except TimeoutException:
            pass

        if self._id is not None:
            actor.state[self._id].set(elements)

        return elements
