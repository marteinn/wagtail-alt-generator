import requests


def get_image_data(image_url):
    '''
    Load external image and return byte data
    '''
    image_data = requests.get(image_url)

    if image_data.status_code > 200 and image_data.status_code < 300:
        return None

    return image_data.content
