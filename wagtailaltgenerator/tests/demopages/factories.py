import wagtail_factories
from . import models


class ImagePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.ImagePage
