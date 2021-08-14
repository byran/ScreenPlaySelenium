import os
import sys
from typing import List
from screenplay import Ability, Actor
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitingWebDriver:
    def __init__(self, webdriver, time_out, ignored_exceptions=None):
        self._webdriver: WebDriver = webdriver
        self._wait = WebDriverWait(webdriver, time_out, ignored_exceptions=ignored_exceptions)

    @property
    def browser(self) -> WebDriver:
        return self._webdriver

    def get(self, url):
        return self._webdriver.get(url)

    def find_element(self, by, value) -> WebElement:
        return self._wait.until(EC.visibility_of_element_located((by, value)))

    def find_elements(self, by, value) -> List[WebElement]:
        return self._wait.until(EC.visibility_of_any_elements_located((by, value)))

    def until(self, action):
        return self._wait.until(action)


class browse_the_web(Ability):
    def __init__(self, create_browser_function: type):
        self._create_browser_function = create_browser_function
        self._webdriver = None
        self.wait_timeout = 10

    def clean_up(self):
        if self._webdriver is not None:
            self._webdriver.quit()
            self._webdriver = None

    @property
    def browser(self) -> WebDriver:
        if self._webdriver is None:
            self._webdriver = self._create_browser_function()
        return self._webdriver

    def waiting_browser(self, ignored_exceptions=None) -> WaitingWebDriver:
        return WaitingWebDriver(self.browser, self.wait_timeout, ignored_exceptions)

    @staticmethod
    def _create_Chrome_browser():
        chrome_options = ChromeOptions()
        if os.getenv('HEADLESS_BROWSER') != 'False':
            chrome_options.headless = True
        if sys.platform.startswith('win'):
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return Chrome(options=chrome_options)

    @staticmethod
    def _create_remote_Chrome_browser():
        chrome_options = ChromeOptions()
        return WebDriver(
            command_executor='http://hub:4444/wd/hub',
            desired_capabilities=chrome_options.to_capabilities()
        )

    @staticmethod
    def using_Chrome():
        return browse_the_web(browse_the_web._create_Chrome_browser)

    @staticmethod
    def using_remote_Chrome():
        return browse_the_web(browse_the_web._create_remote_Chrome_browser)


def browser_for(actor: Actor) -> WebDriver:
    return actor.ability(browse_the_web).browser


def waiting_browser_for(actor: Actor, ignored_exceptions=None) -> WaitingWebDriver:
    return actor.ability(browse_the_web).waiting_browser(ignored_exceptions=ignored_exceptions)
