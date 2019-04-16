import os

import requests
from django.utils.translation import get_language

from wagtailaltgenerator.translation_providers import get_current_provider
from wagtailaltgenerator.providers import DescriptionResult


def get_image_data(image_url):
    """
    Load external image and return byte data
    """
    image_data = requests.get(image_url)

    if image_data.status_code > 200 and image_data.status_code < 300:
        return None

    return image_data.content


def get_local_image_data(image_file):
    """
    Retrive byte data from a local file
    """
    abs_path = os.path.abspath(image_file.path)
    image_data = open(abs_path, "rb").read()
    return image_data


def translate_description_result(result):
    provider = get_current_provider()()

    lang_and_country_code = get_language()
    lang_code = lang_and_country_code.split("-")[0]

    strings = []
    if result.description:
        strings = [result.description]

    if result.tags:
        strings = [*strings, *result.tags]

    translated_strings = provider.translate(strings, target_language=lang_code)

    translated_description = (
        translated_strings[0] if result.description else result.description
    )

    translated_tags = (
        translated_strings[1:] if result.description else translated_strings
    )

    return DescriptionResult(description=translated_description, tags=translated_tags)
