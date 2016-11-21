#!/usr/bin/env python

import os
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


if not settings.configured:
    settings.configure(
        COMPUTER_VISION_API_KEY=os.environ['COMPUTER_VISION_API_KEY'],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=[
            "wagtailaltgenerator",
            "tests",
        ],
        MIDDLEWARE_CLASSES=[],
        ROOT_URLCONF="tests.urls"
    )


def runtests():
    argv = sys.argv[:1] + ["test"] + sys.argv[1:]
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
