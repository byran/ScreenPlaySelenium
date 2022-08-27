from screenplay import Actor, log_message
from selenium.common.exceptions import TimeoutException
from ._find_base_action import find_base_action
from ._find_and_store_as import find_and_store_as
from ._find_redirect import find_redirect


class _find_elements_filter(find_and_store_as):
    def __init__(self, original: find_base_action, filter: find_redirect):
        super().__init__()
        self._original = original
        self._filter = filter

    def perform_as(self, actor: Actor):
        elements = actor.attempts_to(self._original)

        if elements is None:
            return None

        filtered_elements = []
        for element in elements:
            if isinstance(self._filter, find_redirect):
                self._filter.in_WebElement(element)
            if actor.attempts_to(self._filter) is not None:
                filtered_elements.append(element)

        return filtered_elements if len(filtered_elements) > 0 else None


class find_elements(find_redirect):
    def __init__(self, locator):
        super().__init__()
        self._locator = locator

    def only_elements_where_something_is_found_using(self, filter: find_redirect):
        return _find_elements_filter(self, filter)

    @log_message("Finding elements '{self._locator[1]}'")
    def perform_as(self, actor: Actor):
        elements = None
        try:
            elements = self._search_location(actor).find_elements(*self._locator)
        except TimeoutException:
            pass

        return elements
