# suppress warnings
import warnings

warnings.filterwarnings("ignore")

# import libraries
import requests, os
import textwrap
import tiktoken
import json
from pathlib import Path
import re


class LM:
    def __init__(
        self, model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", provider="together"
    ):
        self.model = model
        self.total_cost = 0

        # Load model costs
        costs_file = Path(__file__).parent / "model_costs.json"
        with open(costs_file) as f:
            self.model_costs = json.load(f)

        # Initialize tiktoken encoder
        try:
            self.encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")
        except:
            self.encoder = tiktoken.get_encoding("cl100k_base")

        if provider == "together":
            import together

            self.client = together.Together(api_key=os.getenv("TOGETHER_API_KEY"))
        elif provider == "openai":
            import openai

            self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        elif provider == "openrouter":
            import openrouter

            self.client = openrouter.OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))

    def parse_xml_tags(self, text, tags):
        """Parse specified XML tags from text and verify all tags are present."""
        result = {}
        missing = []
        for tag in tags:
            match = re.search(f"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
            if match:
                result[tag] = match.group(1).strip()
            else:
                missing.append(tag)
        if missing:
            raise ValueError(f"Missing tags: {', '.join(missing)}")
        return result

    def prompt_llm(self, prompt, get_structured_output=None):
        # Count input tokens
        input_tokens = len(self.encoder.encode(prompt))

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        output = response.choices[0].message.content

        # Count output tokens
        output_tokens = len(self.encoder.encode(output))

        # Calculate cost
        if self.model in self.model_costs:
            cost = (
                input_tokens
                * self.model_costs[self.model]["input_cost_per_1m"]
                / 1_000_000
                + output_tokens
                * self.model_costs[self.model]["output_cost_per_1m"]
                / 1_000_000
            )
            self.total_cost += cost
            print(
                f"Tokens: {input_tokens} in, {output_tokens} out | Cost: ${cost:.6f} | Total: ${self.total_cost:.6f}"
            )

        if get_structured_output:
            return self.parse_xml_tags(output, get_structured_output)
        return output


if __name__ == "__main__":
    ### Task 1: YOUR CODE HERE - Write a prompt for the LLM to respond to the user
    prompt = """
    what are the tourist attractions in morocco?
    
    Instructions:
    - 10 words max
    """

    # Get Response
    LLM = LM(model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", provider="together")
    response = LLM.prompt_llm(prompt)

    print("\nResponse:\n")
    print(response)
    print("-" * 100)

    # save response under results/
    with open("results/response.txt", "w") as f:
        f.write(response)
