# ```screenplay_selenium.actions``` - Actions for navigation

## ```screenplay_selenium.actions.navigate_to```

Navigates the browser to the URL passed as the first argument to the
constructor.

```python
from screenplay_selenium.actions import navigate_to

actor.attempts_to(
    navigate_to('https://www.google.co.uk')
)
```

