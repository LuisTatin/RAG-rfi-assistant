🇧🇷 Versão em Português (README.md)

# 🧠 RAG RFI Assistant: Automação de RFPs Corporativas com IA Generativa Local

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-FF4F00?logo=chroma)
![Ollama](https://img.shields.io/badge/LLM-Ollama_(Llama_3)-black?logo=ollama)
![SentenceTransformers](https://img.shields.io/badge/Embeddings-Sentence_Transformers-F7931E)
![Privacy](https://img.shields.io/badge/Data_Privacy-100%25_Local-success)

Este repositório apresenta o design e a implementação de um pipeline **Retrieval-Augmented Generation (RAG)** construído do zero, focado em automatizar a resposta a formulários RFI (Request for Information) e RFP (Request for Proposal).

Diferente de soluções baseadas em APIs em nuvem, este sistema processa bases de conhecimento internas e gera respostas estruturadas utilizando modelos abertos rodando localmente, garantindo zero vazamento de dados sensíveis da empresa.

---

## 📌 Project Overview (Visão de Negócio)

* **Problem Statement:** Responder a RFPs e RFIs é um processo inerentemente manual, que exige a navegação por dezenas de PDFs de documentação técnica, sobrecarregando a equipa de Pré-Vendas (Sales Engineering) e gerando respostas inconsistentes ao longo do tempo.
* **Value Proposition:** O assistente ingere a base de conhecimento proprietária da empresa e, dado um questionário Excel do cliente, pesquisa o contexto exato e elabora respostas precisas com um LLM, classificando o atendimento aos requisitos. 
* **KPIs de Sucesso Impactados:**
  * Redução no *Turnaround Time* (tempo de resposta) de dias para minutos.
  * Redução da carga operacional de Subject Matter Experts (SMEs).
  * Aumento na taxa de ganho (Win Rate) devido a propostas mais consistentes e ágeis.

---

## 🏗️ Architecture & Engineering

A arquitetura adota um design "Framework-less", evitando abstrações complexas (como LangChain) para demonstrar domínio absoluto sobre os mecanismos de vetorização, recuperação e engenharia de prompts.

### 1. Ingestion & Embedding Pipeline
* **Extração:** Leitura e extração de texto bruto de PDFs utilizando `PyPDF`.
* **Chunking:** Segmentação do texto em partes menores para otimizar a janela de contexto do LLM.
* **Vetorização:** Utilização de `SentenceTransformers` (`all-MiniLM-L6-v2`) para mapear chunks de texto para um espaço vetorial denso de alta dimensionalidade.
* **Vector Store:** Indexação e armazenamento de embeddings localmente através do `ChromaDB`, preparado para busca por Similaridade de Cossenos (Top-K).

### 2. Retrieval & Generation (RAG)
* O sistema cruza as perguntas vindas do ficheiro Excel com a base do ChromaDB para obter a verdade terrestre (Ground Truth).
* **LLM Engine:** Integração com um serviço local (`Ollama` + `Llama 3`), operando inteiramente em `localhost` para mitigar riscos de partilha de Propriedade Intelectual (IP).
* **Prompt Engineering:** Instruções rígidas para mitigar *hallucinations*, forçando o LLM a declarar "Informação não encontrada" caso o contexto seja insuficiente.

### 3. Structured Output Parsing
* O output do LLM é constrangido a devolver sempre um formato JSON rigoroso (`{"situacao": "...", "descricao": "..."}`), permitindo parsing automatizado e exportação direta para um novo ficheiro Excel preenchido.

---

## 🚀 Get Started (Quick Start)

### Pré-requisitos
* Python 3.10+
* Servidor do [Ollama](https://ollama.com/) instalado e rodando com o modelo Llama 3 (`ollama run llama3`).

### Execução em 3 Passos
1. **Instalar Dependências:**
```bash
pip install -r requirements.txt
```

2. **Preparar Inputs:**
* Coloca os teus PDFs corporativos na raiz do projeto (ex: `QA.pdf`).
* Preenche o arquivo `rfp_input.xlsx` com a coluna `pergunta`.

3. **Rodar o Pipeline End-to-End:**
```bash
python main.py
```
*(O sistema irá gerar um `rfp_output.xlsx` com as respostas estruturadas baseadas exclusivamente nos teus PDFs)*.

---

## 🛣️ Future Work (Roadmap)

Embora o pipeline atual prove o conceito E2E de forma sólida, as próximas otimizações de nível de produção incluem:
1. **Semantic/Recursive Chunking:** Substituir o corte fixo de caracteres por `RecursiveCharacterTextSplitter` ou chunking semântico para não quebrar sentenças a meio.
2. **Re-ranking Pipeline:** Adicionar um Cross-Encoder (ex: Cohere Rerank) após a pesquisa do ChromaDB para reordenar os documentos recuperados por relevância profunda, melhorando a precisão sem aumentar o tamanho do prompt.
3. **Métricas de Avaliação (Ragas):** Implementar frameworks de avaliação (Answer Relevancy, Context Precision) para monitorizar a degradação do pipeline.

---
**Desenvolvido por Luis Tatin**

#🧠 RAG RFI Assistant: Local GenAI Automation for Enterprise RFPs

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-FF4F00?logo=chroma)
![Ollama](https://img.shields.io/badge/LLM-Ollama_(Llama_3)-black?logo=ollama)
![SentenceTransformers](https://img.shields.io/badge/Embeddings-Sentence_Transformers-F7931E)
![Privacy](https://img.shields.io/badge/Data_Privacy-100%25_Local-success)

This repository presents the design and implementation of an end-to-end **Retrieval-Augmented Generation (RAG)** pipeline built from scratch, aimed at automating responses to RFI (Request for Information) and RFP (Request for Proposal) questionnaires.

Unlike cloud-API-based solutions, this system processes internal knowledge bases and generates structured responses using open-weight models running locally, ensuring zero leakage of sensitive corporate data.

---

## 📌 Project Overview (Business Vision)

* **Problem Statement:** Answering RFPs and RFIs is an inherently manual process requiring navigation through dozens of technical PDFs. This overburdens the Pre-sales (Sales Engineering) team and often leads to inconsistent responses over time.
* **Value Proposition:** The assistant ingests the company's proprietary knowledge base and, given an Excel questionnaire from a client, queries the exact context and crafts precise answers using an LLM, classifying compliance with requirements. 
* **Impacted Success KPIs:**
  * Reduction in Turnaround Time from days to minutes.
  * Decreased operational workload for Subject Matter Experts (SMEs).
  * Increased Win Rate due to highly consistent and agile proposals.

---

## 🏗️ Architecture & Engineering

The architecture adopts a "Framework-less" design, explicitly avoiding complex abstractions (like LangChain) to demonstrate absolute mastery over the underlying mechanics of vectorization, retrieval, and prompt engineering.

### 1. Ingestion & Embedding Pipeline
* **Extraction:** Reading and extracting raw text from PDFs using `PyPDF`.
* **Chunking:** Slicing text into smaller chunks to optimize the LLM's context window.
* **Vectorization:** Utilizing `SentenceTransformers` (`all-MiniLM-L6-v2`) to map text chunks into a high-dimensional dense vector space.
* **Vector Store:** Local indexing and storage of embeddings via `ChromaDB`, primed for Cosine Similarity search (Top-K).

### 2. Retrieval & Generation (RAG)
* The system cross-references incoming Excel queries with the ChromaDB database to retrieve the ground truth context.
* **LLM Engine:** Seamless integration with a local service (`Ollama` + `Llama 3`), operating entirely on `localhost` to mitigate Intellectual Property (IP) sharing risks.
* **Prompt Engineering:** Strict system instructions are in place to mitigate hallucinations, forcing the LLM to declare "Information not found" if the retrieved context is insufficient.

### 3. Structured Output Parsing
* The LLM's output is heavily constrained to always return a strict JSON format (`{"situacao": "...", "descricao": "..."}`), enabling automated parsing and direct export into a newly populated Excel file.

---

## 🚀 Get Started (Quick Start)

### Prerequisites
* Python 3.10+
* [Ollama](https://ollama.com/) server installed and running with the Llama 3 model (`ollama run llama3`).

### 3-Step Execution
1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Prepare Inputs:**
* Place your corporate PDFs in the project root (e.g., `QA.pdf`).
* Fill the `rfp_input.xlsx` file with the target questions under the `pergunta` column.

3. **Run the End-to-End Pipeline:**
```bash
python main.py
```
*(The system will generate an `rfp_output.xlsx` containing structured answers based exclusively on your PDFs)*.

---

## 🛣️ Future Work (Roadmap)

While the current pipeline solidly proves the E2E concept, upcoming production-grade optimizations include:
1. **Semantic/Recursive Chunking:** Replacing the fixed character split with a `RecursiveCharacterTextSplitter` or semantic chunking to avoid breaking sentences mid-way.
2. **Re-ranking Pipeline:** Integrating a Cross-Encoder (e.g., Cohere Rerank) post-retrieval to reorder the fetched documents by deep semantic relevance, thereby improving accuracy without bloating the prompt window.
3. **Evaluation Metrics (Ragas):** Implementing evaluation frameworks (Answer Relevancy, Context Precision) to continuously monitor pipeline degradation.

---
**Developed by Luis Tatin**
