import os
import requests
import json

def download_image(input_data):
    input_data = input_data.replace("'", '"')
    
    data = json.loads(input_data)
    url = data['url']

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
