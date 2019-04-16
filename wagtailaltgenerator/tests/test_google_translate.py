from unittest import mock

from django.test import TestCase

from wagtailaltgenerator.translation_providers import (
    get_provider, get_current_provider
)
from wagtailaltgenerator.translation_providers.google_translate import (
    GoogleTranslate
)


class GoogleTranslateTest(TestCase):
    def test_that_current_provider_is_google_translate(self):
        self.assertEqual(get_current_provider(), GoogleTranslate)

    def test_that_get_provider_works(self):
        provider_cls = get_provider(
            'wagtailaltgenerator.translation_providers.google_translate.GoogleTranslate'
        )

        self.assertEqual(provider_cls, GoogleTranslate)

    @mock.patch.object(
        GoogleTranslate,
        'translate',
        lambda *args, **kwargs: ['hund', 'katt'],
    )
    def test_response_gets_translated(self):
        provider_cls = get_provider(
            'wagtailaltgenerator.translation_providers.google_translate.GoogleTranslate'
        )
        translations = provider_cls().translate(
            ['dog', 'cat'],
            source_language='en',
            target_language='sv',
        )

        self.assertEqual(translations, ['hund', 'katt'])
