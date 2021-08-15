# ```screenplay.actions``` - Actions for checking the ```Actor```'s state and failing tests

## screenplay.actions.fail_with_message

The ```fail_with_message``` actions will cause the scenario/test to fail when
the actions is run. It's takes a single constructor parameter, the failure
message.

```python
from screenplay.actions import fail_with_message

@step('...')
def step_impl(context):
    context.they.attempts_to(
        fail_with_message('Failure message')
    )
```

## screenplay.actions.if_value_of

The ```if_value_of``` action will run a list of ```Action```s and/or
```Task```s if the value of an element of the ```Actor```'s state matches the
specified value(s).

*** TODO: Add more detail here ***

```python
from screenplay.actions import if_value_of, fail_with_message

@step('...')
def step_impl(context):
    context.they.attempts_to(
        if_value_of('ok_button').is_None().then(
            fail_with_message('Unable to find the "OK" button')
        )
    )
```

# ```screenplay.actions``` - Actions for accessing the ```Actor```'s state

## screenplay.actions.select_element_at_index

# ```screenplay.actions``` - Actions for slowing tests

## screenplay.actions.pause_for

Pauses the execution of the test/scenario for the specified amount of time. The
action takes one constructor parameter, the time (in seconds by default).

The ```pause_for``` action has two methods that modify it's behaviour:

* ```seconds()``` - specifies the time is in seconds. Although this call is
  optional (as the time is in seconds by default), it is recommended.
* ```milliseconds()``` - specifies the time is in milliseconds instead of
  seconds.

```python
from screenplay.actions import pause_for

@step('...')
def step_impl(context):
    context.they.attempts_to(
        pause_for(2).seconds(),
        pause_for(100).milliseconds()
    )
```
