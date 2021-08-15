# Creating step definitionss

It's advised to [filter the scenarios](filtering_the_scenarios_run.md) that are
run when developing new scenarios.

## Writing the step definitionss

### 1. Run the tests and the copy the suggested step definitions

When you run the tests behave will provide suggested step definitions for all
the steps that weren't matched. Copy these step definitions and paste them into
a file in the ```src/features/steps``` directory. If there isn't an appropriate
file then create a new file with a descriptive filename.

You should now have a file that looks similar to below.

```python
@given(u'Byran has opened Google')
def step_impl(context):
    throw ...

@when(u'they search for "Hello World"')
def step_impl(context):
    throw ...

@then(u'they should see a result for \'"Hello, World!" program - Wikipedia\'')
def step_impl(context):
    throw ...
```

### 2. Import the required decorators and replace definition types

Add imports for the ```step``` and ```then``` decorators from ```behave```
at the top of the file.

```python
from behave import step, then
```

Replace the ```@given``` and ```@when``` definition decorators with then generic
```@step``` definition decorator. This allows the step definitions to be used
for both Given and When steps. As the ```@then``` steps are checking things they
should not be converted to the generic definition decorators.

The file should now look like below.

```python
from behave import step, then


@step(u'Byran has opened Google')
def step_impl(context):
    throw ...

@step(u'they search for "Hello World"')
def step_impl(context):
    throw ...

@then(u'they should see a result for \'"Hello, World!" program - Wikipedia\'')
def step_impl(context):
    throw ...
```

### 3. Add parameters to your generic and then step definitions

Add step parameters enclosed in braces (e.g. ```{parameter}```) to yout step
definition text and matching parameters to the step function.

(Note - Step parameters use the named fields syntax of the
[parse](https://pypi.org/project/parse/) library in step definitions.)

```python
...

@step(u'{actor} has opened Google')
def step_impl(context: runner.Context, actor: str):
    throw ...

...
```

### 4. Implement the generic step definitions functions

Import the required tasks to implement the step definition function and call
them from the step definition function. Make the actor ```attempt_to```
(or ```attempts_to```) the tasks. The current actor can be accessed from the
context using ```context.they```.

```python
from behave import step, then
from tasks.search_for import search_for

...

@step(u'they search for "{search_text}"')
def step_impl(context: runner.Context, search_text: str):
    context.they.attempt_to(
        search_for(search_text)
    )

...
```
If the step definition should also switch the active actor then use
```context.actors.switch_active(<actor>)```.

```python
from behave import runner, step
from tasks.open_google import open_google

...

@step(u'{actor} has opened Google')
def step_impl(context: runner.Context, actor: str):
    context.actors.switch_active(actor)
    context.they.attempt_to(
        open_google()
    )

...
```

### 5 Implement the then step definition functions

Import the required questions and matchers to check the state of the system.
You can then use the actor's ```should``` method to check if the answer to the
```Question``` matches the expected result of the ```Matcher``` using a
```Condition``` (usually ```see_that```). The actors ```should``` method can
take one or more ```Condition```s. ```Condition```s have three methods that
run a list of tasks depending on the result of the condition:

* ```if_they_do(...)```
* ```if_they_do_not(...)```
* ```regardless_of_that(...)```

```python
from behave import runner, step
from screenplay.matchers.contains import contains
from screenplay.condition import see_that
from questions.the_search_result_titles import the_search_result_titles
from screenplay_selenium.tasks import save_screenshot

...

@step(u"they should see a result for '{expected}'")
def step_impl(context: runner.Context, expected: str):
    context.they.should(
        see_that(the_search_result_titles(), contains(expected))
        .regardless_of_that(
            save_screenshot()
        )
    )

...
```

## A completed step definition file

Following all these steps you will have a file that looks like file below.

```python
from behave import runner, step
from screenplay.matchers.contains import contains
from screenplay.condition import see_that
from tasks.search_for import search_for
from tasks.open_google import open_google
from questions.the_search_result_titles import the_search_result_titles
from screenplay_selenium.tasks import save_screenshot


@step(u'{actor} has opened Google')
def step_impl(context: runner.Context, actor: str):
    context.actors.switch_active(actor)
    context.they.attempt_to(
        open_google()
    )


@step(u'they search for "{search_text}"')
def step_impl(context: runner.Context, search_text: str):
    context.they.attempt_to(
        search_for(search_text)
    )


@step(u"they should see a result for '{expected}'")
def step_impl(context: runner.Context, expected: str):
    context.they.should(
        see_that(the_search_result_titles(), contains(expected))
        .regardless_of_that(
            save_screenshot()
        )
    )
```
