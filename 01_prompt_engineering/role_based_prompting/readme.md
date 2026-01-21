# Role-Based Prompt Engineering for Healthcare Applications

# Overview
This module demonstrates how structured prompt engineering can be used to control Large Language Model (LLM) behavior in high-stakes domains such as healthcare.

Rather than relying on model capability alone, this approach enforces explicit role boundaries, safety constraints, and bias-aware response behavior through prompt design.

## Design Goals
The prompt was designed to:
- Prevent unauthorized medical diagnosis or treatment
- Reduce hallucinated or speculative responses
- Encourage uncertainty acknowledgement when information is insufficient
- Avoid demographic or socioeconomic bias
- Promote responsible escalation for severe symptoms


# Key Prompt Engineering Techniques

# Role Confinement
The model is explicitly instructed to act as a healthcare information assistant, not a medical professional.  
This prevents role drift and overconfident responses.

# Explicit Constraints
Clear prohibitions (diagnosis, treatment, emergency advice) are embedded directly in the prompt to ensure consistent safety behavior.

# Uncertainty Handling
The prompt instructs the model to acknowledge uncertainty rather than fabricate answers.

# Bias Avoidance
The prompt explicitly forbids assumptions about user demographics, encouraging fair and inclusive responses.


# Why This Matters
In real-world LLM systems, many failures are caused by insufficient behavioral constraints rather than model limitations.

This module demonstrates how prompt engineering functions as a control mechanism, not merely a formatting exercise.
