
from screenplay import Action, Actor


class _index_of_stored_element_with_text(Action):
    def __init__(self, sourceId: str, text: str):
        super().__init__()
        self._sourceId = sourceId
        self._text = text
        self._id = None

    def and_store_as(self, id):
        self._id = id
        return self

    def perform_as(self, actor: Actor):
        index = None

        elements = actor.state[self._sourceId].value
        if elements is not None:
            for i, e in enumerate(elements):
                if e.text.strip() == self._text:
                    index = i

        if self._id is not None:
            actor.state[self._id].set(index)

        return index


class index_of_stored_element_in:
    def __init__(self, id: str):
        self._id = id

    def with_text_equal_to(self, text) -> _index_of_stored_element_with_text:
        return _index_of_stored_element_with_text(self._id, text)
