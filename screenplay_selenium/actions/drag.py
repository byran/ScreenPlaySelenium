from os import path
from screenplay import Action, Actor, log_message
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from screenplay_selenium.abilities import browser_for


class _drag_base(Action):
    def __init__(self):
        super().__init__()
        self._dragElementId = None
        self._dropElementId = None

    def stored_element(self, id: str):
        self._dragElementId = id
        return self

    def onto_stored_element(self, id: str):
        self._dropElementId = id
        return self


class actionchain_drag(_drag_base):
    @log_message('Drag stored element "{self._dragElementId}" onto stored element "{self._dropElement}"')
    def perform_as(self, actor: Actor):
        drag: WebElement = actor.state[self._dragElementId].value
        drop: WebElement = actor.state[self._dropElementId].value
        driver = browser_for(actor)

        # ActionChains(driver).click_and_hold(drag).move_to_element(drop).release(drop).perform()
        ActionChains(driver).drag_and_drop(drag, drop).perform()


def load_drag_js():
    with open(path.join(path.dirname(__file__), 'drag.js')) as file:
        lines = file.readlines()
        return ''.join(lines)


_drag_js = load_drag_js()


class html5_drag(_drag_base):
    @log_message('Drag stored element "{self._dragElementId}" onto stored element "{self._dropElement}"')
    def perform_as(self, actor: Actor):
        drag: WebElement = actor.state[self._dragElementId].value
        drop: WebElement = actor.state[self._dropElementId].value
        driver = browser_for(actor)
        driver.execute_script(_drag_js, drag, drop)


drag = html5_drag
