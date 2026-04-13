import chromadb

class VectorStore:
    def __init__(self, collection_name="rfp_docs"):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(collection_name)

    def add_documents(self, chunks, embedding_model):
        for i, chunk in enumerate(chunks):
            embedding = embedding_model.encode(chunk)

            self.collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[str(i)]
            )

    def query(self, pergunta, embedding_model, top_k=5):
        query_embedding = embedding_model.encode(pergunta)

        resultados = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return "\n".join(resultados["documents"][0])