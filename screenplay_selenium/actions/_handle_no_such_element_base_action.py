from screenplay import Action, Actor
from screenplay.actions import fail_with_message
from ._find_base_action import find_base_action
from selenium.common.exceptions import NoSuchElementException


class _if_no_such_element_fail_with_message(Action):
    def __init__(self, action: Action, fail_actions: list, message: str):
        super().__init__()
        self.action = action
        self.fail_actions = fail_actions
        self.message = message

    def perform_as(self, actor: Actor):
        try:
            return actor.attempts_to(
                self.action
            )
        except NoSuchElementException:
            actor.attempts_to(
                *self.fail_actions,
                fail_with_message(self.message)
            )


class handle_no_such_element_base_action(Action):
    def if_element_is_not_found_fail_with_message(self, message: str):
        return _if_no_such_element_fail_with_message(self, find_base_action.create_fail_actions_callback(), message)
