from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, AgentType, Tool, initialize_agent


### Prompt Definitions

system_prompt = """
    You are an assistant that performs basic arithmetic operations.

    The following tools are available to you:
    1. Add - Gets the sum of 2 numbers. Input Format: (a,b)
    2. Subtract - Gets the subtraction result of 2 numbers. Input Format: (a,b)

    Use these tools if necessary to answer questions.
"""

prompt_template = f"""
    {system_prompt}

    Question: {{question}}

    Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(prompt_template)


### Tool Definitions

def add(*args) -> float:
    args_tuple = string_to_tuple(args[0])
    assert len(args_tuple) == 2
    return args_tuple[0] + args_tuple[1]

def subtract(*args) -> float:
    args_tuple = string_to_tuple(args[0])
    assert len(args_tuple) == 2
    return args_tuple[0] - args_tuple[1]

# When tool is invoked, we get whatever the LLM wanted to send it as a string.
def string_to_tuple(s):
    s = s.strip("()")
    vals = s.split(', ')
    vals = tuple(map(float, vals))
    return vals

tools = [
    Tool(name="Add", func=add, description="Performs addition of exactly two numbers."),
    Tool(name="Subtract", func=subtract, description="Performs subtraction of exactly two numbers."),
]


### Langchain Definition 

llm = OllamaLLM(model="llama3")

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent_executor.invoke({"input": "What is 3 + 5?"})
print(response)

response = agent_executor.invoke({"input": "What is 10 - 4?"})
print(response)

response = agent_executor.invoke({"input": "What is 5 + 4? Also, what is 99 - 33?"})
print(response)
