import os
import dotenv
import argparse
import lmlab

dotenv.load_dotenv()


# suppress warnings
import warnings

warnings.filterwarnings("ignore")

# import libraries
import argparse
from together import Together
import textwrap


## FUNCTION 1: This Allows Us to Prompt the AI MODEL
# -------------------------------------------------

## PROMPT LLM FUNCTION:
# ---------------------
import together
import dotenv

# load .env file
dotenv.load_dotenv()


def prompt_llm(prompt):
    # model
    model = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

    # together client
    client = together.Together(api_key=os.getenv("TOGETHER_API_KEY"))

    # Make the API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    output = response.choices[0].message.content

    return output


response = prompt_llm("what are the tourist attractions in morocco?")
print(response)

ewrerwer
if __name__ == "__main__":
    # args on which to run the script
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--api_key", type=str, default=None)
    args = parser.parse_args()

    # Get Client for your LLMs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lib", "-l", type=str, default="parse_anything")
    args = parser.parse_args()

    if args.lib == "prompt_llm":
        LLM = lmlab.prompt_llm.LM(
            model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", provider="together"
        )
        response = LLM.prompt_llm("What is the capital of France?")
        print(response)
    elif args.lib == "parse_anything":
        parser = lmlab.parse_anything.ParseAnything()
        print(parser.parse_website("https://www.google.com"))
        print(parser.parse_file("sample_data/compliance-report-ev.pdf"))
    else:
        print("Invalid tool")
