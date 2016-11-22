#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

try:
    from wagtail.wagtailimages import get_image_model
except ImportError:
    from wagtail.wagtailimages.models import get_image_model

from wagtailaltgenerator import helpers

image_cls = get_image_model()


ALT_GENERATOR_USE_TAGS = getattr(settings, 'ALT_GENERATOR_USE_TAGS', True)
ALT_GENERATOR_MAX_TAGS = getattr(settings, 'ALT_GENERATOR_MAX_TAGS', -1)


@receiver(post_save, sender=image_cls, dispatch_uid="apply_image_alt")
def apply_image_alt(sender, instance, **kwargs):
    if not kwargs['created']:
        return

    image_url = instance.file.url
    data = helpers.describe(image_url)

    if image_url.endswith(instance.title):
        _apply_title(instance, data)

    if ALT_GENERATOR_USE_TAGS:
        _apply_tags(instance, data)

    instance.save()


def _apply_title(instance, data):
    try:
        caption = data['description']['captions'][0]['text']
    except:
        caption = None

    if not caption:
        return

    instance.title = caption


def _apply_tags(instance, data):
    tags = []

    try:
        tags = data['description']['tags']
    except:
        pass

    if ALT_GENERATOR_MAX_TAGS != -1:
        tags = tags[:ALT_GENERATOR_MAX_TAGS]

    instance.tags.add(*tags)
