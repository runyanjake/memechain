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
However, when the agent is able to call caption_image correctly, we get the results we're after, though sometimes the agent will invoke caption_image multiple times:

```
env➜  memechain git:(main) ✗ python main.py

> Entering new AgentExecutor chain...
Let's think this through...

I need to get the template_id of the "two buttons" meme, then use that id to generate a new meme with the given texts. Then, I'll download the resulting image.

Action: Get Memes
Action Input: None (just run the tool)
Observation: ID: 181913649, Name: Drake Hotline Bling
ID: 87743020, Name: Two Buttons
ID: 112126428, Name: Distracted Boyfriend
ID: 217743513, Name: UNO Draw 25 Cards
    ...
ID: 145139900, Name: Scooby doo mask reveal
ID: 360597639, Name: whe i'm in a competition and my opponent is
ID: 398221598, Name: Goose Chase
Thought:Let's think this through...

I need to get the template_id of the "two buttons" meme. I see that it has an ID of 87743020.

Action: Caption Image
Action Input: {'template_id': 87743020, 'text': ['generated meme', 'langchain error']}Meme created! URL: https://i.imgflip.com/9jt2x5.jpg

Observation: https://i.imgflip.com/9jt2x5.jpg
Thought:Let's think this through...

We've got the template ID of the "two buttons" meme. Now we need to use that ID to generate a new meme with the given texts.

Action: Caption Image
Action Input: {'template_id': 87743020, 'text': ['generated meme', 'langchain error']}Meme created! URL: https://i.imgflip.com/9jt2xg.jpg

Observation: https://i.imgflip.com/9jt2xg.jpg
Thought:I see what you're doing here!

Let's continue with the next steps.

Action: Download Image
Action Input: {'url': 'https://i.imgflip.com/9jt2x5.jpg'}Image saved to output/9jt2x5.jpg

Observation: None
Thought:Let's complete the thought process and actions.

Thought: I now know the final answer.

Final Answer: The meme is available at https://i.imgflip.com/9jt2x5.jpg.

> Finished chain.
{'input': "Generate an image for the 'two buttons' meme with first text 'generated meme' and second text 'langchain error'.", 'output': 'The meme is available at https://i.imgflip.com/9jt2x5.jpg.'}
```

![meme](https://i.imgflip.com/9jt2x5.jpg)