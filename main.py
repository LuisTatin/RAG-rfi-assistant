import pandas as pd

from src.ingestion import extrair_texto_pdf, chunkar_texto
from src.embedding import EmbeddingModel
from src.retrieval import VectorStore
from src.llm import gerar_resposta_llm


def main():
    embedding_model = EmbeddingModel()
    vector_store = VectorStore()

    # Indexação
    arquivos = [
        "QA.pdf",
        "Funcionalidades da Empresa.pdf"
    ]

    for arquivo in arquivos:
        texto = extrair_texto_pdf(arquivo)
        chunks = chunkar_texto(texto, tamanho=800)
        vector_store.add_documents(chunks, embedding_model)

    # Perguntas
    df = pd.read_excel("rfp_input.xlsx")

    situacoes = []
    descricoes = []

    for i, pergunta in enumerate(df["pergunta"]):
        print(f"[{i+1}/{len(df)}] Processando...")

        contexto = vector_store.query(pergunta, embedding_model)
        resultado = gerar_resposta_llm(pergunta, contexto)

        situacoes.append(resultado["situacao"])
        descricoes.append(resultado["descricao"])

    df["situacao"] = situacoes
    df["descricao"] = descricoes

    df.to_excel("rfp_output.xlsx", index=False)
    print("Processo finalizado!")


if __name__ == "__main__":
    main()