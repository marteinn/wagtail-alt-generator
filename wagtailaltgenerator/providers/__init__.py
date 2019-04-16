import importlib

from wagtailaltgenerator import app_settings


def get_current_provider():
    provider = app_settings.ALT_GENERATOR_PROVIDER
    return get_provider(provider)


def get_provider(path):
    module_name, class_name = path.rsplit(".", 1)
    return getattr(importlib.import_module(module_name), class_name)


class AbstractProvider(object):
    def describe(image):
        pass


class DescriptionResult(object):
    def __init__(self, description, tags):
        self.description = description
        self.tags = tags
