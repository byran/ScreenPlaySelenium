"""Action class to cause the browser to navigate to a URL"""

from screenplay import Action, Actor, log_message
from screenplay_selenium.abilities.browse_the_web import browser_for


class navigate_to(Action):
    """
    Creates an Action class to make the browser to navigate to a URL

    Arguments:

    url - The url to navigate to
    """
    def __init__(self, url: str):
        super().__init__()
        self._url = url

    @log_message('Navigate browser to "{self._url}"')
    def perform_as(self, actor: Actor):
        browser_for(actor).get(self._url)
