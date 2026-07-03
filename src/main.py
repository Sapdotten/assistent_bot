from google import genai
from google.genai import types

client = genai.Client(
    api_key='',
    http_options=types.HttpOptions(
        client_args={'proxy': 'socks5://127.0.0.1:10808'},
        async_client_args={'proxy': 'socks5://127.0.0.1:10808'},
    ),
)

interaction = client.models.generate_content(
    # gemini-3.5-flash пока не существует, проверь актуальное имя модели
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words, my babe"
)
print(interaction.text)
