from config import AiConfig
from functions.schedule_func import schedule_function
from google import genai
from google.genai import types

ai_config = AiConfig()
client = genai.Client(
    api_key=ai_config.api_key,
    http_options=types.HttpOptions(
        client_args={'proxy': ai_config.proxy},
        async_client_args={'proxy': ai_config.proxy},
    ),
)


interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=(
        "Amigo, remind me to clean my room tomorrow."
        "Today is 19 July 2026. And also remind me tomorrow to wash dishes."
    ),
    tools=[{"type": "function", **schedule_function.model_dump()}],
    system_instruction="You are a cat. Your name is Neko."
)

for step in interaction.steps:
    print(step)
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
