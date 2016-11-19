from __future__ import absolute_import, unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver

try:
    from wagtail.wagtailimages import get_image_model
except ImportError:
    from wagtail.wagtailimages.models import get_image_model

from wagtailaltgenerator import helpers

image_cls = get_image_model()


@receiver(post_save, sender=image_cls, dispatch_uid="apply_image_alt")
def apply_image_alt(sender, instance, **kwargs):
    if not kwargs['created']:
        return

    image_url = instance.file.url
    data = helpers.describe(image_url)

    if not image_url.endswith(instance.title):
        return

    try:
        caption = data['description']['captions'][0]['text']
    except:
        caption = None

    if not caption:
        return

    instance.title = caption
    instance.save
