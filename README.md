# Wagtail Alt Detection

Autogenerate image descriptions with the help of computer vision (onspired by [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)).


## Requirements

- Python 2.7 / Python 3.4 / PyPy
- Django 1.8+
- Wagtail 1.7+
- An Microsoft Cognitive Service account
- Images must be accessible by third part (to enable Computer Vision processing)


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator (Not yet working)
```


## Quick Setup

1. Register an account on [Microsoft Cognitive Service](https://www.microsoft.com/cognitive-services/)
2. Retrive api key for the product `Computer Vision - Preview`
3. Add the key in your django settings:
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

- `COMPUTER_VISION_API_KEY`: Api key to the Azure Computer Vision product.


## Tests

This library include tests, just run `python runtests.py`

Make sure to install dev requirements: `pip install -r requirements/dev.txt`

Before running any type of tests, make sure the env variable `COMPUTER_VISION_API_KEY` is exported.

You can also run separate test cases: `runtests.py tests.GenerateLabelTest`


## Credits

- Inspiration from [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)
- [Cognitive-Vision-Python](https://github.com/Microsoft/Cognitive-Vision-Python)


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-alt-generator is released under the [MIT License](http://www.opensource.org/licenses/MIT).
