from screenplay import Actor, log_message
from ._find_base_action import find_base_action


class _find_stored_element_with_text(find_base_action):
    def __init__(self, sourceId: str, text: str):
        super().__init__()
        self._sourceId = sourceId
        self._text = text
        self._id = None

    def and_store_as(self, id):
        self._id = id
        return self

    @log_message('Finding element with text "{self._text}" from "{self._sourceId}"')
    def perform_as(self, actor: Actor):
        element = None

        elements = actor.state[self._sourceId].value
        if elements is not None:
            element = next((e for e in elements if e.text.strip() == self._text), None)

        if self._id is not None:
            actor.state[self._id].set(element)

        return element


class find_stored_element_in:
    def __init__(self, id: str):
        self._id = id

    def with_text_equal_to(self, text) -> _find_stored_element_with_text:
        return _find_stored_element_with_text(self._id, text)
