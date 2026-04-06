from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

nome = ""
idade = ""

while True:
    mensagem = input("Você: ").lower()

    if "oi" in mensagem:
        if nome:
            print(f"Bot: Oi {nome}! Tudo bem?")
        else:
            print("Bot: Oi! Tudo bem?")
        
    elif "meu nome é" in mensagem:
        nome = mensagem.replace("meu nome é", "").strip()
        print(f"Bot: Prazer em te conhecer, {nome}!Qual é a sua idade?")
        
    elif "tenho" in mensagem and "anos" in mensagem:
        idade = mensagem.replace("tenho", "").replace("anos", "").strip()
        print(f"Bot: Nossa, apenas {idade} anos. Fico feliz que você seja tão jovem ainda! O que você deseja saber?")
        
    elif "tchau" in mensagem:
        print("Bot: Até mais!")
        break
        
else:
    # construção de IA no projeto (API nova)

    contexto = f"""
Você é um assistente virtual que representa Carolyne Cristine.

Informações:
- Estudante de Gestão de TI (conclusão em 2027)
- Especialista em Atendimento ao Correntista
- Interesse em QA e Inteligência Artificial

Responda de forma clara, profissional e amigável.
Se o usuário já informou o nome, use ele: {nome}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=contexto + f"\nUsuário: {mensagem}"
    )

    print("Bot:", response.output_text)