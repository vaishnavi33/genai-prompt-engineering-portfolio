Retrieval-Augmented Generation (RAG) System using LangChain + FAISS

Problem Statement
Large Language Models (LLMs) often generate confident but incorrect responses when operating without access to authoritative, up-to-date information. In high-stakes domains such as healthcare, hallucinated responses can be misleading or harmful.

This project implements a Retrieval-Augmented Generation (RAG) pipeline that grounds LLM responses in trusted external knowledge sources, significantly reducing hallucination risk while preserving response quality.


Architecture Overview
The system follows a retrieval-first design pattern:

User Query  
→ Query Embedding Generation  
→ FAISS Vector Similarity Search  
→ Top-K Relevant Document Retrieval  
→ Context Injection into Prompt  
→ LLM Response Generation

This architecture ensures that the LLM reasons over retrieved evidence rather than relying solely on parametric knowledge.


Data Sources
- Centers for Disease Control and Prevention (CDC)
- World Health Organization (WHO)

These sources were selected to ensure authoritative and up-to-date healthcare information.

Chunking Strategy
- Chunk size: 500 tokens  
- Overlap: 50 tokens  

This balances retrieval precision with contextual completeness.

Embeddings
- Model: `sentence-transformers/all-MiniLM-L6-v2`
- Reason: Lightweight, fast, and effective for semantic similarity search.

Vector Store
- FAISS (local vector database)
- Chosen for low-latency retrieval and ease of experimentation.

Key Design Decisions
- Retrieval-First Strategy:** Forces grounding before generation to reduce hallucinations.
- Explicit Chunking Control:** Tuned chunk size and overlap to balance recall and precision.
- Model-Agnostic Design:** Retrieval and generation components are decoupled, enabling future LLM swaps without architectural changes.
- Local Vector Store (FAISS):** Selected for fast experimentation and deterministic behavior during development.


Limitations
- FAISS index is local and not horizontally scalable.
- No reranking or cross-encoder refinement stage.
- Evaluation is qualitative rather than metric-driven in the current version.


Future Improvements
- Migrate vector storage to Pinecone or Weaviate for distributed scalability.
- Introduce reranking models to improve retrieval precision.
- Add automated evaluation metrics for faithfulness and relevance.
- Deploy the pipeline using AWS Bedrock or SageMaker for production inference.

