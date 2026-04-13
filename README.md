# rag-rfi-assistant

AI-powered Retrieval-Augmented Generation (RAG) system for automating RFI/RFP responses using internal enterprise knowledge.

This project showcases the design of an end-to-end data + AI pipeline, combining document ingestion, semantic search, and Large Language Models (LLMs) to generate accurate, contextual, and structured answers grounded in proprietary data.

---

## Problem

RFI (Request for Information) and RFP (Request for Proposal) processes are essential in enterprise sales, yet they present significant operational challenges.

Responding to these requests requires navigating large volumes of internal documentation, relying heavily on subject matter experts, and ensuring consistency across answers.

As organizations scale, this process becomes:

- Inefficient and time-consuming
- Difficult to standardize
- Hard to maintain at scale

The lack of automation leads to slower response times, increased workload for pre-sales teams, and inconsistent outputs.

---

## Solution

This project implements a Retrieval-Augmented Generation (RAG) pipeline that integrates data processing, vector search, and LLM-based generation.

Instead of relying solely on a language model, the system retrieves relevant context from internal documents and uses it to generate grounded responses.

### Key pipeline stages:

- **Document Ingestion**  
  Extraction and preprocessing of unstructured PDF data

- **Text Chunking**  
  Segmentation of documents into smaller units to improve retrieval quality

- **Embedding Generation**  
  Transformation of text chunks into dense vector representations using SentenceTransformers

- **Vector Storage**  
  Storage of embeddings in a vector database (ChromaDB) for efficient similarity search

- **Semantic Retrieval**  
  Query-time retrieval of top-k relevant chunks based on vector similarity

- **LLM Generation**  
  Context-aware answer generation using a local LLM API

- **Structured Output**  
  Standardized JSON responses for downstream consumption

This architecture ensures that responses are consistent, traceable, and grounded in internal knowledge, while reducing hallucinations.

---

## Architecture

The system follows a modular RAG pipeline with clear separation of concerns between data processing, retrieval, and generation layers.

### Pipeline Overview

Documents → Chunking → Embeddings → Vector Store → Retrieval → LLM → Structured Output

### Components

- **Ingestion Layer**
  - Parses and extracts text from PDF documents
  - Prepares raw data for downstream processing

- **Processing Layer**
  - Applies chunking strategy for optimal context windows
  - Handles transformation of unstructured data into model-ready inputs

- **Embedding Layer**
  - Uses SentenceTransformers (`all-MiniLM-L6-v2`)
  - Converts text into high-dimensional vector space

- **Storage Layer**
  - ChromaDB vector store for similarity-based retrieval
  - Enables efficient nearest-neighbor search

- **Retrieval Layer**
  - Performs semantic search using cosine similarity
  - Returns top-k relevant context chunks

- **Generation Layer**
  - Integrates with LLM via API
  - Ensures responses are generated strictly from retrieved context

- **Output Layer**
  - Produces structured JSON output:
    - `situacao`: classification (Sim / Não / Informação não encontrada)
    - `descricao`: explanation

---

## Key Engineering Considerations

- Modular pipeline design for maintainability and extensibility
- Clear separation between data processing, retrieval, and generation
- Use of vector databases for scalable semantic search
- Structured outputs for integration with downstream systems
- Grounded generation to reduce hallucinations

---
