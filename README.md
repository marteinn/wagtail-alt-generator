[![PyPI version](https://badge.fury.io/py/wagtailaltgenerator.svg)](https://badge.fury.io/py/wagtailaltgenerator)
[![Build Status](https://travis-ci.org/marteinn/wagtail-alt-generator.svg?branch=develop)](https://travis-ci.org/marteinn/wagtail-alt-generator)

# Wagtail Alt Generator

Generate image description and tags with the help of computer vision (inspired by [altify](https://github.com/ParhamP/altify/blob/master/altify/altify)).

[![Screen1](https://raw.githubusercontent.com/marteinn/wagtail-alt-generator/develop/img/screenshot.png)](https://www.youtube.com/watch?v=1JeCjKx0lko)

[Screencast demo](https://www.youtube.com/watch?v=1JeCjKx0lko)


## Features

- Create image descriptions using computer vision
- Generate tags using computer vision
- Support for multiple service providers Azure Cognitive Services, AWS Rekognition and Google Vision
- Translate descriptions to your native language usgin Google Translate


## Documentation

- [Getting started](./docs/getting-started.md)
- [Settings](./docs/settings.md)
- Adding supported provider:
    - [Adding Azure Cognitive Services as a provider](./docs/adding-azure-cognitive-services.md)
    - [Adding AWS Rekognition as a provider](./docs/adding-aws-rekognition.md)
    - [Adding Google Vision as a provider](./docs/adding-google-vision.md)
- [Translating description/tags](./docs/adding-google-translate.md)


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail-alt-generator is released under the [MIT License](http://www.opensource.org/licenses/MIT).
