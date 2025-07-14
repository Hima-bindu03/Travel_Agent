# tourist_guide_bot.py

from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain_core.tools import tool
# from IPython.display import display_markdown  # Only works in Jupyter/IPython

load_dotenv()

@tool
def tourist_guide(city: str) -> str:
    """Extracts the city user is asking about for travel advice and Provides tourist attractions in a specified U.S. city."""
    return f"Here are the tourist attractions in {city}!"

persona = """ 
You are a smart and friendly tourist guide who uses tools to identify which city the user is asking about.

You are allowed to call the `tourist_guide` tool only to extract the name of the city.

Do not rely on the tool for information. Instead, use your own knowledge and experience to generate a helpful, informative response about that city — including tourist attractions, landmarks, and travel tips.

Never return the output of the tool — just use it as a helper to identify the topic.
"""

agent = create_react_agent(
    model="groq:llama-3.1-8b-instant",
    tools=[tourist_guide],
    prompt=persona
)

def my_guide(message):
    out = agent.invoke({"input": message})

    if isinstance(out, dict) and "messages" in out:
        final_response = None
        for msg in reversed(out["messages"]):
            if hasattr(msg, "content") and msg.content.strip():
                final_response = msg.content
                break
        if final_response:
            print(final_response)
        else:
            print("No response found.")
    elif "output" in out:
        print(out["output"])
    elif hasattr(out, "content"):
        print(out.content)
    else:
        print(str(out))


if __name__ == "__main__":
    # Example run
    my_guide(user_input := input("Ask me about a city: Example - Newyork "))
