[![PyPI version](https://badge.fury.io/py/wagtailaltgenerator.svg)](https://badge.fury.io/py/wagtailaltgenerator)

# Wagtail Alt Generator

Insert image description and tags with the help of computer vision (inspired by [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)).

[![Screen1](https://raw.githubusercontent.com/marteinn/wagtail-alt-generator/develop/img/screenshot.png)](https://www.youtube.com/watch?v=1JeCjKx0lko)

[Screencast demo](https://www.youtube.com/watch?v=1JeCjKx0lko)


## Supported providers

- [Microsoft Cognitive Service](#microsoft-cognitive-services)
- [AWS Rekognition](#aws-rekognition)


## Requirements

- Python 2.7 / Python 3.5+
- Django 1.8+
- Wagtail 1.7+
- Access to any of the [supported providers](#providers)

- NOTE: Images must be accessible to third parties (to enable computer vision processing). That means any image that can be reached through, for instance yourdomain.com/yourimage.jpg will work, while localhost images won't.


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator
```


## Quick Setup (on Microsoft Cognitive Service)

1. Register an account on [Microsoft Cognitive Service](https://www.microsoft.com/cognitive-services/)
2. Retrieve API key for the product `Computer Vision - Preview`
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


## General settings

- `ALT_GENERATOR_USE_TAGS`: Enable/disable image tags (True by default)
- `ALT_GENERATOR_MAX_TAGS`: The total amount of tags to use (unlimited by default)
- `ALT_GENERATOR_PROVIDER`: The provider you would like to use (Cognitive Services is default)


## Providers

### Microsoft Cognitive Services

Microsofts computer vision API. [Docs](https://microsoft.com/cognitive-services/en-us/computer-vision-api)

- (Pros) Supports both tags and descriptions
- (Cons) Service still in preview
- (Cons) Requires monthly API key rotation

#### Settings

- `ALT_GENERATOR_PROVIDER`: `wagtailaltgenerator.providers.cognitive.Cognitive`
- `COMPUTER_VISION_API_KEY`: Microsoft Cognitive Service API key


### AWS Rekognition

Amazon's image analysis API. [Docs](https://aws.amazon.com/rekognition/)

- (Pros) Stable
- (Cons) Supports only tags

#### Installing

Add `...[rekognition]` when you install wagtailaltgenerator (this will install the extra packages required).

- `pip install wagtailaltgenerator[rekognition]`

#### Settings

The Rekognition provider is based on [boto](http://boto3.readthedocs.io/) and uses its [configuration](http://boto3.readthedocs.io/en/latest/guide/configuration.html).

These are three of the most common settings:

- `AWS_ACCESS_KEY_ID`: The access key for your AWS account
- `AWS_SECRET_ACCESS_KEY`: The secret key for your AWS account
- `AWS_DEFAULT_REGION`: The default region to use, e.g. us-west-2, us-west-2, etc

You also need to define the provider:

- `ALT_GENERATOR_PROVIDER`: `wagtailaltgenerator.providers.rekognition.Rekognition`


## Tests

This library include tests for the different providers.

### Getting started

- Make sure to install dev requirements: `pip install -r requirements/tests.txt`
- Copy test_vars.sh and fill in the blanks `cp test_vars.example.sh test_vars.sh`

### Running

- Run tests: `source test_vars.sh && python runtests.py`

You can also run separate test cases: `runtests.py tests.GenerateLabelTest`


### Release start

These hooks will automatically bump the application version when using `git flow release ...`

```bash
chmod +x $PWD/git-hooks/release-start.sh
ln -nfs $PWD/git-hooks/release-start.sh .git/hooks/post-flow-release-start
ln -nfs $PWD/git-hooks/release-start.sh .git/hooks/post-flow-hotfix-start
```


## Distribution

### Register

```bash
python setup.py egg_info
twine register dist/mypkg.wh
```

### Publish

```bash
python setup.py sdist
twine upload dist/*
```


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-alt-generator is released under the [MIT License](http://www.opensource.org/licenses/MIT).
