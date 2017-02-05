from django.test import TestCase

from wagtailaltgenerator import app_settings
from wagtailaltgenerator.providers import get_provider
from wagtailaltgenerator.providers.cognitive import (
    describe_by_url,
    describe_by_data,
)

from tests.factories import MockedUrlImageFile, ImageFactory


test_image = 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'


class CognitiveServiceTest(TestCase):
    def test_api_describe_by_url(self):
        image_url = test_image
        data = describe_by_url(image_url)

        self.assertTrue('description' in data)
        self.assertTrue('captions' in data['description'])
        self.assertTrue(len(data['description']['captions']) > 0)
        self.assertTrue('text' in data['description']['captions'][0])

    def test_api_describe_by_data(self):
        image_url = test_image
        data = describe_by_data(image_url)

        self.assertTrue('description' in data)
        self.assertTrue('captions' in data['description'])
        self.assertTrue(len(data['description']['captions']) > 0)
        self.assertTrue('text' in data['description']['captions'][0])

    def test_provider_describe_by_url(self):
        app_settings.ALT_GENERATOR_PREFER_UPLOAD = False

        image = ImageFactory()
        image.file = MockedUrlImageFile(image_url=test_image)

        provider = get_provider(
            'wagtailaltgenerator.providers.cognitive.Cognitive'
        )

        data = provider().describe(image)

        self.assertIsNotNone(data.description)
        self.assertTrue(len(data.tags) > 0)

        app_settings.ALT_GENERATOR_PREFER_UPLOAD = True

    def test_provider_describe_by_data(self):
        image = ImageFactory()
        image.file = MockedUrlImageFile(image_url=test_image)

        provider = get_provider(
            'wagtailaltgenerator.providers.cognitive.Cognitive'
        )

        data = provider().describe(image)

        self.assertIsNotNone(data.description)
        self.assertTrue(len(data.tags) > 0)
