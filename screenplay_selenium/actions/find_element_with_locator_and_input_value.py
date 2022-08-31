from screenplay import Actor, log_message
from selenium.common.exceptions import TimeoutException
from ._find_redirect import find_redirect


class find_element_with_locator_and_input_value(find_redirect):
    def __init__(self, locator: str, value: str):
        super().__init__()
        self._locator = locator
        self._value = value

    @log_message('Finding element {self._locator} with input value "{self._value}"')
    def perform_as(self, actor: Actor):
        elements = []
        try:
            elements = self._search_location(actor).find_elements(*self._locator)
        except TimeoutException:
            pass

        element = next((e for e in elements if e.get_attribute('value') == self._value), None)

        return element
