#!/usr/bin/env python

import os
import sys

from django.conf import settings
from django.core.management import execute_from_command_line

DEBUG = False

TIME_ZONE = 'Europe/Stockholm'

DATABASES={
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

SECRET_KEY = 'not needed'

USE_TZ = True

LANGUAGE_CODE = "en"

INSTALLED_APPS=[
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    "django.contrib.admin",

    'wagtail.core',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.images',
    "wagtail.documents",
    'taggit',

    "wagtailaltgenerator",
    "wagtailaltgenerator.tests.demopages",
    "wagtailaltgenerator.tests.demosite",
]

ROOT_URLCONF = 'wagtailaltgenerator.tests.demosite.urls'

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ALT_GENERATOR_MIN_CONFIDENCE = 0

COMPUTER_VISION_API_KEY = os.environ['COMPUTER_VISION_API_KEY']
COMPUTER_VISION_REGION = "canada"
