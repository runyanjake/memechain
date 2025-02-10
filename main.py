import requests
import os
import json

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)
    
def get_memes():
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    result = response.json()
    
    if result['success']:
        memes = result['data']['memes']
        for meme in memes:
            print(f"ID: {meme['id']}, Name: {meme['name']}")
    else:
        print("Failed to retrieve memes.")

def create_meme(template_id, text0, text1):
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
        download_image(meme_url)
    else:
        print(f"Error: {result['error_message']}")

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        image_path = os.path.join(output_dir, url.split("/")[-1])
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved to {image_path}")
    else:
        print("Failed to download image.")


create_meme(20007896, "Top text", "Bottom text")
# get_memes()