# memechain
So the idea here is to make an llm agent with tools that use https://imgflip.com/api to turn natural language into a meme.

![memechain](https://i.imgflip.com/9jr481.jpg)

## Setup

### Python

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Update config.json with your imgflip username and password.
Example:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

```bash
python main.py
```

### Ollama
Note we are using the `langchain-ollama` python package (see requirements).  
Pull model
```
ollama pull llama3
```
If failing, check status of ollama process (Ubuntu):
```
sudo service ollama status
```
Or start the program from search. (MacOS)

## Results

### So This Actually Works!
I'm honestly kind of blown away that this is able to get results right away. Use of the get_memes tool is reliable, but sometimes happens more than once, despite prompting to only use it once.  
Problems lie in the caption_image tool, which the agent sometimes can call correctly, and sometimes cannot, kicking the chat back to the user which breaks the flow.  
However, when the agent is able to call caption_image correctly, we get the results we're after:

```
env➜  memechain git:(main) ✗ python main.py

> Entering new AgentExecutor chain...
Let's get started.

Thought: To generate an image for the "two buttons" meme, I need to find a template_id that corresponds to this meme. Then, I can use the Caption Image tool to create a new meme with the desired text.

Action: Get Memes
Action Input: None (no input needed)
Observation: ID: 181913649, Name: Drake Hotline Bling
ID: 87743020, Name: Two Buttons
    ...
ID: 398221598, Name: Goose Chase
Thought:Thought: Now that I have the list of template_ids and names from Get Memes, I can find the ID for the "two buttons" meme. The name "Two Buttons" matches with the template_id 87743020.

Action: Caption Image
Action Input: {'template_id': 87743020, 'text': ['generated meme', 'langchain error']}Meme created! URL: https://i.imgflip.com/9jt1zu.jpg

Observation: https://i.imgflip.com/9jt1zu.jpg
Thought:I've got the image URL!

Action: Download Image
Action Input: {'url': 'https://i.imgflip.com/9jt1zu.jpg'}

Traceback (most recent call last):
  File "/Users/runyanjake/Desktop/repositories/memechain/main.py", line 54, in <module>
    ...
  File "/Users/runyanjake/Desktop/repositories/memechain/env/lib/python3.13/site-packages/requests/sessions.py", line 792, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for "{'url': 'https://i.imgflip.com/9jt1zu.jpg'}"
```
