# Safety-Aware Retrieval-Augmented Generation (RAG) System

## Overview
This project implements an end-to-end Retrieval-Augmented Generation (RAG) pipeline designed to demonstrate how large language model (LLM) hallucinations and unsafe behavior can be mitigated through architectural controls rather than relying solely on powerful models.

The system intentionally uses GPT-2, a weaker and non-instruction-tuned model, to highlight how retrieval grounding, rule-based safety checks, and constrained generation can be combined to produce safer, more reliable outputs.



## Problem Statement
Large Language Models can generate fluent but incorrect or unsafe responses, particularly in high-stakes domains such as healthcare. Relying purely on model capability often masks architectural weaknesses and makes systems brittle.

This project explores how to design a robust RAG pipeline that compensates for model limitations through explicit system design.



## System Architecture
1. User submits a query
2. High-risk queries are detected using rule-based safety checks
3. Relevant context is retrieved from authoritative sources using FAISS
4. Retrieved context is passed to the language model
5. GPT-2 is used only for constrained summarization (not reasoning or diagnosis)
6. A neutral, informational response is generated



 Data Sources
- Centers for Disease Control and Prevention (CDC)
- World Health Organization (WHO)

These sources were selected to ensure factual grounding and reduce misinformation risk.



Key Design Decisions

 Why GPT-2?
- Demonstrates system-level safety controls
- Avoids reliance on instruction-following models
- Makes hallucination risks visible and addressable
- Ensures local, reproducible execution

 Safety Controls
- Rule-based detection of high-risk symptoms
- Explicit escalation messaging for severe conditions
- GPT-2 restricted to neutral summarization only
- No diagnosis or treatment recommendations

Retrieval Strategy
- Sentence-transformer embeddings
- FAISS vector store for low-latency retrieval
- Controlled chunking (500 tokens, 50 overlap)


 Limitations
- GPT-2 lacks reasoning and instruction-following capability
- Safety checks are keyword-based, not probabilistic
- No automated quantitative evaluation metrics

Future Improvements
- Replace GPT-2 with instruction-tuned or hosted models (GPT-4, Bedrock)
- Add probabilistic risk classification
- Introduce automated hallucination evaluation
- Deploy as an API-backed service

 Key Takeaway
This project demonstrates that safe and reliable LLM systems are achieved through thoughtful architecture and controls, not model strength alone.
