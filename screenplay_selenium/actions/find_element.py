from screenplay import Actor, log_message
from selenium.common.exceptions import TimeoutException
from ._find_redirect import find_redirect


class find_element(find_redirect):
    def __init__(self, locator):
        super().__init__()
        self._locator = locator

    @log_message("Finding element '{self._locator[1]}'")
    def perform_as(self, actor: Actor):
        element = None
        try:
            element = self._search_location(actor).find_element(*self._locator)
        except TimeoutException:
            pass

        return element
