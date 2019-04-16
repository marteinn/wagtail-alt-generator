from unittest import skip

from django.test import TestCase

from wagtailaltgenerator.providers import get_provider
from wagtailaltgenerator.tests.factories import (
    MockedUrlImageFile, ImageFactory
)


test_image = 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'


class ProviderGoogleVisionTagTest(TestCase):
    @skip("External test")
    def test_provider_describe(self):
        image = ImageFactory()
        image.file = MockedUrlImageFile(image_url=test_image)

        provider = get_provider(
            'wagtailaltgenerator.providers.google_vision.GoogleVision'
        )

        data = provider().describe(image)

        self.assertIsNone(data.description)
        self.assertTrue(len(data.tags) > 0)
