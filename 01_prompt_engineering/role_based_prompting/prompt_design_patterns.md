Prompt Design Patterns for High-Stakes Domains (Healthcare Case Study)

Overview
Prompt engineering plays a critical role in controlling Large Language Model (LLM) behavior, particularly in high-stakes domains such as healthcare where hallucinations, overconfidence, or biased outputs can cause real harm.

This document presents a set of prompt design patterns used to build a safe, reliable, and bias-aware healthcare information assistant**, focusing on behavior control rather than task performance alone.


Design Goals
The prompt patterns in this project were designed to achieve the following goals:

- Prevent unauthorized medical diagnosis or treatment recommendations
- Reduce hallucinated or speculative responses
- Enforce uncertainty acknowledgement when information is insufficient
- Encourage escalation to professional help for high-risk symptoms
- Avoid demographic or socioeconomic bias in responses


Core Prompt Design Patterns
1. Role Confinement Pattern
The model is explicitly instructed to operate within a narrowly defined role.

Purpose:
Prevent role drift and overreach into medical authority.

Example:
“You are a healthcare information assistant. You are not a medical professional.”

Impact:
Reduces overconfident language and discourages diagnostic statements.