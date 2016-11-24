[![PyPI version](https://badge.fury.io/py/wagtailaltgenerator.svg)](https://badge.fury.io/py/wagtailaltgenerator)

# Wagtail Alt Generator

Insert image description and tags with the help of computer vision (inspired by [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)).

[![Screen1](https://raw.githubusercontent.com/marteinn/wagtail-alt-generator/develop/img/screenshot.png)](https://www.youtube.com/watch?v=1JeCjKx0lko)

[Screencast demo](https://www.youtube.com/watch?v=1JeCjKx0lko)


## Requirements

- Python 2.7 / Python 3.5+
- Django 1.8+
- Wagtail 1.7+
- An Microsoft Cognitive Service account

- NOTE: Images must be accessible by third part (to enable Computer Vision processing). That means any image that be reached through yourdomain.com/yourimage.jpg will work, while localhost won't.


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator
```


## Quick Setup

1. Register an account on [Microsoft Cognitive Service](https://www.microsoft.com/cognitive-services/)
2. Retrive api key for the product `Computer Vision - Preview`
3. Add the key to your django settings:

    ```
    COMPUTER_VISION_API_KEY = 'yourkey'
    ```
4. Make sure `wagtailaltgenerator` is added to your `INSTALLED_APPS`.

    ```python
    INSTALLED_APPS = (
        # ...
        'wagtailaltgenerator',
    )
    ```


## Usage

1. Upload an image through Wagtail
2. Watch the title get generated...
3. ...And done!


## Settings

- `COMPUTER_VISION_API_KEY`: Computer Vision api key
- `ALT_GENERATOR_USE_TAGS`: Enable/disable image tags (True by default)
- `ALT_GENERATOR_MAX_TAGS`: The total amount of tags to use (unlimited by default)


## Tests

This library include tests, just run `python runtests.py`

Make sure to install dev requirements: `pip install -r requirements/dev.txt`

Before running any type of tests, make sure the env variable `COMPUTER_VISION_API_KEY` is exported.

You can also run separate test cases: `runtests.py tests.GenerateLabelTest`


## Git hooks

### Release start

These hooks will automatically bump the application version when using `git flow release ...`

```
chmod +x $PWD/git-hooks/release-start.sh
ln -nfs $PWD/git-hooks/release-start.sh .git/hooks/post-flow-release-start
ln -nfs $PWD/git-hooks/release-start.sh .git/hooks/post-flow-hotfix-start
```


## Distribution

### Register

```
python setup.py egg_info
twine register dist/mypkg.wh
```

### Publish

```
python setup.py sdist
twine upload dist/*
```


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-alt-generator is released under the [MIT License](http://www.opensource.org/licenses/MIT).
