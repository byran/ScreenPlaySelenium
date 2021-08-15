# Creating a Page

Pages classes are used with the ```screenplay_selenium.actions``` built in ```Action```s.
If you're not creating scenarios for testing a website then you'll need to
create a similar class for your domain.

## Creating a new Page class

### 1. Create a file for the page

Create a file with a name that describes the page in the ```src/pages```
directory.

### 2. Import the required dependencies

```python
from selenium.webdriver.common.by import By
```

### 3. Create the class and add locators

Locators are tuples stored as class attributes. The first element of the tuple
specifies how the element should be located using a ```By``` attribute (e.g.
```NAME```, ```CSS_SELECTOR```, etc...). The second element is a string
specifying the location of the element.

```python
from selenium.webdriver.common.by import By


class google_homepage:
    search_textbox = (By.NAME, 'q')
```
