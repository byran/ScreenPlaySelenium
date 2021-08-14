from screenplay import Action, Actor
from screenplay_selenium.abilities.browse_the_web import browser_for


class save_screenshot_to_file(Action):
    def __init__(self, filename: str):
        super().__init__()
        self._filename = filename

    def perform_as(self, actor: Actor):
        browser_for(actor).save_screenshot(self._filename)
