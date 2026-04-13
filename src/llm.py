import requests
import json

def gerar_resposta_llm(pergunta, contexto):
    prompt = f"""
    Você é um engenheiro de soluções da Empresa.

    Responda SEMPRE em JSON válido:

    {{
        "situacao": "Sim | Não | Informação não encontrada",
        "descricao": "explicação"
    }}

    REGRAS:

    1. Classificação:
    - "Sim" → quando houver evidência direta OU fortemente indicativa
    - "Não" → quando houver evidência clara de ausência
    - "Informação não encontrada" → quando não houver evidência suficiente

    2. Interpretação:
    - Considere equivalências técnicas
    - Considere descrições indiretas claras
    - NÃO invente funcionalidades

    3. Estilo:
    - Fale como parte da Empresa
    - Use: "nosso produto", "nossa plataforma"
    - Tom profissional de pré-vendas

    4. Proibição:
    - NÃO inventar
    - NÃO extrapolar além do contexto
    - NÃO responder a questão com informações genéricas

    5. Se não houver evidência suficiente:
    - Use "Informação não encontrada"
    - Explique brevemente

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """



    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
            "temperature": 0.2
        }
    )

    texto = response.json()["response"]

    try:
        json_inicio = texto.find("{")
        json_fim = texto.rfind("}") + 1
        json_str = texto[json_inicio:json_fim]

        return json.loads(json_str)

    except:
        return {
            "situacao": "Erro",
            "descricao": texto
        }