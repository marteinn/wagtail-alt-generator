## Settings

- `ALT_GENERATOR_USE_TAGS`: Enable/disable generation of image tags describing the image (`True` by default)
- `ALT_GENERATOR_MAX_TAGS`: The maximum amount of tags to use from service (default `-1`, which means unlimited)
- `ALT_GENERATOR_PROVIDER`: The provider you would like to use (`wagtailaltgenerator.providers.cognitive.Cognitive` is default)
- `ALT_GENERATOR_MIN_CONFIDENCE`: The minimum accepted percentage (0-100) of confidence the provider has in describing the image (default is `0`, which means any description is accepted).
- `ALT_GENERATOR_PREFER_UPLOAD`: If you want your provider to read asset by url, or through binary upload (default `True`, always try to post image). Only Azure Cognitive Services supports this.
- `ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG`: If you want to translate the generated text to your local language (default `False`)
- `ALT_GENERATOR_TRANSLATION_PROVIDER`: The language provider you would like to use (`wagtailaltgenerator.translation_providers.google_translate.GoogleTranslate` is default)
