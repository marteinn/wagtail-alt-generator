from django.conf import settings


DEFAULT_PROVIDER = "wagtailaltgenerator.providers.cognitive.Cognitive"  # NOQA

ALT_GENERATOR_USE_TAGS = getattr(settings, "ALT_GENERATOR_USE_TAGS", True)
ALT_GENERATOR_MAX_TAGS = getattr(settings, "ALT_GENERATOR_MAX_TAGS", -1)
ALT_GENERATOR_PROVIDER = getattr(settings, "ALT_GENERATOR_PROVIDER", DEFAULT_PROVIDER)
ALT_GENERATOR_MIN_CONFIDENCE = getattr(settings, "ALT_GENERATOR_MIN_CONFIDENCE", 50)
ALT_GENERATOR_PREFER_UPLOAD = getattr(settings, "ALT_GENERATOR_PREFER_UPLOAD", True)

ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG = getattr(
    settings, "ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG", None
)

ALT_GENERATOR_TRANSLATION_PROVIDER = getattr(
    settings,
    "ALT_GENERATOR_TRANSLATION_PROVIDER",
    "wagtailaltgenerator.translation_providers.google_translate.GoogleTranslate",
)


def get_setting(name):
    return getattr(settings, name, None) or globals()[name]
