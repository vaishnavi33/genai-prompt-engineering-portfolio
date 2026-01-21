Retrieval-Augmented Generation (RAG) System using LangChain + FAISS

Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline designed to reduce hallucinations in Large Language Model (LLM) responses by grounding outputs in authoritative external healthcare data.

The system retrieves relevant context from trusted sources and injects it into the LLM prompt before generation, ensuring responses are evidence-based rather than purely parametric.

---

Problem Statement
Large Language Models often generate confident but incorrect answers when they rely solely on internal training data. This risk is amplified in high-stakes domains such as healthcare.

This project addresses that limitation by combining semantic retrieval with generation, allowing the model to reason over retrieved evidence.

---

## Data Sources
The pipeline retrieves information from authoritative public health sources:
- Centers for Disease Control and Prevention (CDC)
- World Health Organization (WHO)

These sources were selected to ensure reliability and factual grounding.

---

## System Architecture
1. Fetch healthcare-related documents from web sources
2. Clean and preprocess textual content
3. Split documents into overlapping chunks
4. Generate embeddings using a sentence-transformer model
5. Store embeddings in a FAISS vector database
6. Retrieve top-k relevant chunks for a user query
7. Provide retrieved context for grounded response generation

---

## Key Implementation Details
Chunk Size:** 500 tokens  
Chunk Overlap:** 50 tokens  
Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`  
Vector Store:** FAISS (local)

These parameters were chosen to balance retrieval accuracy with contextual completeness.



## Example Query
What should I do if I experience chest discomfort?
