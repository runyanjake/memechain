from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, AgentType, Tool, initialize_agent

import requests
import os

from tools.get_memes import get_memes
from tools.caption_image import caption_image
from tools.download_image import download_image

system_prompt = """
You are an assistant that helps users create memes using the Imgflip API. 

Your tasks include:
1. Searching for the numerical template_id of a requested meme using the "Get Memes" tool.
   - This tool should only be used once per request.
   - If the template_id cannot be found, inform the user.

2. Generating a meme using the "Caption Image" tool once the template_id is found.
   - The tool input must be valid JSON with the keys: "template_id" (integer) and "text" (list of strings). Keys must be enclosed in double quotes.

3. Downloading the generated meme using the "Download Image" tool if requested.

Your tool invocations must match the exact string of one of the tools listed above.
"""

prompt_template = f"""
{system_prompt}

Question: {{question}}

Answer: Let's think step by step. We should generate exactly one meme given the directions of the user. I will not ask the user for additional input after their request. Once the meme is created, I will conclude our conversation.
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

tools = [
    Tool(name="Get Memes", func=get_memes, description="Does not take any agruments. Returns a list of template_ids (integer) and names (string) which are the titles of the memes that correspond to the template_id."),
    Tool(name="Caption Image", func=caption_image, description="Given a template_id and list of text strings, returns the url of a new meme as a string. Tool input is valid json syntax, with the following keys: 'template_id' (integer) and 'text' (list of strings)."),
    Tool(name="Download Image", func=download_image, description="Given a valid url returned from the caption_image tool, downloads the image we made locally. Tool input is valid json syntax, with the following key: 'url' (string).")
]

llm = OllamaLLM(model="llama3")

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent_executor.invoke({"input": "Generate an image for the 'two buttons' meme with first text 'generated meme' and second text 'langchain error'."})
print(response)

