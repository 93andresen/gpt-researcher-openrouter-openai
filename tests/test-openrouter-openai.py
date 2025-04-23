# This file is only kept in the git history for potential future reference but is intended to be deleted immediately after the initial commit to this fork.
import os
import asyncio
import sys

# Add the project root to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gpt_researcher.config.config import Config
from gpt_researcher.memory.embeddings import Memory

async def test_configuration():
    """
    Test that our configuration correctly uses OpenAI for embeddings
    while keeping OpenRouter for LLMs.

    This function loads the configuration, prints relevant environment variables,
    and attempts to generate embeddings using the configured provider and model
    to verify the setup.
    """
    print("\n=== Testing OpenRouter + OpenAI Configuration ===\n")

    # Load configuration from environment variables or default settings
    cfg = Config()

    # Print current configuration settings relevant to the test
    print("Current configuration:")
    print(f"OPENAI_BASE_URL: {os.environ.get('OPENAI_BASE_URL')}")
    print(f"OPENAI_EMBEDDINGS_BASE_URL: {os.environ.get('OPENAI_EMBEDDINGS_BASE_URL')}")
    print(f"EMBEDDING: {os.environ.get('EMBEDDING')}")
    print(f"FAST_LLM: {os.environ.get('FAST_LLM')}")
    print(f"SMART_LLM: {os.environ.get('SMART_LLM')}")

    # Test embeddings functionality
    try:
        # Create Memory instance with the configured embedding provider and model
        memory = Memory(
            embedding_provider=cfg.embedding_provider,
            model=cfg.embedding_model
        )

        # Get the embeddings object from the Memory instance
        embeddings = memory.get_embeddings()

        # Define a simple text string to test the embedding generation
        test_text = "This is a test sentence to verify embeddings are working correctly."
        # Generate the embedding vector for the test text
        embedding_vector = embeddings.embed_query(test_text)

        # Report success and details about the generated embedding
        print(f"\n✅ SUCCESS: Generated embeddings using provider: {cfg.embedding_provider}")
        print(f"Model: {cfg.embedding_model}")
        print(f"Embedding vector length: {len(embedding_vector)}")
        print(f"First few values: {embedding_vector[:3]}")

    except Exception as e:
        # Report any errors encountered during the embedding test
        print(f"\n❌ ERROR testing embeddings: {e}")
        # Print the full traceback for debugging
        import traceback
        traceback.print_exc()

    print("\n=== Test Complete ===")

# Standard Python entry point to run the async test function
if __name__ == "__main__":
    asyncio.run(test_configuration())