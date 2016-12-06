# -*- coding: utf-8 -*-

import boto3
import requests

from wagtailaltgenerator.providers import (
    AbstractProvider,
    DescriptionResult
)


class Rekognition(AbstractProvider):
    def __init__(self, *args, **kwargs):
        self.client = boto3.client('rekognition')
        super(Rekognition, self).__init__(*args, **kwargs)

    def describe(self, image):
        image_url = image.file.url
        image_data = requests.get(image_url)

        description = None
        tags = []

        if image_data.status_code == 200:
            response = self.client.detect_labels(
                Image={
                    'Bytes': image_data.content,
                },
                MinConfidence=50
            )
            if response['Labels']:
                for label in response['Labels']:
                    tags.append(label['Name'])

        return DescriptionResult(
            description=description,
            tags=tags,
        )
