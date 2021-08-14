from screenplay import Actor
from screenplay.log import Log
from itertools import chain


def capture_log_messages(user: Actor, *actions):
    original_log_function = Log.write_line
    log_text = []

    def write_line(*values, sep=''):
        line = sep.join(map(str, chain.from_iterable(values)))
        log_text.append(line)

    Log.write_line = write_line

    try:
        user.attempts_to(*actions)
    finally:
        Log.write_line = original_log_function

    return log_text
