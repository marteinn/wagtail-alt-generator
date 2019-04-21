## Running tests

This library include tests for the different providers.

### Getting started

- Make sure to install dev requirements: `pip install -r requirements/tests.txt`
- Copy test_vars.sh and fill in the blanks `cp test_vars.example.sh test_vars.sh`


### Running

- Run tests: `source test_vars.sh && python runtests.py`

You can also run separate test cases: `runtests.py tests.test_cognitive_service.CognitiveServiceTest`

