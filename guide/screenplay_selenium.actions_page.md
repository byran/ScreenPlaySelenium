# ```screenplay_selenium.actions``` - Page object used in examples

Some of the code examples use the page file below

```python
# pages/google_homepage.py
from selenium.webdriver.common.by import By


class google_homepage:
    search_textbox = (By.NAME, 'q')
```
