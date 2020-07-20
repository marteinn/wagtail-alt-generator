from unittest import mock

from django.test import SimpleTestCase

from wagtailaltgenerator.translation_providers.google_translate import GoogleTranslate
from wagtailaltgenerator.utils import translate_description_result
from wagtailaltgenerator.providers import DescriptionResult


class TranslationToDescriptionResultTest(SimpleTestCase):
    @mock.patch.object(
        GoogleTranslate,
        "translate",
        lambda *args, **kwargs: ["Min titel", "katt", "hus", "sko"],
    )
    def test_translation_mapping(self):
        result = DescriptionResult("My title", ["cat", "house", "shoe"])
        translated_result = translate_description_result(result)

        self.assertEqual(translated_result.description, "Min titel")
        self.assertEqual(translated_result.tags, ["katt", "hus", "sko"])

    @mock.patch.object(
        GoogleTranslate, "translate", lambda *args, **kwargs: ["katt", "hus", "sko"]
    )
    def test_that_description_is_excluded_when_empty(self):
        result = DescriptionResult("", ["cat", "house", "shoe"])
        translated_result = translate_description_result(result)

        self.assertEqual(translated_result.description, "")
        self.assertEqual(translated_result.tags, ["katt", "hus", "sko"])

    @mock.patch.object(
        GoogleTranslate, "translate", lambda *args, **kwargs: ["A bridge"]
    )
    def test_that_description_is_set_when_tags_are_none(self):
        result = DescriptionResult("En bro", None)
        translated_result = translate_description_result(result)

        self.assertEqual(translated_result.description, "A bridge")
        self.assertEqual(translated_result.tags, [])
