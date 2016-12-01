from django.test import TestCase

from wagtailaltgenerator.providers import get_current_provider
from wagtailaltgenerator.providers.cognitive_service import CognitiveService


class ProviderdRetrivalTest(TestCase):
    def test_generate(self):
        provider = get_current_provider()

        self.assertTrue(isinstance(provider(), CognitiveService))
