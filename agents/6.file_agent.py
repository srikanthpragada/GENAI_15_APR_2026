from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
import keys
from langchain_core.tools import tool

@tool()
def read_file(filename : str) -> str | None:
    """Reads contents of the file and returns a string. If file is not found then returns None.

    Args:
        filename : str
    """
    try:
         with open(filename, "rt") as f:
            return f.read()
    except:
        return None
    


# Create the agent with tools
model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    api_key=keys.GROQKEY
)
tools = [read_file]

agent = create_agent(model, tools)

system_message = SystemMessage(
    "You are an assistant that MUST use tools when needed. "
    "When you call a tool, you MUST use its returned result in your final answer. "
    "Do not ignore tool outputs. Return the exact content from the tool when asked to read files."
)

human_message = HumanMessage("Show me contents of names.txt")

# Invoke agent
response = agent.invoke({"messages": [system_message, human_message]})

for message in response['messages']:
    message.pretty_print()
