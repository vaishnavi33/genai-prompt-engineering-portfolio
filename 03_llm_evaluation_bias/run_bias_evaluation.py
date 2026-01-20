from bias_test_cases import test_cases

def simulate_llm_response(prompt):
    """
    Simulated LLM responses to demonstrate bias evaluation.
    In production, this would call an actual LLM API.
    """
    return (
        "Chest discomfort and shortness of breath can be serious symptoms. "
        "It is important to seek medical evaluation, especially if symptoms "
        "are sudden, severe, or worsening."
    )

def run_evaluation():
    results = []

    for case in test_cases:
        response = simulate_llm_response(case["prompt"])

        results.append({
            "demographic": case["demographic"],
            "prompt": case["prompt"],
            "response": response
        })

    return results

if __name__ == "__main__":
    outputs = run_evaluation()

    for o in outputs:
        print("\n---")
        print(f"Demographic: {o['demographic']}")
        print(f"Prompt: {o['prompt']}")
        print(f"Response: {o['response']}")
