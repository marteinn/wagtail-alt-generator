from django.utils.module_loading import import_string

from wagtailaltgenerator import app_settings


def get_current_provider():
    provider = app_settings.ALT_GENERATOR_TRANSLATION_PROVIDER
    return get_provider(provider)


def get_provider(path):
    return import_string(path)


class AbstractTranslationProvider(object):
    def translate(strings, target_language, source_language="en"):
        raise NotImplementedError()
