# MCP Vector Server Setup Guide

This guide explains how to set up and run the MCP (Model Context Protocol) vector server with PostgreSQL and OpenAI integration.

## Prerequisites

### Required Tools
- **Python**: 3.10 or higher
- **Docker**: 20.0 or higher (with Docker Compose)
- **Node.js**: 18.0 or higher (for MCP client integration)
- **OpenAI API Key**: Required for embedding generation

## Setup Instructions

### 1. Install UV Package Manager

UV is a fast Python package manager that handles dependencies and virtual environments.

```bash
# Install UV using pip
pip install uv
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root or export the variables:

```bash
# OpenAI API Key (required for embedding generation)
export OPENAI_API_KEY="your-openai-api-key-here"
```

### 3. Start PostgreSQL with Vector Extension

The project includes a `docker-compose.yaml` file that sets up PostgreSQL with the `pgvector` extension and initializes the database.

#### Step-by-step Docker Compose Instructions:

1. **Ensure Docker is running**:
   ```bash
   # Check if Docker is running
   docker --version
   docker compose --version
   ```

2. **Navigate to the project directory**:
   ```bash
   # Make sure you're in the mcp-server-vector directory
   cd mcp-server-vector
   ```

3. **Start the services**:
   ```bash
   # Start PostgreSQL container with vector extensions
   docker compose up -d
   ```

4. **Verify the container is running**:
   ```bash
   # Check if postgres container is running
   docker compose ps
   
   # Or check all running containers
   docker ps
   ```

5. **Check container logs** (optional):
   ```bash
   # View postgres logs to ensure proper startup
   docker compose logs postgres
   ```

6. **Stop the services** (when needed):
   ```bash
   # Stop all services
   docker compose down
   
   # Stop and remove volumes (deletes data)
   docker compose down -v
   ```

This will start PostgreSQL on port `5433` with:
- Database: `postgres`
- Username: `postgres` 
- Password: `postgres`
- Vector extension enabled
- Auto-initialization from `sql/prompts.sql`

### 4. Install Dependencies

```bash
# Install all dependencies using uv
uv sync
```

### 5. Run the MCP Server

```bash
# Start the server in development mode
uv run mcp dev server.py
```

The server will start on `http://0.0.0.0:6274`

**Important**: When the server starts, it will generate an authentication token and display a link in the console. You **must** open this link in your browser to authenticate and enable the MCP connection. Look for output similar to:
```
🔗 Click here to authenticate: http://localhost:6274/auth?token=your-auth-token
```

## Connection Details

### PostgreSQL Connection String
```
postgres://postgres:postgres@localhost:5433/postgres
```

### Server Configuration
- **Host**: `0.0.0.0`
- **Port**: `6274`
- **Protocol**: HTTP with MCP

## Available Tools (Current)

### health_check
- **Purpose**: Verify server connectivity
- **Parameters**: `test_string: str`
- **Returns**: "OK" status

## Workshop: Adding Vector Tools

During the workshop, you'll implement 3 new tools for vector operations:

### add_embedding_columns_to_table
- **Parameters**: 
  - `table_name: str`
  - `embedding_column_name: str` 
  - `connection_string: str`
- **Function**: Adds a vector(1536) column to an existing table

### generate_embedding
- **Parameters**:
  - `column_name_from: str`
  - `column_name_to: str`
  - `table_name: str`
  - `connection_string: str`
  - `openai_api_key: str`
- **Function**: Generates embeddings for text data using OpenAI's text-embedding-ada-002

### similarity_search
- **Parameters**:
  - `query: str`
  - `table_name: str`
  - `embedding_column_name: str`
  - `connection_string: str`
  - `openai_api_key: str`
  - `match_threshold: float` (0.0-1.0)
- **Function**: Performs vector similarity search using cosine distance

## Development Commands

```bash
# Install dependencies
uv sync

# Run server in development mode
uv run mcp dev server.py

# Run with auto-reload
uv run uvicorn server:app --reload --host 0.0.0.0 --port 6274

# Install additional packages
uv add package-name

# Type checking
uv run pyright

# Linting
uv run ruff check
```

## Database Configuration

The project uses `docker-compose.yaml` to automatically set up PostgreSQL with pgvector extension. The database configuration includes:

- **Image**: `ankane/pgvector` (PostgreSQL with vector extensions)
- **Port**: `5433` (mapped from container port 5432)
- **Auto-initialization**: Scripts in `sql/` directory are automatically executed
- **Persistent storage**: Data persisted in `pgdata3` volume

### Adding Custom Tables
To add custom tables or initialization data, create SQL files in the `sql/` directory. They will be automatically executed when the container starts for the first time.

## Troubleshooting

### Common Issues

**PostgreSQL Connection Failed**
- Ensure Docker is running: `docker ps`
- Check container logs: `docker compose logs`
- Verify port 5433 is not in use: `lsof -i :5433`

**OpenAI API Errors**
- Verify API key is set: `echo $OPENAI_API_KEY`
- Check API key permissions and usage limits
- Ensure internet connectivity

**MCP Server Won't Start**
- Check Python version: `python --version` (must be 3.10+)
- Verify all dependencies: `uv sync`
- Check for port conflicts: `lsof -i :6274`

**Vector Extension Missing**
```sql
-- Enable pgvector extension manually if needed
CREATE EXTENSION IF NOT EXISTS vector;
```

### Development Tips

- Use `uv run mcp dev server.py` for auto-reload during development
- Check server logs for debugging information
- Test tools individually before integration
- Monitor PostgreSQL logs: `docker compose logs postgres`

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings)
- [UV Package Manager](https://github.com/astral-sh/uv)

## Contact

For support or contributions, please refer to the workshop materials or contact your instructor.