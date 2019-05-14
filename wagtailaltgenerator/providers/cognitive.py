# -*- coding: utf-8 -*-
import logging

from django.conf import settings
import requests

from wagtailaltgenerator import app_settings
from wagtailaltgenerator.providers import AbstractProvider, DescriptionResult
from wagtailaltgenerator.utils import get_image_data, get_local_image_data


API_URL = "https://{}.api.cognitive.microsoft.com"

logger = logging.getLogger(__name__)


def describe_by_url(image_url):
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": settings.COMPUTER_VISION_API_KEY,
    }

    json_data = {"url": image_url}

    endpoint = API_URL.format(settings.COMPUTER_VISION_REGION)
    response = requests.post(
        "{}{}".format(endpoint, "/vision/v1.0/describe"),
        headers=headers,
        json=json_data,
    )

    if response.status_code != 200:
        logger.warning([response, response.text])
        return None

    return response.json()


def describe_by_data(image_data):
    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-Key": settings.COMPUTER_VISION_API_KEY,
    }

    endpoint = API_URL.format(settings.COMPUTER_VISION_REGION)
    response = requests.post(
        "{}{}".format(endpoint, "/vision/v1.0/describe"),
        data=image_data,
        headers=headers,
    )

    if response.status_code != 200:
        logger.warning([response, response.text])
        return None

    data = response.json()
    return data


class Cognitive(AbstractProvider):
    def describe(self, image):
        if app_settings.ALT_GENERATOR_PREFER_UPLOAD:
            if not image.is_stored_locally():
                image_data = get_image_data(image.file.url)
                data = describe_by_data(image_data)
            else:
                image_data = get_local_image_data(image.file)
                data = describe_by_data(image_data)
        else:
            data = describe_by_url(image.file.url)

        description = None
        tags = []

        min_confidence = float(app_settings.ALT_GENERATOR_MIN_CONFIDENCE) / 100.0

        if not data:
            return DescriptionResult(description=description, tags=tags)

        if "description" in data and len(data["description"]["captions"]):
            captions = data["description"]["captions"]
            captions = [
                caption["text"]
                for caption in captions
                if caption["confidence"] >= min_confidence
            ]

            if len(captions):
                description = captions[0]

        try:
            tags = data["description"]["tags"]
        except:  # NOQA
            pass

        return DescriptionResult(description=description, tags=tags)
