"""
AWS Bedrock Inference Example (Claude 3 Version)

This script demonstrates how retrieved context from a local RAG pipeline
can be sent to a managed LLM hosted on AWS Bedrock for generation.

NOTE:
- Assumes AWS credentials are configured via IAM / AWS CLI.
- Uses the Claude 3 Messages API format.
"""

import json
import boto3 
import botocore

# 1. Bedrock Client Initialization
# Ensure your AWS CLI is configured with 'aws configure' before running
session = boto3.Session()
bedrock = session.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"  # Change to your specific region
)

# 2. Example RAG Context (Simulated)
retrieved_context = """
Headaches can have many causes, including stress, dehydration, viral infections,
or lack of sleep. In most cases, headaches are temporary and resolve on their own.
Persistent or severe headaches may require professional medical evaluation.
"""

user_query = "I have a severe headache"

# 3. Prompt Construction
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

# 4. Bedrock Invocation (Claude 3 Haiku - fast and cost-effective)
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500,
    "temperature": 0.2,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]
})

try:
    response = bedrock.invoke_model(
        modelId=model_id,
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    # 5. Parsing the response
    response_body = json.loads(response.get("body").read())
    output_text = response_body["content"][0]["text"]

    print("\n" + "="*30)
    print("Generated Response from AWS Bedrock:")
    print("="*30)
    print(output_text)

except botocore.exceptions.ClientError as err:
    print(f"Couldn't invoke Claude 3. Error: {err.response['Error']['Message']}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")