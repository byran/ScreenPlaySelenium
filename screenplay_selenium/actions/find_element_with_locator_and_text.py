from screenplay import Actor, log_message
from selenium.common.exceptions import TimeoutException
from ._find_redirect import find_redirect


class find_element_with_locator_and_text(find_redirect):
    def __init__(self, locator: str, text: str):
        super().__init__()
        self._locator = locator
        self._text = text
        self._id = None

    def and_store_as(self, id: str):
        self._id = id
        return self

    @log_message('Finding element {self._locator} with text "{self._text}"')
    def perform_as(self, actor: Actor):
        elements = []
        try:
            elements = self._search_location(actor).find_elements(*self._locator)
        except TimeoutException:
            pass

        element = next((e for e in elements if e.text.strip() == self._text), None)

        if self._id is not None:
            actor.state[self._id].set(element)

        return element
