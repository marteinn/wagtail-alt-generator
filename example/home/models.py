from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("main_image"),
    ]
