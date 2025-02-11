from caption_image import caption_image
from download_image import download_image
from get_memes import get_memes

get_memes()
meme_url = caption_image(20007896, "Top text", "Bottom text")
download_image(meme_url)

