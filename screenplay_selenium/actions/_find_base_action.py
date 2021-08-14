from screenplay import Action, Actor
from screenplay.actions import fail_with_message


class _if_nothing_is_found_fail_with_message(Action):
    def __init__(self, action: Action, fail_actions: list, message: str):
        super().__init__()
        self.action = action
        self.fail_actions = fail_actions
        self.message = message

    def perform_as(self, actor: Actor):
        value = actor.attempts_to(
            self.action
        )

        if value is None:
            actor.attempts_to(
                *self.fail_actions,
                fail_with_message(self.message)
            )

        return value


def _create_empty_additional_actions():
    return []


class find_base_action(Action):
    create_fail_actions_callback = _create_empty_additional_actions

    def if_nothing_is_found_fail_with_message(self, message: str):
        return _if_nothing_is_found_fail_with_message(self, find_base_action.create_fail_actions_callback(), message)
