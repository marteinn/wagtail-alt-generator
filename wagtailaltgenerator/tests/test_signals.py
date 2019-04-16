from unittest import mock

from django.test import TestCase, override_settings
from wagtail.images import get_image_model
from wagtail.images.tests.utils import get_test_image_file
from wagtail_factories import ImageFactory

from wagtailaltgenerator.providers import DescriptionResult
from wagtailaltgenerator.providers.cognitive import Cognitive
from wagtailaltgenerator.translation_providers.google_translate import (
    GoogleTranslate
)


ImageModel = get_image_model()


class SignalsTest(TestCase):
    @override_settings(
        ALT_GENERATOR_PROVIDER='wagtailaltgenerator.providers.cognitive.Cognitive'
    )
    def test_that_text_get_described(self):
        with mock.patch.object(
            Cognitive,
            'describe',
            return_value=DescriptionResult(
                description="A title", tags=["blue", "green", "white"]
            )
        ) as mock_method:
            image = ImageFactory(
                title=get_test_image_file().name,
                file=get_test_image_file()
            )
            image.refresh_from_db()

        mock_method.assert_called_with(image)

        self.assertEqual(image.title, "A title")
        self.assertEqual(image.tags.all().count(), 3)
        self.assertTrue(image.tags.filter(slug__in=["blue"]).exists())

    @override_settings(
        ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG=True,
    )
    def test_that_text_gets_translated(self):
        with mock.patch.object(
            Cognitive,
            'describe',
            return_value=DescriptionResult(
                description="A title", tags=["blue", "green", "white"]
            )
        ):
            with mock.patch.object(
                GoogleTranslate,
                'translate',
                return_value=['En titel', "blå", "grön", "vit"]
            ):
                image = ImageFactory(
                    title=get_test_image_file().name,
                    file=get_test_image_file()
                )
                image.refresh_from_db()

        self.assertEqual(image.title, "En titel")
        self.assertEqual(image.tags.all().count(), 3)
        self.assertTrue(image.tags.filter(slug__in=["vit"]).exists())
