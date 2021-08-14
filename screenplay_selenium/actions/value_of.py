from screenplay import Action, Actor, log_message
from selenium.webdriver.remote.webdriver import WebElement


class _value_of_stored_element(Action):
    def __init__(self, id: str):
        super().__init__()
        self._id = id
        self._stripWhitespace = False

    def stripped_of_whitespace(self):
        self._stripWhitespace = True
        return self

    @log_message('Get value of stored element "{self._id}"')
    def perform_as(self, actor: Actor):
        element: WebElement = actor.state[self._id].value
        value = element.get_attribute('value')

        if self._stripWhitespace:
            value = value.strip()

        return value


class value_of:
    def stored_element(self, id: str):
        return _value_of_stored_element(id)
