from django.conf import global_settings
from django.template import Context, Template
from django.test import TestCase, modify_settings, override_settings


class GenerateLabelTest(TestCase):
    def test_generate(self):
        self.assertTrue(True)
