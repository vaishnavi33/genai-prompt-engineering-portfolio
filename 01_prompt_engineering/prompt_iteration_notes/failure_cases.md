# Prompt Failure Analysis & Iteration Notes

This document records observed prompt failures and the design changes made to address them.

# Failure Case 1: Overly Authoritative Responses
Issue:
The model produced confident-sounding explanations in ambiguous healthcare queries.

Mitigation:  
- Strengthened role boundaries
- Added explicit uncertainty-handling instructions
- Required summarization of retrieved context instead of free reasoning

---

# Failure Case 2: Hallucination When Context Is Missing
Issue:
When retrieval returned weak or irrelevant context, the model attempted to fill gaps.

Mitigation: 
- Added instructions to acknowledge insufficient information
- Introduced pre-generation checks for empty or low-confidence retrieval

---

# Failure Case 3: Over-Restriction Reducing Helpfulness
**Issue:**  
Excessively strict prompts caused frequent refusals.
 
 Mitigation:
- Separated non-negotiable safety rules from task-level guidance
- Introduced neutral informational fallback responses
