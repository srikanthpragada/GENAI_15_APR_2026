# Install groq - pip install langchain-groq
# Login and create key in groq.com 

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import keys 


@tool()
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


# Create the agent with tools
model = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider="groq",
    api_key=keys.GROQKEY
)
tools = [add]

agent = create_agent(model, tools)

human_message = HumanMessage("What is 10 + 20")

# Invoke agent
response = agent.invoke({"messages": [human_message]})

for message in response['messages']:
    message.pretty_print()
