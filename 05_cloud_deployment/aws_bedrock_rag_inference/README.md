# AWS Bedrock Integration — Cloud Inference Proof

## Overview
This module demonstrates how a locally built Retrieval-Augmented Generation (RAG) system can be integrated with a managed cloud LLM service using AWS Bedrock.

The goal is to validate cloud compatibility and production readiness without deploying a full application.

---

## Architecture
Local RAG Pipeline  
→ Retrieved Context (FAISS)  
→ Prompt Construction  
→ AWS Bedrock (Managed LLM Inference)  
→ Generated Response  

This separation allows retrieval logic to remain local or self-hosted while delegating generation to a scalable cloud service.

---

## Why AWS Bedrock
- Fully managed LLM inference
- Enterprise security and governance
- Model-agnostic API
- Commonly adopted in Fortune-500 GenAI stacks

---

## Scope of This Module
✔ Demonstrates cloud LLM invocation  
✔ Shows prompt + context handoff  
✔ Validates end-to-end RAG compatibility  

✖ Not a full deployment  
✖ No UI or API layer  
✖ No fine-tuning  

This is an intentional **minimal proof of cloud execution**.


# Next Steps
- Wrap inference in a FastAPI endpoint
- Add IAM-secured invocation
- Replace local GPT-2 with Bedrock-hosted models
