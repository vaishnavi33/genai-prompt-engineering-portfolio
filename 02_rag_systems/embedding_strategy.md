Embedding Strategy for Healthcare RAG

Embedding Model
Sentence transformer embeddings are used to capture semantic meaning in healthcare text.

Chunking Strategy
Chunk size: 300–500 tokens
Overlap: 50 tokens
Rationale: Maintain context while enabling efficient retrieval

Vector Store
FAISS is used for local development and experimentation.

Importance
Embedding and chunking choices directly impact retrieval quality and hallucination risk.
