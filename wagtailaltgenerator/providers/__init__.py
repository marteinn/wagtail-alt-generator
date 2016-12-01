import importlib

from django.conf import settings
from django.utils.functional import cached_property


DEFAULT_PROVIDER = 'wagtailaltgenerator.providers.cognitive_service.CognitiveService'  # NOQA


def get_current_provider():
    provider = getattr(settings, 'ALT_GENERATOR_PROVIDER', DEFAULT_PROVIDER)
    return get_provider(provider)


def get_provider(path):
    module_path, provider_name = path.rsplit('.', 1)
    module = importlib.import_module(module_path)

    provider_cls = getattr(module, provider_name)
    return provider_cls


class AbstractProvider(object):
    def describe(image):
        pass


class DescriptionResult(object):
    def __init__(self, description, tags):
        self.description = description
        self.tags = tags
