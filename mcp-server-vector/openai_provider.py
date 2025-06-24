import openai

# TODO: WORKSHOP - Update this function to use the modern OpenAI client
# The current implementation uses the old openai library syntax
# Update to use: client = openai.OpenAI(api_key=api_key) and client.embeddings.create()
def generate_embedding(text: str, api_key: str, model: str = "text-embedding-ada-002") -> list:
    """Generate an embedding for the given text using OpenAI's API."""
    openai.api_key = api_key
    response = openai.Embedding.create(
        input=text,
        model=model
    )
    return response['data'][0]['embedding'] 

# TODO: WORKSHOP - Add error handling and retry logic
# Consider implementing:
# 1. Rate limiting handling
# 2. API error handling (network errors, API limits, etc.)
# 3. Input validation (text length limits)
# 4. Batch processing for multiple texts
# 5. Exponential backoff for retries 