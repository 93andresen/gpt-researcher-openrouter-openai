# Using OpenRouter for LLMs and OpenAI for Embeddings

This guide explains how to configure GPT Researcher to use:
- **OpenRouter API** for LLM inference (to access Gemini, Claude, and other models at lower costs)
- **OpenAI API** for embeddings (to maintain high-quality vector embeddings)

## How It Works

We've created a custom solution that allows GPT Researcher to use different API providers for different functions:

1. **New Embedding Provider**: Added a new `openrouter_openai` embedding provider that specifically uses OpenAI's API for embeddings while the main OpenAI configuration points to OpenRouter.

2. **Separate API Configurations**:
   - Main `OPENAI_BASE_URL` points to OpenRouter for LLM calls
   - New `OPENAI_EMBEDDINGS_BASE_URL` points to OpenAI for embeddings
   - Main `OPENAI_API_KEY` contains the OpenRouter key
   - New `OPENAI_EMBEDDINGS_API_KEY` contains the OpenAI key

## Configuration Steps

### 1. Update your .env file

```bash
# OpenRouter Configuration for LLMs
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=sk-or-v1-your-openrouter-key

# OpenAI Configuration for Embeddings
OPENAI_EMBEDDINGS_API_KEY=sk-your-openai-key
OPENAI_EMBEDDINGS_BASE_URL=https://api.openai.com/v1

# Set embedding to use our special provider
EMBEDDING="openrouter_openai:text-embedding-3-small"

# Set models through OpenRouter
# Using the OpenRouter prefix format for models
FAST_LLM="openai:google/gemini-2.0-flash-001"
SMART_LLM="openai:anthropic/claude-3.7-sonnet"
STRATEGIC_LLM="openai:anthropic/claude-3.7-sonnet"
```

### 2. Verify Configuration

You can run the test script to verify your configuration is working correctly:

```bash
cd tests
python test-openrouter-openai.py
```

## Benefits of This Approach

1. **No Core Code Modifications**: Works without changing the core GPT Researcher code
2. **Future-Proof**: Uses existing extension points that are unlikely to be removed
3. **Easily Reversible**: Can switch back to other configurations by changing env vars
4. **Compatible with LM Studio**: The original "custom" provider remains untouched
5. **Maintainable**: Changes are isolated and well-documented

## Switching Between Configurations

### To use OpenRouter + OpenAI:
```
EMBEDDING="openrouter_openai:text-embedding-3-small"
```

### To use LM Studio:
```
EMBEDDING="custom:your-embedding-model"
```

### To use OpenAI for everything:
```
EMBEDDING="openai:text-embedding-3-small"
OPENAI_BASE_URL=https://api.openai.com/v1
```

## Troubleshooting

If you encounter issues:

1. **Check API Keys**: Ensure both your OpenRouter and OpenAI API keys are valid
2. **Check Base URLs**: Make sure the base URLs are correct
3. **Check Model Names**: Ensure you're using model names that are supported by each provider
4. **Check Environment Variables**: Make sure all environment variables are set correctly