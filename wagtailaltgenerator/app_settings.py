from django.conf import settings


DEFAULT_PROVIDER = 'wagtailaltgenerator.providers.cognitive.Cognitive'  # NOQA

ALT_GENERATOR_USE_TAGS = getattr(settings, 'ALT_GENERATOR_USE_TAGS', True)
ALT_GENERATOR_MAX_TAGS = getattr(settings, 'ALT_GENERATOR_MAX_TAGS', -1)
ALT_GENERATOR_PROVIDER = getattr(settings, 'ALT_GENERATOR_PROVIDER', DEFAULT_PROVIDER)

# COMPUTER_VISION_API_KEY = getattr(settings, 'ALT_GENERATOR_MAX_TAGS', -1)
