from screenplay.matcher import Matcher
from selenium.webdriver.remote.webelement import WebElement


class _IsDisplayedMatcher(Matcher):
    def __init__(self):
        super().__init__()
        self._fail_message = 'the element was not displayed'

    def matches(self, answer: WebElement) -> bool:
        if answer.is_displayed():
            return True
        return False


def is_displayed():
    return _IsDisplayedMatcher()
