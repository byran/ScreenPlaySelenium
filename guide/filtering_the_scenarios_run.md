# Filtering the scenarions that are run

As a test run can take a long time, when developing a new scenario it's useful
to filter the tests that will be run to either a few tests or just the test
you're developing.

## Setting up the filtering

### 1. Add arguments to the '.vscode/launch.json' file to filter the scenarios that will be run

Add the following to the "Run tests" launch task to pass command line
arguments to behave to filter which tests are run.

```json
        "args": [
            "-t",
            "inProgress"
        ]
```

The "Run tests" launch task should look like below when the arguments have been
added

```json
    {
        "name": "Run tests",
        "type":"python",
        "request":"launch",
        "module": "behave",
        "console": "integratedTerminal",
        "envFile": "${workspaceFolder}/debug.env",
        "cwd": "${workspaceFolder}/src",
        "args": [
            "-t",
            "inProgress"
        ]
    },
```

### 2. Apply an 'inProgress' tag to the scenarios you want to run

```feature
Feature: The best feature in the works

  REQ-001 - It does something

  @REQ-001
  Scenario: This scenario will not be run
    Given ...

  @REQ-001 @inProgress
  Scenario: This scenario will be run
    Given ...
```

### 3. Now when you run the tests only the sceranios with an 'inProgress' tag will be run

## Do not commit the modified '.vscode/launch.json'

The ```.vscode/launch.json``` file is a tracked file, make sure you do not
commit it with filtering enabled.
