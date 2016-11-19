# Wagtail Alt Detection

Autogenerate image titles based on computer vision.

NOTE: Currently this only works on applications where the images are public (such as uploaded on AWS S3).


## Requirements

- Python 2.7 / Python 3.4 / PyPy
- Django 1.8+


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator (Not yet working)
```


## Quick Setup

1. Register an account on Azure and retrive api key for the product `Computer Vision - Preview`
2. Add the key in your django settings:
```
COMPUTER_VISION_API_KEY = 'yourkey'
```

2. Make sure `wagtailaltgenerator` is added to your `INSTALLED_APPS`.

```python
INSTALLED_APPS = (
    # ...
    'wagtailaltgenerator',
)
```


## Usage

1. Upload image
2. Watch the title get generated
3. Done!


## Settings

- `COMPUTER_VISION_API_KEY`: Api key


## Tests

Before running any type of tests, make sure the env variable `COMPUTER_VISION_API_KEY` is exported.

This library include tests, just run `python runtests.py`

You can also run separate test cases: `runtests.py tests.GenerateLabelTest`


## Credits

- Inspiration from [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)
- [Cognitive-Vision-Python](https://github.com/Microsoft/Cognitive-Vision-Python)


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtailaltgenerator is released under the [MIT License](http://www.opensource.org/licenses/MIT).
