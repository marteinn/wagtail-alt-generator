#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import AppConfig


class AltGeneratorAppConfig(AppConfig):
    name = "wagtailaltgenerator"
    verbose_name = "Alt generator"

    def ready(self):
        import wagtailaltgenerator.signals  # NOQA
