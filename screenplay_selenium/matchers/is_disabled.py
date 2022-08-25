from screenplay.matcher import Matcher
from selenium.webdriver.remote.webelement import WebElement


class is_disabled(Matcher):
    def __init__(self):
        super().__init__()
        self._fail_message = 'the element is enabled'

    def matches(self, answer: WebElement) -> bool:
        if answer.is_enabled():
            return False
        return True
