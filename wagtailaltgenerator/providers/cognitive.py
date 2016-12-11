# -*- coding: utf-8 -*-
import logging

from django.conf import settings
import requests

from wagtailaltgenerator.providers import (
    AbstractProvider,
    DescriptionResult,
)
from wagtailaltgenerator import app_settings


API_URL = 'https://api.projectoxford.ai'

logger = logging.getLogger(__name__)


def describe(image_url):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': settings.COMPUTER_VISION_API_KEY,
    }

    json_data = {
        "url": image_url,
    }

    response = requests.post('{}{}'.format(API_URL, '/vision/v1.0/describe'),
                             headers=headers,
                             json=json_data
                             )

    if response.status_code != 200:
        logging.warn(response)
        return None

    return response.json()


class Cognitive(AbstractProvider):
    def describe(self, image):
        image_url = image.file.url

        data = describe(image_url)

        description = None
        tags = []

        min_confidence = float(app_settings.ALT_GENERATOR_MIN_CONFIDENCE)/100.0

        if not data:
            return DescriptionResult(
                description=description,
                tags=tags,
            )

        if 'description' in data and len(data['description']['captions']):
            captions = data['description']['captions']
            captions = [caption['text'] for caption in captions
                        if caption['confidence'] >= min_confidence]

            if len(captions):
                description = captions[0]

        try:
            tags = data['description']['tags']
        except:
            pass

        return DescriptionResult(
            description=description,
            tags=tags,
        )
