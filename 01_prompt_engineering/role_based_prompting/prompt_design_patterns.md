# Prompt Design Patterns

This document outlines prompt design patterns used to control LLM behavior
in production-oriented GenAI systems.

These patterns treat prompts as behavioral control mechanisms, not
just input formatting.



# 1. Role Definition Pattern

Purpose:  
Explicitly define what the model is and is not allowed to do.

Why it matters:
Without a clear role, LLMs tend to overstep authority and hallucinate.
Example:

- Defining the model as a *non-diagnostic healthcare information assistant*
- Explicitly prohibiting diagnosis and treatment advice


## 2. Constraint-First Pattern

Purpose:
State non-negotiable constraints before task instructions.

Why it matters: 
Safety and boundary rules should override task completion.

Example:
- “You must NOT diagnose conditions”
- “You must NOT invent information outside the provided context”


# 3. Context-Grounded Response Pattern

Purpose:
Force the model to rely only on retrieved or provided context.

Why it matters:
Reduces hallucination by limiting reliance on parametric memory.

Example: 
- “Base responses ONLY on the provided context”
- “If context is insufficient, explicitly state that”

---

# 4. Uncertainty Acknowledgment Pattern

Purpose:
Encourage the model to admit uncertainty instead of fabricating answers.

Why it matters:
LLMs default to confident language even when unsure.

Example Phrases:  
- “The available information does not allow for a definitive conclusion”
- “Based on the provided context…”



## 5. Failure-Aware Prompting Pattern

Purpose:  
Design prompts with expected failure modes in mind.

Why it matters: 
Prompt failures are inevitable; planning for them improves reliability.

Example: 
- Clear refusal instructions
- Safe fallback responses
- Escalation guidance

---

## Summary

These prompt patterns are used consistently across the system to improve:
- Safety
- Reliability
- Predictability
- Ease of iteration

Prompts are treated as versioned, testable artifacts**, not one-off text.
