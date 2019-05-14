#!/usr/bin/env python

import os


DEBUG = False

TIME_ZONE = "Europe/Stockholm"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

SECRET_KEY = "not needed"

USE_TZ = True

LANGUAGE_CODE = "en"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.messages",
    "wagtail.core",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.images",
    "wagtail.documents",
    "taggit",
    "wagtailaltgenerator",
    "wagtailaltgenerator.tests.demopages",
    "wagtailaltgenerator.tests.demosite",
]

ROOT_URLCONF = "wagtailaltgenerator.tests.demosite.urls"

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.core.middleware.SiteMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
)

ALT_GENERATOR_MIN_CONFIDENCE = 0

COMPUTER_VISION_API_KEY = getattr(os.environ, "COMPUTER_VISION_API_KEY", None)
COMPUTER_VISION_REGION = "canada"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
            ]
        }
    }
]
