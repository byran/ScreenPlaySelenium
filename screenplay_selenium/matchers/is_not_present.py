from screenplay.matcher import Matcher
from selenium.webdriver.remote.webelement import WebElement


class is_not_present(Matcher):
    def __init__(self):
        super().__init__()
        self._fail_message = 'the element was present'

    def matches(self, answer: WebElement) -> bool:
        if answer is None:
            return True
        return False
