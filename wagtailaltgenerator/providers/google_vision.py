# -*- coding: utf-8 -*-
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

from wagtailaltgenerator import app_settings
from wagtailaltgenerator.providers import AbstractProvider, DescriptionResult
from wagtailaltgenerator.utils import get_image_data, get_local_image_data


class GoogleVision(AbstractProvider):
    def __init__(self, *args, **kwargs):
        credentials = GoogleCredentials.get_application_default()
        self.service = discovery.build("vision", "v1", credentials=credentials)
        super(GoogleVision, self).__init__(*args, **kwargs)

    def describe(self, image):
        if not image.is_stored_locally():
            image_data = get_image_data(image.file.url)
        else:
            image_data = get_local_image_data(image.file)

        description = None
        tags = []

        min_confidence = float(app_settings.ALT_GENERATOR_MIN_CONFIDENCE) / 100.0

        if image_data:
            image_data_base64 = base64.b64encode(image_data)

            max_results = app_settings.ALT_GENERATOR_MAX_TAGS

            request_body = {
                "requests": [
                    {
                        "image": {"content": image_data_base64.decode("UTF-8")},
                        "features": [{"type": "LABEL_DETECTION"}],
                    }
                ]
            }

            if max_results != -1:
                request_body["requests"][0]["features"][0][
                    "maxResults"
                ] = max_results  # NOQA

            service_request = self.service.images().annotate(body=request_body)

            response = service_request.execute()
            labels = response["responses"][0]["labelAnnotations"]
            tags = [
                label["description"]
                for label in labels
                if label["score"] >= min_confidence
            ]

        return DescriptionResult(description=description, tags=tags)
