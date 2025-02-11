import json
import requests

CAPTION_IMAGE_URL = "https://api.imgflip.com/caption_image"

def load_config():
    with open('tools/config.json') as config_file:
        return json.load(config_file)   

def caption_image(input_data):
    # Replace single quotes with double quotes because langchain likes to use single quotes
    input_data = input_data.replace("'", '"')
    
    data = json.loads(input_data)
    template_id = data['template_id']
    text = data['text']

    config = load_config()
    username = config['username']
    password = config['password']

    url = CAPTION_IMAGE_URL
    payload = {
        "template_id": template_id,
        "username": username,
        "password": password,
    }
    
    for i in range(len(text)):
        payload[f'text{i}'] = text[i]

    response = requests.post(url, data=payload)
    result = response.json()

    if result['success']:
        meme_url = result['data']['url']
        print(f"Meme created! URL: {meme_url}")
        return meme_url
    else:
        return None
