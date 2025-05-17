import requests

GET_MEMES_URL = "https://api.imgflip.com/get_memes"

def get_memes(ignored="ignored"):
    return get_memes_helper()

def get_memes_helper():
    print("Retrieving meme options...")
    response = requests.get(GET_MEMES_URL)
    result = response.json()

    if result['success']:
        memes = result['data']['memes']
        memes_str = "\n".join([f"ID: {meme['id']}, Name: {meme['name']}" for meme in memes])
        return memes_str
    else:
        return "No template_ids found."

