# Few-Shot vs Zero-Shot Prompting

This document compares few-shot and zero-shot prompting strategies
based on practical system behavior rather than theoretical accuracy.



# Zero-Shot Prompting

Description: 
The model is given instructions and constraints without examples.

When Used:
- Strong role definition and constraints are present
- Task is well-defined
- Consistency is more important than creativity

Advantages:
- Faster iteration
- Lower token usage
- Easier to maintain and update
- Reduced risk of example leakage or overfitting

Risks: 
- Ambiguous instructions can lead to inconsistent behavior
- Requires very clear role and constraint definitions


# Few-Shot Prompting

Description:
The model is provided with examples demonstrating desired behavior.

When Used:  
- Task behavior is subtle or nuanced
- Output format consistency is critical
- Zero-shot behavior is unstable

Advantages:
- Improves behavioral consistency
- Helps guide tone and structure
- Reduces ambiguity in complex tasks

Risks: 
- Higher token cost
- Risk of overfitting to examples
- Examples may introduce unintended bias


# Design Decision in This System

For this system:
- Zero-shot prompting is used for safety-critical constraints and role definition
- Few-shot prompting is used selectively for response formatting and tone

Safety and boundary rules are never encoded only through examples.



#  Key Takeaway

Few-shot prompting is a behavioral aid , not a safety mechanism.

Safety, role boundaries, and hallucination mitigation must be enforced
through explicit constraints and system-level logic.
