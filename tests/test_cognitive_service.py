from django.test import TestCase, override_settings

from wagtail.wagtailimages.models import Image
from wagtailaltgenerator.providers import get_provider
from wagtailaltgenerator.providers.cognitive_service import (
    CognitiveService,
    describe,
)

from tests.factories import MockedUrlImageFile, ImageFactory


test_image = 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'

class CognitiveServiceTest(TestCase):
    def test_api_describe(self):
        image_url = test_image
        data = describe(image_url)

        self.assertTrue('description' in data)
        self.assertTrue('captions' in data['description'])
        self.assertTrue(len(data['description']['captions']) > 0)
        self.assertTrue('text' in data['description']['captions'][0])

    def test_provider_describe(self):
        image = ImageFactory()
        image.file = MockedUrlImageFile(image_url=test_image)

        provider = get_provider(
            'wagtailaltgenerator.providers.cognitive_service.CognitiveService'
        )

        data = provider().describe(image)

        self.assertIsNotNone(data.description)
        self.assertTrue(len(data.tags) > 0)
