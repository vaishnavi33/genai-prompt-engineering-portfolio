# GenAI Prompt Engineering & LLM Systems Portfolio

# Overview
This portfolio demonstrates how Large Language Model (LLM) systems can be designed to be reliable, safe, and production-aware through prompt engineering, retrieval-augmented generation (RAG), and explicit evaluation of hallucination risks.

The focus is not on model power alone, but on system design, behavior control, and responsible AI practices .


# Portfolio Structure & Design Philosophy

# 01 — Prompt Engineering (Behavior Control)
 `01_prompt_engineering/`

This section demonstrates how structured prompt engineering is used to control LLM behavior in high-stakes domains such as healthcare.

Key focus areas:
- Role confinement and boundary enforcement
- Safety-aware response design
- Bias avoidance and uncertainty handling

This layer ensures the model does not overstep its intended role.


# 03 — RAG Systems (Grounded Generation)
 `03_rag_systems/rag_langchain_faiss/`

This is the flagship system in the portfolio.

It demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline that grounds LLM responses in authoritative external data (CDC, WHO) using FAISS-based semantic retrieval.

Key focus areas:
- Document ingestion and chunking
- Embedding-based similarity search
- Retrieval-first architecture
- Controlled generation using GPT-2


# 04 — Evaluation & Reliability (Trust & Safety)
 `04_evaluation_and_reliability/hallucination_reduction/`

This section documents how hallucination risks and unsafe behaviors are identified and mitigated through architectural and prompt-level controls.

Key focus areas:
- Hallucination risk analysis
- Rule-based safety escalation
- Qualitative evaluation of outputs
- Transparent documentation of limitations

# Key Takeaway
Safe and reliable GenAI systems are built through **intentional design**, not by relying solely on powerful models.

This portfolio demonstrates how prompt engineering, retrieval grounding, and evaluation-aware thinking work together to produce trustworthy LLM applications.

---

# Cloud Execution Proof (AWS Bedrock)

 `05_cloud_deployment/aws_bedrock_rag_inference/`

This module demonstrates how the local Retrieval-Augmented Generation (RAG) pipeline can be integrated with a managed cloud LLM service using AWS Bedrock.

Key highlights:
- End-to-end RAG context handoff to Bedrock-hosted LLMs
- Safe, constrained prompt construction for healthcare scenarios
- Clean separation between local retrieval and cloud-based generation
- Minimal, inference-only design aligned with enterprise GenAI practices

