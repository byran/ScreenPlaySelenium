# ```screenplay_selenium.actions``` - Actions for finding elements

Some of the examples on this page use the
[google_homepage](screenplay_selenium.actions_page.md) page object.


## ```screenplay_selenium.actions.find_element```

Finds an element using a locator (usually from a page object) passed as the
first argument to the constructor.

This action will always return the element.

```python
from screenplay_selenium.actions import find_element
from pages.google_homepage import google_homepage

element = actor.attempts_to(
    find_element(google_homepage.search_box)
)
```

### ```.and_store_as(id)``` method

Make the action store the element in the ```Actor```'s state identified by the
first argument to the method.

```python
from screenplay_selenium.actions import find_element
from pages.google_homepage import google_homepage

actor.attempts_to(
    find_element(google_homepage.search_box).and_store_as('search_box')
)
```

### ```.if_nothing_is_found_fail_with_message(message)``` method

If the element specified by the locator could not be found, this method will
make the test fail after the element could not be found with the message passed
as the first argument to the method.

```python
from screenplay_selenium.actions import find_element
from pages.google_homepage import google_homepage

actor.attempts_to(
    find_element(google_homepage.search_box).and_store_as('search_box')
    .if_nothing_is_found_fail_with_message('Unable to find "Search Box"')
)
```

## ```screenplay_selenium.actions.find_element_with_locator_and_text```

## ```screenplay_selenium.actions.find_elements```

## ```screenplay_selenium.actions.find_sub_element```

## ```screenplay_selenium.actions.find_stored_element_in```
