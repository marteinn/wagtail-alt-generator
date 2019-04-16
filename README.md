[![PyPI version](https://badge.fury.io/py/wagtailaltgenerator.svg)](https://badge.fury.io/py/wagtailaltgenerator)
[![Build Status](https://travis-ci.org/marteinn/wagtail-alt-generator.svg?branch=develop)](https://travis-ci.org/marteinn/wagtail-alt-generator)

# Wagtail Alt Generator

Generate image description and tags with the help of computer vision (inspired by [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)).

[![Screen1](https://raw.githubusercontent.com/marteinn/wagtail-alt-generator/develop/img/screenshot.png)](https://www.youtube.com/watch?v=1JeCjKx0lko)

[Screencast demo](https://www.youtube.com/watch?v=1JeCjKx0lko)


## Supported providers

- [Azure Cognitive Services](#azure-cognitive-services)
- [AWS Rekognition](#aws-rekognition)
- [Google Vision](#google-vision)


## Translation providers

- [Google Translate](#google-translate)


## Requirements

- Python 3.5+
- Wagtail 2+
- Access to any of the [supported providers](#providers)


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator
```

Depending on your selected provider, you might also need extra requirements (example `pip install wagtailaltgenerator[rekognition]`. Please check the install instructions for the various providers below.


## Quick Setup (on Azure Cognitive Service)

1. Install `pip install wagtailaltgenerator`
2. Register an account on [Azure Cognitive Service](https://www.microsoft.com/cognitive-services/)
3. Create a new resource for `Computer Vision`
4. Retrive your api key and your selected region
5. Add the key and region to your django settings:

    ```
    COMPUTER_VISION_API_KEY = 'yourkey'
    COMPUTER_VISION_REGION = 'your-region' (example northeurope)
    ```
6. Make sure `wagtailaltgenerator` is added to your `INSTALLED_APPS`.

    ```python
    INSTALLED_APPS = (
        # ...
        'wagtailaltgenerator',
    )
    ```


## Usage

1. Upload an image through Wagtail
2. Watch the title and/or tags get generated...
3. ...And done!


## General settings

- `ALT_GENERATOR_USE_TAGS`: Enable/disable image tags (`True` by default)
- `ALT_GENERATOR_MAX_TAGS`: The maximum amount of tags to use from service (default `-1`, unlimited)
- `ALT_GENERATOR_PROVIDER`: The provider you would like to use (`wagtailaltgenerator.providers.cognitive.Cognitive` is default)
- `ALT_GENERATOR_MIN_CONFIDENCE`: The minimum accepted percentage of confidence the provider has in describing the image (default `0`, accept any).
- `ALT_GENERATOR_PREFER_UPLOAD`: If you want your provider to read asset by url, or through binary upload (default `True`, always try to post image). Only Azure Cognitive Services supports this.
- `ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG`: If you want to translate the generated text to your local language (default `False`)
- `ALT_GENERATOR_TRANSLATION_PROVIDER`: The language provider you would like to use (`wagtailaltgenerator.translation_providers.google_translate.GoogleTranslate` is default)


## Providers

### Azure Cognitive Services

Azure's computer vision API. [Docs](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)

- (+) Supports both tags and descriptions

#### Settings

- `ALT_GENERATOR_PROVIDER`: `'wagtailaltgenerator.providers.cognitive.Cognitive'`
- `COMPUTER_VISION_API_KEY`: Azure Computer Vision API key
- `COMPUTER_VISION_REGION`: The default region to use, e.g. westus, northeurope, etc


### AWS Rekognition

Amazon's image analysis API. [Docs](https://aws.amazon.com/rekognition/)

- (+) Stable
- (-) Supports only tags

#### Installing

Add `...[rekognition]` when you install wagtailaltgenerator (this will install the extra packages required).

- `pip install wagtailaltgenerator[rekognition]`

#### Settings

The Rekognition provider is based on [boto](http://boto3.readthedocs.io/) and uses its [configuration](http://boto3.readthedocs.io/en/latest/guide/configuration.html).

These are three of the most common settings:

- `AWS_ACCESS_KEY_ID`: The access key for your AWS account
- `AWS_SECRET_ACCESS_KEY`: The secret key for your AWS account
- `AWS_DEFAULT_REGION`: The default region to use, e.g. us-west-2, eu-west-1, etc

You also need to define the provider:

- `ALT_GENERATOR_PROVIDER`: `'wagtailaltgenerator.providers.rekognition.Rekognition'`


### Google Vision

Google's Cloud Vision API [docs](https://cloud.google.com/vision/).

- (+) Stable
- (-) Support only tags

#### Installing

- `pip install wagtailaltgenerator[google_vision]`

#### Settings

The Google Vision provider is based on `google-api-python-client` and are typically done using [Application Default Credentials](https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow) for authentication.

You can authenticate locally with the [Google Cloud SDK](https://cloud.google.com/sdk/), on production with either the built in credentials (if you already run on Google Cloud) or with a [Service Account key file](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount).

You also need to define the provider:

- `ALT_GENERATOR_PROVIDER`: `'wagtailaltgenerator.providers.google_vision.GoogleVision'`


## Translation providers

The generated descriptions are returned as english, so we need to use separate translation providers to translate them to your websites local language.

### Google Translate

Google's Cloud Translation Api [docs](https://cloud.google.com/translate/docs/).

#### Installing

- `pip install wagtailaltgenerator[google_translate]`

#### Settings

The Google Cloud Translation Api uses `google-cloud-translate` and are typically authenticated using [Application Default Credentials](https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow) for authentication.

You can authenticate locally with the [Google Cloud SDK](https://cloud.google.com/sdk/), on production with either the built in credentials (if you already run on Google Cloud) or with a [Service Account key file](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount).

You also need to activate translation

- `ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG`: `True`


## Tests

This library include tests for the different providers.

### Getting started

- Make sure to install dev requirements: `pip install -r requirements/tests.txt`
- Copy test_vars.sh and fill in the blanks `cp test_vars.example.sh test_vars.sh`

### Running

- Run tests: `source test_vars.sh && python runtests.py`

You can also run separate test cases: `runtests.py tests.test_cognitive_service.CognitiveServiceTest`


### Release start

These hooks will automatically bump the application version when using `git flow release ...`

```bash
chmod +x $PWD/git-hooks/bump-version.sh
ln -nfs $PWD/git-hooks/bump-version.sh .git/hooks/post-flow-release-start
ln -nfs $PWD/git-hooks/bump-version.sh .git/hooks/post-flow-hotfix-start
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
