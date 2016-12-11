import importlib

import requests

from wagtailaltgenerator import app_settings


def get_current_provider():
    provider = app_settings.ALT_GENERATOR_PROVIDER
    return get_provider(provider)


def get_provider(path):
    module_name, class_name = path.rsplit('.', 1)
    return getattr(importlib.import_module(module_name), class_name)


class AbstractProvider(object):
    def describe(image):
        pass

    def get_image_data(self, image):
        '''
        Load external image and return byte data
        '''
        image_url = image.file.url
        image_data = requests.get(image_url)

        if image_data.status_code > 200 and image_data.status_code < 300:
            return None

        return image_data.content


class DescriptionResult(object):
    def __init__(self, description, tags):
        self.description = description
        self.tags = tags
