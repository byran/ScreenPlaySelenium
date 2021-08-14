from screenplay import Action, Actor, log_message


class _text_of_stored_element(Action):
    def __init__(self, id: str):
        super().__init__()
        self._source_id = id
        self._destination_id = None
        self._stripWhitespace = False

    def stripped_of_whitespace(self):
        self._stripWhitespace = True
        return self

    def and_store_as(self, id):
        self._destination_id = id
        return self

    @log_message('Get text of stored element "{self._source_id}"')
    def perform_as(self, actor: Actor):
        text = actor.state[self._source_id].value.text

        if self._stripWhitespace:
            text = text.strip()

        if self._destination_id is not None:
            actor.state[self._destination_id].set(text)

        return text


class text_of:
    def stored_element(self, id: str):
        return _text_of_stored_element(id)
