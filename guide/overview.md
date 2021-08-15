# Guide to using ScreenPlay with Behave

## General process for writing a feature & scenarios

1. Writing a feature file
2. [Create step definitions for the feature steps](creating_step_definitions.md)
3. For each given or when (generic) step definition:
   1. [Implement the tasks that the step definition runs](creating_a_task.md)
   2. [Implement a page to hold the locators](creating_a_page.md)
   3. (optionally) Implement actions to complete the tasks
4. For each then step definition:
   1. Implement the question to get information about the state of the system
   under test
   2. Implement the matcher to check the answer the question returned

## Other ScreenPlay features

* Using the Actor's state to store information
* Implementing abilitites

## Built in Abilities, Tasks, Actions, Matchers

### Abiltiies

* screenplay_selenium.abilities.browse_the_web

### Tasks

* screenplay_selenium.tasks.save_screenshot

### Actions

#### ```screenplay.actions```

[screenplay.actions](screenplay.actions.md)

* screenplay.actions.fail_with_message
* screenplay.actions.if_value_of
* screenplay.actions.pause_for
* screenplay.actions.select_element_at_index

#### ```screenplay_selenium.actions```

[Actions for navigation](screenplay_selenium.actions_navigation.md)

* screenplay_selenium.actions.navigate_to

[Actions for saving screenshots](screenplay_selenium.actions_save_screenshots.md)

* screenplay_selenium.actions.save_screenshot_to_file

[Actions for finding elements](screenplay_selenium.actions_find.md)

* screenplay_selenium.actions.find_element
* screenplay_selenium.actions.find_element_with_locator_and_text
* screenplay_selenium.actions.find_elements
* screenplay_selenium.actions.find_stored_element_in
* screenplay_selenium.actions.find_sub_element

[Actions for interacting with elements](screenplay_selenium.actions_interacting.md)

* screenplay_selenium.actions.click_on
* screenplay_selenium.actions.click_on_sub_element
* screenplay_selenium.actions.enter_text
* screenplay_selenium.actions.send_key_to

[Actions for querying information](screenplay_selenium.actions_information.md)

* screenplay_selenium.actions.text_of
* screenplay_selenium.actions.value_of

### Matchers

screenplay.matchers

* screenplay.matchers.contains
* screenplay.matchers.equals
* screenplay.matchers.is_an_empty_list

screenplay_selenium.matchers

* screenplay_selenium.matchers.is_displayed
* screenplay_selenium.matchers.is_not_present
