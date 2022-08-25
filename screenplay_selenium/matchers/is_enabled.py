from screenplay.matcher import Matcher
from selenium.webdriver.remote.webelement import WebElement


class is_enabled(Matcher):
    def __init__(self):
        super().__init__()
        self._fail_message = 'the element is not enabled'

    def matches(self, answer: WebElement) -> bool:
        if answer.is_enabled():
            return True
        return False
