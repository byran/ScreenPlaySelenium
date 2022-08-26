from screenplay import Actor
from screenplay_selenium.abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from ._find_base_action import find_base_action


class find_redirect(find_base_action):
    def __init__(self):
        super().__init__()
        self._location: WebElement = None

    def in_WebElement(self, location: WebElement):
        self._location = location
        return self

    def _search_location(self, actor: Actor):
        if self._location is not None:
            return self._location
        else:
            return waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException))