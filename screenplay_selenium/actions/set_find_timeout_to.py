from screenplay import Action, Actor
from screenplay_selenium.abilities.browse_the_web import browse_the_web


class set_find_timeout_to(Action):
    def __init__(self, timeout: int):
        self.timeout = timeout
        self.actions = []

    def seconds_and_then(self, *actions):
        self.actions = actions
        return self

    def perform_as(self, actor: Actor):
        browse_ability = actor.ability(browse_the_web)
        timeout_before_change = browse_ability.wait_timeout

        browse_ability.wait_timeout = self.timeout

        try:
            actor.attempts_to(*self.actions)
        finally:
            browse_ability.wait_timeout = timeout_before_change
