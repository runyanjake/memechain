import json
import requests

CAPTION_IMAGE_URL = "https://api.imgflip.com/caption_image"

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)   

def caption_image(template_id, text0, text1):
    config = load_config()
    username = config['username']
    password = config['password']

    url = "https://api.imgflip.com/caption_image"
    payload = {
        "template_id": template_id,
        "username": username,
        "password": password,
        "text0": text0,
        "text1": text1
    }

    response = requests.post(url, data=payload)
    result = response.json()

    if result['success']:
        meme_url = result['data']['url']
        print(f"Meme created! URL: {meme_url}")
        return meme_url
    else:
        return None
