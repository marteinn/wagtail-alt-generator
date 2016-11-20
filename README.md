# Wagtail Alt Detection

Autogenerate image descriptions with the help of computer vision. (Inspired by [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)).


## Requirements

- Python 2.7 / Python 3.4 / PyPy
- Django 1.8+
- Wagtail 1.7+
- Images must be accessible by third part (to enable Computer Vision processing)


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator (Not yet working)
```


## Quick Setup

1. Register an account on [Microsoft Cognitive Service](https://www.microsoft.com/cognitive-services/) and retrive api key for the product `Computer Vision - Preview`
2. Add the key in your django settings:
    ```
    COMPUTER_VISION_API_KEY = 'yourkey'
    ```
3. Make sure `wagtailaltgenerator` is added to your `INSTALLED_APPS`.
    ```python
    INSTALLED_APPS = (
        # ...
        'wagtailaltgenerator',
    )
    ```


## Usage

1. Upload image through the Wagtail uploader
2. Watch the title get generated
3. Done!


## Settings

- `COMPUTER_VISION_API_KEY`: Api key to the Azure Computer Vision product.


## Tests

This library include tests, just run `python runtests.py`

Before running any type of tests, make sure the env variable `COMPUTER_VISION_API_KEY` is exported.

You can also run separate test cases: `runtests.py tests.GenerateLabelTest`


## Credits

- Inspiration from [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)
- [Cognitive-Vision-Python](https://github.com/Microsoft/Cognitive-Vision-Python)


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-alt-generator is released under the [MIT License](http://www.opensource.org/licenses/MIT).
