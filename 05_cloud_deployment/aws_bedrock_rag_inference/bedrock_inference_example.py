"""
AWS Bedrock Inference Example 

This script demonstrates how retrieved context from a local RAG pipeline
can be sent to a managed LLM hosted on AWS Bedrock for generation.

NOTE:
- This is a minimal inference-only example.
- Assumes AWS credentials are configured via IAM / AWS CLI.
- No fine-tuning or deployment infrastructure is included.
"""

import json
import boto3

# Bedrock Client Initialization

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"  
)


# Example RAG Context (Simulated)

retrieved_context = """
Headaches can have many causes, including stress, dehydration, viral infections,
or lack of sleep. In most cases, headaches are temporary and resolve on their own.
Persistent or severe headaches may require professional medical evaluation.
"""


user_query = "I have a severe headache"


# Prompt Construction

prompt = f"""
You are a healthcare information assistant.
You are NOT a medical professional.

Use the context below to answer the question.
Do NOT diagnose conditions or recommend treatments.
Use neutral, informational language only.

Context:
{retrieved_context}

Question:
{user_query}

Answer:
"""

# Bedrock Invocation (Example: Anthropic Claude)

response = bedrock.invoke_model(
    modelId="anthropic.claude-v2",
    body=json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 200,
        "temperature": 0.2
    }),
    contentType="application/json",
    accept="application/json"
)
response_body = json.loads(response["body"].read())

print("\nGenerated Response from AWS Bedrock:\n")
print(response_body.get("completion", "No response"))