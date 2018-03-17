#!/usr/bin/env python

import os
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    params = dict(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'django.contrib.sites',
            'wagtail.wagtailcore',
            'wagtail.sites',
            'wagtail.users',
            'wagtail.images',
            'taggit',
            "wagtailaltgenerator",
            "tests",
        ],
        MIDDLEWARE_CLASSES=[],
        ROOT_URLCONF='tests.urls',
        ALT_GENERATOR_MIN_CONFIDENCE=0,
    )

    if 'COMPUTER_VISION_API_KEY' in os.environ:
        params.update(dict(
            COMPUTER_VISION_API_KEY=os.environ['COMPUTER_VISION_API_KEY'],
        ))

    settings.configure(**params)


def runtests():
    argv = sys.argv[:1] + ["test"] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
