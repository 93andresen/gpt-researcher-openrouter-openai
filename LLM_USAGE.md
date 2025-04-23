# Large Language Model Usage in GPT-Researcher

GPT-Researcher utilizes three distinct Large Language Models (LLMs) for different purposes, configurable via environment variables: `FAST_LLM`, `SMART_LLM`, and `STRATEGIC_LLM`. The choice of model for each variable impacts the performance, cost, and capabilities of the research process.

These variables are defined in `gpt_researcher/config/variables/base.py` (lines 9-11) and their default values are set in `gpt_researcher/config/variables/default.py` (lines 7-9). The `gpt_researcher/config/config.py` file handles loading these configurations, including overriding defaults with environment variables (lines 21-22, 28-33).

## FAST_LLM

**Purpose:** This model is used for operations that require speed and are less computationally intensive, such as generating summaries ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) line 23).

**Optimal "Smartness":** For `FAST_LLM`, the optimal model should prioritize speed and cost-effectiveness over advanced reasoning capabilities. A smaller, faster model is generally suitable here. The default configuration uses `openai:gpt-4o-mini` ([`gpt_researcher/config/variables/default.py`](gpt_researcher/config/variables/default.py) line 7), which is described as a model for fast LLM operations ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) line 23).

## SMART_LLM

**Purpose:** This model is designated for more complex and "smart" operations, including generating comprehensive research reports and performing detailed reasoning ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) line 24). It is also noted to have support for longer responses (2k+ words) ([`gpt_researcher/config/variables/default.py`](gpt_researcher/config/variables/default.py) line 8). The multi-agent functionality currently relies solely on the `SMART_LLM` ([`multi_agents/README.md`](multi_agents/README.md) line 11).

**Optimal "Smartness":** The `SMART_LLM` requires a more capable model than the `FAST_LLM`. It should be a model known for its strong reasoning abilities and capacity to handle longer contexts and generate detailed outputs. A medium to large-sized model is typically appropriate. The default configuration uses `openai:gpt-4o-2024-11-20` ([`gpt_researcher/config/variables/default.py`](gpt_researcher/config/variables/default.py) line 8), and the documentation suggests `openai:gpt-4o` as a default ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) line 24).

## STRATEGIC_LLM

**Purpose:** This model is used for strategic tasks, such as generating research plans and overall strategies for the research process ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) line 25).

**Optimal "Smartness":** The `STRATEGIC_LLM` benefits from a model with good planning and strategic thinking capabilities. This might overlap with the requirements for the `SMART_LLM`, and often the same model can be used for both if it possesses sufficient capabilities. A capable model, similar in intelligence to or even more advanced than the `SMART_LLM`, is recommended. The default configuration uses `openai:o3-mini` ([`gpt_researcher/config/variables/default.py`](gpt_researcher/config/variables/default.py) line 9), and the documentation suggests `openai:o1-preview` as a default ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) line 25).

## Making Decisions on Model Selection

When choosing models for these variables, consider the following:

*   **Task Requirements:** Match the model's capabilities to the specific tasks assigned to each LLM type (fast operations, smart reasoning/reporting, strategic planning).
*   **Performance vs. Cost:** Faster, less capable models are generally cheaper. More capable models are often slower and more expensive. Balance the need for performance and intelligence with budget constraints.
*   **Token Limits:** Pay attention to the token limits of the models, especially for `SMART_LLM` which is used for generating potentially long reports ([`gpt_researcher/config/variables/default.py`](gpt_researcher/config/variables/default.py) line 8). The default token limits are defined in `gpt_researcher/config/variables/default.py` (lines 10-12) and mentioned in [`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) (lines 28-30).
*   **Provider Compatibility:** Ensure the chosen models are compatible with the configured LLM provider (e.g., OpenAI, Cohere, Ollama, etc.). The format for setting the environment variables is typically `<provider>:<model_name>` ([`gpt_researcher/config/config.py`](gpt_researcher/config/config.py) lines 160, 168-169). Various examples for different providers are available in [`docs/docs/gpt-researcher/llms/llms.md`](docs/docs/gpt-researcher/llms/llms.md).
*   **Multi-Agent Usage:** If using multi-agent features, ensure the `SMART_LLM` is set to a model capable of handling those tasks, as it is the only LLM used in that context ([`multi_agents/README.md`](multi_agents/README.md) line 11).

By carefully selecting models for `FAST_LLM`, `SMART_LLM`, and `STRATEGIC_LLM` based on their intended use cases, you can optimize the performance and effectiveness of GPT-Researcher for your specific needs. Configuration can be done via environment variables in a `.env` file or by providing a custom config file ([`docs/docs/gpt-researcher/gptr/config.md`](https://docs.gptr.dev/docs/gpt-researcher/gptr/config) lines 45, 55).