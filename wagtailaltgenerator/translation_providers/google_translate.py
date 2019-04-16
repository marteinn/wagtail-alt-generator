import logging

from . import AbstractTranslationProvider
from google.cloud import translate


logger = logging.getLogger(__name__)


class GoogleTranslate(AbstractTranslationProvider):
    def translate(self, strings, target_language, source_language="en"):
        client = translate.Client()
        response = client.translate(
            strings, source_language=source_language, target_language=target_language
        )

        return list(map(lambda x: x["translatedText"], response))
