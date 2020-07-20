from django.test import SimpleTestCase

from wagtailaltgenerator.providers import get_current_provider
from wagtailaltgenerator.providers.cognitive import Cognitive


class ProviderdRetrivalTest(SimpleTestCase):
    def test_generate(self):
        provider = get_current_provider()

        self.assertTrue(isinstance(provider(), Cognitive))
