from screenplay import Task, Actor, log_message
from screenplay_selenium.actions import save_screenshot_to_file
from os import path


class save_screenshot(Task):
    path = None
    index = 0

    def __init__(self):
        super().__init__()
        save_screenshot.index += 1
        self._index = save_screenshot.index

    @log_message("Save screenshot '{self._index}.png'")
    def perform_as(self, actor: Actor):
        assert save_screenshot.path is not None, "capture_screenshot.path not set before trying to capture a screenshot"
        filename = path.join(save_screenshot.path, str(self._index) + '.png')

        actor.attempts_to(
            save_screenshot_to_file(filename)
        )
