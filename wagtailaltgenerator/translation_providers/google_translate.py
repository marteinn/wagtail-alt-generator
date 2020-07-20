import logging

from . import AbstractTranslationProvider


logger = logging.getLogger(__name__)


class GoogleTranslate(AbstractTranslationProvider):
    def translate(self, strings, target_language, source_language="en"):
        from google.cloud import translate

        client = translate.Client()
        response = client.translate(
            strings, source_language=source_language, target_language=target_language
        )

        return list(map(lambda x: x["translatedText"], response))
