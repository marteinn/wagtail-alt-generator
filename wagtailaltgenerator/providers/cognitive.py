# -*- coding: utf-8 -*-

from django.conf import settings
import requests

from wagtailaltgenerator.providers import (
    AbstractProvider,
    DescriptionResult,
)


API_URL = 'https://api.projectoxford.ai'


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

    return response.json()


class Cognitive(AbstractProvider):
    def describe(self, image):
        image_url = image.file.url
        data = describe(image_url)

        description = None
        tags = []

        try:
            description = data['description']['captions'][0]['text']
        except:
            pass

        try:
            tags = data['description']['tags']
        except:
            pass

        return DescriptionResult(
            description=description,
            tags=tags,
        )
