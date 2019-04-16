#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from wagtail.images import get_image_model

from wagtailaltgenerator.providers import get_current_provider
from wagtailaltgenerator.utils import translate_description_result
from wagtailaltgenerator import app_settings
from wagtailaltgenerator.app_settings import get_setting


image_cls = get_image_model()


@receiver(post_save, sender=image_cls, dispatch_uid="apply_image_alt")
def apply_image_alt(sender, instance, **kwargs):
    if not kwargs['created']:
        return

    provider = get_current_provider()()
    image_url = instance.file.url

    result = provider.describe(instance)

    if get_setting("ALT_GENERATOR_TRANSLATE_TO_LOCAL_LANG"):
        result = translate_description_result(result)

    if image_url[-4:] == instance.title[-4:]:
        _apply_title(instance, result)

    if app_settings.ALT_GENERATOR_USE_TAGS:
        _apply_tags(instance, result)

    instance.save()


def _apply_title(instance, result):
    if not result.description:
        return

    instance.title = result.description


def _apply_tags(instance, result):
    if not result.tags:
        return

    tags = result.tags

    if app_settings.ALT_GENERATOR_MAX_TAGS != -1:
        tags = tags[:app_settings.ALT_GENERATOR_MAX_TAGS]

    instance.tags.add(*tags)
