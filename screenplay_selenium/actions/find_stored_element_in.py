from screenplay import Actor, log_message
from ._find_and_store_as import find_and_store_as


class _find_stored_element_with_text(find_and_store_as):
    def __init__(self, sourceId: str, text: str):
        super().__init__()
        self._sourceId = sourceId
        self._text = text

    @log_message('Finding element with text "{self._text}" from "{self._sourceId}"')
    def perform_as(self, actor: Actor):
        element = None

        elements = actor.state[self._sourceId].value
        if elements is not None:
            element = next((e for e in elements if e.text.strip() == self._text), None)

        return element


class find_stored_element_in:
    def __init__(self, id: str):
        self._id = id

    def with_text_equal_to(self, text) -> _find_stored_element_with_text:
        return _find_stored_element_with_text(self._id, text)
