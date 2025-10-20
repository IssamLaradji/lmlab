# llmlab

A simple wrapper for useful Large Model (LM) libraries.

## Libraries

1. **parse_anything**: Parse various file formats (PDF, DOCX, Excel, etc.) and websites into structured text.  
   *Code Path*: [`lmlab/parse_anything.py`](lmlab/parse_anything.py)

2. **prompt_llm**: Unified interface for prompting LLMs across multiple providers (Together, OpenAI, OpenRouter).  
   *Code Path*: [`lmlab/prompt_llm.py`](lmlab/prompt_llm.py)

## Installation

Install the package with `uv`:

```bash
uv pip install -e .
```

## Run

```
python minimal.py -l <library>
```

where <library> can be `parse_anything`
