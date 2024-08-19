def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

import matplotlib.pyplot as plt
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    api_key = api_key,
    max_tokens = 256,
    temperature = 0.1
)

def get_response(file, prompt):
    agent = create_pandas_dataframe_agent(
        llm,
        file,
        verbose= False,
        agent_type= "tool-calling",
        return_intermediate_steps=True,
        allow_dangerous_code=True
    )
    
    response = agent.invoke(prompt)

    return response
