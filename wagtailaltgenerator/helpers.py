#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
import requests


API_URL = 'https://api.projectoxford.ai'



def describe(image_url):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': settings.COMPUTER_VISION_API_KEY,
    }

    json_data = {
        "url": image_url,
    }

    response = requests.post('{}{}'.format(API_URL, '/vision/v1.0/describe'),
                             headers=headers,
                             json=json_data
                             )

    return response.json()
