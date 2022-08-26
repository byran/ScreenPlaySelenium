from ._find_base_action import find_base_action
from screenplay import Actor, action_log_message


class _find_and_store_as(find_base_action):
    def __init__(self, find_action, id: str):
        super().__init__()
        self._find_action = find_action
        self._id = id

    def perform_as(self, actor: Actor):
        elements = actor.attempts_to(self._find_action)

        actor.state[self._id].set(elements)

        @action_log_message('Storing as {id}'.format(id=self._id))
        def output_log_message(var):
            pass

        output_log_message(None)

        return elements


class find_and_store_as(find_base_action):
    def and_store_as(self, id: str):
        return _find_and_store_as(self, id)
