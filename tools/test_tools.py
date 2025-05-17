import json
from caption_image import caption_image
from download_image import download_image
from get_memes import get_memes

# Utilities to determine the template_id
# memes = get_memes()
# print(memes)

# After determining the template_id, manually add it to the below json.
input_data = """
{
  "template_id": 87743020,
  "text": ["generated meme", "langchain error"]
}
"""
meme_url = caption_image(input_data)
input_data = json.dumps({"url": meme_url})
download_image(input_data)

