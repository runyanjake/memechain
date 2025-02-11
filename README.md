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
If failing, check status of ollama process:
```
sudo service ollama status
```


