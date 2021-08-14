"""Action class to enter text into a webpage element"""

from screenplay import Action, Actor, log_message
from selenium.webdriver.remote.webelement import WebElement
from screenplay_selenium.abilities.browse_the_web import browser_for
from ._handle_no_such_element_base_action import handle_no_such_element_base_action


class _enter_text_into_element(handle_no_such_element_base_action):
    def __init__(self, text: str, locator):
        super().__init__()
        self._text = text
        self._locator = locator
        self._displayText = text

    @log_message('Enter text "{self._displayText}" into element "{self._locator}"')
    def perform_as(self, actor: Actor):
        element: WebElement = browser_for(actor).find_element(*self._locator)
        element.send_keys(self._text)

    def and_do_not_log_text(self):
        self._displayText = '**hidden**'
        return self


class _enter_text_into_stored_element(Action):
    def __init__(self, text: str, id: str):
        super().__init__()
        self._text = text
        self._id = id
        self._displayText = text

    @log_message('Enter text "{self._displayText}" into element "{self._id}"')
    def perform_as(self, actor: Actor):
        actor.state[self._id].value.send_keys(self._text)

    def and_do_not_log_text(self):
        self._displayText = '**hidden**'
        return self


class enter_text:
    """
    Creates an Action class to enter text into a webpage element.
    Need to call the 'into' method to specify the element.

    e.g. enter_text('Hello').into_element(textbox)

    Arguments:

    text - The text to send to the webpage element
    """
    def __init__(self, text: str):
        self._text = text

    def into_element(self, locator):
        """
        Specifies the element to enter the text into

        Arguments:

        locator - A tuple with the first element is a selenium By value and
        the second a string to specify the id/tag/etc...
        """
        return _enter_text_into_element(self._text, locator)

    def into_stored_element(self, id: str):
        """
        Specifies the stored element to enter the text into

        Arguments:

        id - The Id of the stored element
        """
        return _enter_text_into_stored_element(self._text, id)
