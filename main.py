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
    You are an assistant that looks up the numerical template_id of a meme from imgflip.
    The following tools are available to you:

    1. get_memes - Does not take any agruments. Returns a list of template_ids (integer) and names (string) which are the titles of the memes that correspond to the template_id.
    2. caption_image - Given a valid template_id, top text, and bottom text, generates an image with the desired text. Returns the url of the new meme as a string.
    3. download_image - Given a valid url returned from the caption_image tool, downloads the image we made locally.

    Use these tools if necessary to answer questions.
"""

prompt_template = f"""
    {system_prompt}

    Question: {{question}}

    Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(prompt_template)

tools = [
    Tool(name="Get Memes", func=get_memes, description="Does not take any agruments. Returns a list of template_ids (integer) and names (string) which are the titles of the memes that correspond to the template_id."),
    Tool(name="Caption Image", func=caption_image, description="Given a valid template_id, top text, and bottom text, generates an image with the desired text. Returns the url of the new meme as a string."),
    Tool(name="Download Image", func=download_image, description="Given a valid url returned from the caption_image tool, downloads the image we made locally.")
]

llm = OllamaLLM(model="llama3")

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent_executor.invoke({"input": "Generate an image for the 'stick poke' meme with the top text 'come on' and the bottom text 'do something'."})
print(response)

