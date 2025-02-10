# memechain
So the idea here is to make an llm agent with tools that use https://imgflip.com/api to turn natural language into a meme.

![memechain](https://i.imgflip.com/9jr481.jpg)

## Setup

```bash
python -m venv env
source env/bin/activate
```

```bash
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
