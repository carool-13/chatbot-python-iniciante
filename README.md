# 🌙 Chatbot Interativo — Tech Journey

## Sobre o projeto

Este projeto consiste em um chatbot desenvolvido em Python com funcionamento híbrido:

* Respostas baseadas em regras (if/elif)
* Integração com API da OpenAI
* Tratamento de falhas da API (fallback)

O objetivo é simular um assistente virtual capaz de manter uma conversa básica e evoluir para respostas inteligentes utilizando IA sobre o meu currículo.

---

## Funcionalidades

*  Reconhecimento de saudação
*  Captura de nome do usuário
*  Identificação de idade com Regex
*  Integração com IA (OpenAI)
*  Tratamento de erro quando a API não está disponível

---

## Tecnologias utilizadas

* Python 3.12
* OpenAI API
* Regex (`re`)
* dotenv

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/carool-13/chatbot-openai-python.git
```

2. Acesse a pasta:

```bash
cd chatbot-openai-python
```

3. Crie um arquivo `.env`:

```env
OPENAI_API_KEY=sua_chave_aqui
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute o projeto:

```bash
python src/main.py
```

---

## Segurança

O arquivo `.env` não é versionado para proteger a chave da API.

---

## Decisões técnicas

* Uso de `.strip()` para evitar erros de entrada do usuário
* Regex para identificação de idade
* Estrutura híbrida para evitar chamadas desnecessárias à API
* Tratamento de exceções para garantir funcionamento mesmo sem IA

---

## Melhorias futuras

* Histórico de conversa
* Interface gráfica (Streamlit ou Web)
* Melhor interpretação de linguagem natural
* Deploy do projeto

---

## Autora

Carolyne Cristine
Estudante de Gestão de TI
Interesse em QA e Inteligência Artificial
