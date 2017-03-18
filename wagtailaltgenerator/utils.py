import requests
import os


def get_image_data(image_url):
    '''
    Load external image and return byte data
    '''
    image_data = requests.get(image_url)

    if image_data.status_code > 200 and image_data.status_code < 300:
        return None

    return image_data.content


def get_local_image_data(image_file):
    '''
    Retrive byte data from a local file
    '''
    abs_path = os.path.abspath(image_file.path)
    image_data = open(abs_path, 'rb').read()
    return image_data
