from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Diga apenas: API funcionando"
)

print(response.output_text)