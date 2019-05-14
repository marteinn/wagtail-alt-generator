# Getting started with Azure Cognitive Services

## Requirements

- Python 3.5+
- Wagtail 2+
- Access to any of the [supported providers](#providers)


## Installation

Install the library with pip:

```
$ pip install wagtailaltgenerator
```


## Setup on Azure Cognitive Service

1. Register an account on [Azure Cognitive Service](https://www.microsoft.com/cognitive-services/)
2. Create a new resource for `Computer Vision`
3. Retrive your api key and your selected region
4. Add the key and region to your django settings:

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

