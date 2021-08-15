# Creating a task

## Creating a new task file

### 1. Create a file for the task

Create a new file in the ```src/tasks``` directory and name it the same as the
task you're going to create. The name should describe what the task is going to
do and should read like part of a sentance. The name should be all lower case
(unless the case is indicating a specific value) and have words separated with
an underscore ( ```_``` ).

### 2. Copy the template_task for an easy start point

Copy the contents of the ```src/tasks/template_task.py``` file (shown below)
into your new file for an easy start point. Update or remove the docstring at
the top of the file.

```python
"""Example file containing a minimum implementation of a Task"""

from screenplay import Task, Actor, log_message


class template_task(Task):
    @log_message('Enter a description of what the task does')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            # A parameter list of Action objects
        )
```

A ```Task``` must inherit from the ```Task``` class of the ```screenplay```
package. The core method of a ```Task``` is the ```perform_as``` method, this
will be called by the ScreenPlay framework when the ```Task``` is run. More on
this later.

### 3. Name the class to the name of the task

Name the class the name of the task (i.e. the same as the filename without the extension)

```python
from screenplay import Task, Actor, log_message


class search_for_Hello_world(Task):
    @log_message('Enter a description of what the task does')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            # A parameter list of Action objects
        )
```

### 4. Update the log message

Set the message passed to the ```log_message``` decerator on the
```perform_as```, this will (optionally) be output to the console when the task
is run.

```python
...

class search_for_Hello_world(Task):
    @log_message('they search for "Hello World"')
    def perform_as(self, actor: Actor):
        ...
```

### 5. Import Actions and make the actor perform them

The core method in a ```Task``` is the ```perform_as``` method, it's called by
the ScreenPlay framework when the task is run. It's passed the current
```Actor``` which it should use to run ```Action```s (or other ```Task```s)
using the ```Actor.attempts_to``` (or ```attempt_to```) method.

The ```Action```s (and ```Task```s) that the ```Task``` runs and anything else
that is required must be imported.

```python
from screenplay import Task, Actor, log_message
from screenplay_selenium.actions import enter_text, send_enter_key_to
from pages.google_homepage import google_homepage


class search_for_Hello_world(Task):
    @log_message('Enter "Hello World" into google')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text('Hello world').into_element(google_homepage.search_textbox),
            send_enter_key_to().element(google_homepage.search_textbox)
        )
```

### 6. Accepting parameters in the constructor

To make your some ```Task```s reusable it's necessary for the ```Task``` to
take parameters. If the parameter would appear at the end of the sentance then
it can be passed as a parameter to the constructor. Remember to call the base
class constructor.

``` python
...

class delete_the_file_called(Task):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

...
```

This type of ```Task``` can be used as follows:

```python
...

@step('...')
def step_impl(context):
    context.they.attempts_to(
        delete_the_file_called("hello.txt")
    )
```

### 7. Including parameters in the log message

Parameters stored as class attributes (and other class attributes) can be
included in the log message by wrapping their name in braces ```{self.xyz}```.

``` python
...

class delete_the_file_called(Task):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    @log_message('Deleting "{self.file_name}"')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            ...
        )
```


### 8. Accepting parameters in other methods

If you want to provide options for how the ```Task``` works or take
additional parameters add methods to the class. Remeber to return ```self```
from the methods.

``` python
...

class delete_the_file_called(Task):
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
        self.path = None

    def from_the_directory(self, path: str):
        self.path = path
        return self

    @log_message('Deleting "{self.file_name}" from "{self.path}"')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            ...
        )
```

This type of ```Task``` can be used as follows:

```python
...

@step('...')
def step_impl(context):
    context.they.attempts_to(
        delete_the_file_called("hello.txt").from_the_directory("/temp")
    )
```

## A completed Task file

``` python
from screenplay import Task, Actor, log_message
from screenplay_selenium.actions import enter_text, send_enter_key_to
from pages.google_homepage import google_homepage


class search_for(Task):
    def __init__(self, text: str):
        super().__init__()
        self._text = text

    @log_message('Enter "{self._text}" into google')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self._text).into_element(google_homepage.search_textbox),
            send_enter_key_to().element(google_homepage.search_textbox)
        )
```
