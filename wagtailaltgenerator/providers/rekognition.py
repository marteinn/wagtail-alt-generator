# -*- coding: utf-8 -*-

import boto3

from wagtailaltgenerator import app_settings
from wagtailaltgenerator.providers import AbstractProvider, DescriptionResult
from wagtailaltgenerator.utils import get_image_data, get_local_image_data


class Rekognition(AbstractProvider):
    def __init__(self, *args, **kwargs):
        self.client = boto3.client("rekognition")
        super(Rekognition, self).__init__(*args, **kwargs)

    def describe(self, image):
        if not image.is_stored_locally():
            image_data = get_image_data(image.file.url)
        else:
            image_data = get_local_image_data(image.file)

        description = None
        tags = []

        if image_data:
            response = self.client.detect_labels(
                Image={"Bytes": image_data},
                MinConfidence=app_settings.ALT_GENERATOR_MIN_CONFIDENCE,
            )
            if response["Labels"]:
                tags = [label["Name"] for label in response["Labels"]]

        return DescriptionResult(description=description, tags=tags)
