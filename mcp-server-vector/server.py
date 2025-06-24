# server.py
from mcp.server.fastmcp import FastMCP
from postgres_provider import add_column_to_table, process_embeddings, search_by_similarity
import mcp.types as types
# Create an MCP server
mcp = FastMCP("Demo", port=6274, host="0.0.0.0")


# Adding tools

@mcp.tool()
def health_check(test_string: str) -> int:
    """Health check the MCP server"""
    print(f"Health checking database {test_string}")
    return "OK"

# TODO: WORKSHOP - Implement add_embedding_columns_to_table tool
# This tool should accept: table_name: str, embedding_column_name: str, connection_string: str
# It should add a vector(1536) column to the specified table
# @mcp.tool()
# def add_embedding_columns_to_table(table_name: str, embedding_column_name: str, connection_string: str) -> str:
#     """Add embedding column to a table"""
#     # Implementation goes here
#     pass

# TODO: WORKSHOP - Implement generate_embedding tool  
# This tool should accept: column_name_from: str, column_name_to: str, table_name: str, connection_string: str, openai_api_key: str
# It should generate embeddings for text data using OpenAI's text-embedding-ada-002 model
# @mcp.tool()
# def generate_embedding(column_name_from: str, column_name_to: str, table_name: str, connection_string: str, openai_api_key: str) -> str:
#     """Generate embeddings for table data"""
#     # Implementation goes here
#     pass

# TODO: WORKSHOP - Implement similarity_search tool
# This tool should accept: query: str, table_name: str, embedding_column_name: str, connection_string: str, openai_api_key: str, match_threshold: float
# It should perform vector similarity search using cosine distance
# @mcp.tool()
# def similarity_search(query: str, table_name: str, embedding_column_name: str, connection_string: str, openai_api_key: str, match_threshold: float) -> str:
#     """Search for similar items using vector similarity"""
#     # Implementation goes here
#     pass

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.prompt("Call health_check")
def review_code(test_string: str) -> str:
    return f"Please call the health_check tool:\n\n{test_string}"

# mcp.run()