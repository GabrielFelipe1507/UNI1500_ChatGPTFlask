import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def gerar_resposta(mensagem_usuario):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": mensagem_usuario}],
        max_tokens=150
    )

    return resposta["choices"][0]["message"]["content"]
