# AI WORKSHOP: Building MCP Servers with Vector Capabilities

<div align="center">
<svg fill="none" viewBox="0 0 69 15" width="200">
    <path fill="currentColor" d="M3 3H0v3h3zm0 3H0v3h3zm3-6H3v3h3zM3 0H0v3h3zm6 9H6v3h3zM6 9H3v3h3zM3 9H0v3h3zm9-6H9v3h3zM9 0H6v3h3zm3 6H9v3h3zm18-3h-3v3h3zm3-3h-3v3h3zm-3 0h-3v3h3zm6 0h-3v3h3zm-3 9h-3v3h3zm3 0h-3v3h3zm3-3h-3v3h3zm6-3h-3v3h3zm6-3h-3v3h3zm-3 0h-3v3h3zm-3 0h-3v3h3zm9 3h-3v3h3zm0 6h-3v3h3zm0-3h-3v3h3zM39 3h-3v3h3zm6 6h-3v3h3zm0-3h-3v3h3zm0 6h-3v3h3zm9 0h-3v3h3zm-15 0h-3v3h3zm0-3h-3v3h3zm-9 0h-3v3h3zm0 3h-3v3h3zm0-6h-3v3h3zM3 12H0v3h3zm15-3h-3v3h3zm42 0h-3v3h3zm3-3h-3v3h3zm3-3h-3v3h3zm3-3h-3v3h3zm-3 9h-3v3h3zm3 3h-3v3h3zm-9 0h-3v3h3zM18 6h-3v3h3zm42 0h-3v3h3zM18 3h-3v3h3zm42 0h-3v3h3zM18 0h-3v3h3zm42 0h-3v3h3zM21 12h-3v3h3zm3 0h-3v3h3z"></path>
</svg>
</div>

## Workshop Overview

This hands-on workshop explores the frontier of AI development, focusing on Large Language Models (LLMs) and the Model Context Protocol (MCP). You'll learn to build sophisticated AI agents with vector database capabilities, implementing real-world applications of semantic search and embedding generation.

## Workshop Agenda

### 📚 **Introduction**
- **Artificial Intelligence Fundamentals**
  - AI's impact across industries (healthcare, finance, law)
  - Machine learning, logic, and perception basics
  - Automation of repetitive and decision-based tasks
  - Predictive modeling and anomaly detection

- **Evolution of Large Language Models**
  - From rule-based systems to transformer architectures
  - Training on massive corpora (Common Crawl, Wikipedia, GitHub)
  - Multilingual, multimodal, and memory-augmented capabilities

### 🤖 **OpenAI & Modern LLMs**
- **OpenAI's Mission**: Ensuring AGI benefits all humanity
- **Key Models**: GPT-3, GPT-4, Codex, DALL·E
- **Impact**: ChatGPT reaching 100M users in 2 months
- **Developer Ecosystem**: APIs powering thousands of applications
- **Research Areas**: Alignment, interpretability, safety, multi-modal models

### ⚡ **LLM Features Deep Dive**

#### **1. Retrieval-Augmented Generation (RAG)**
- Connecting LLMs to external knowledge sources
- Real-time information retrieval for enhanced accuracy
- Reducing hallucination risks
- Applications: Perplexity, Bing Chat, enterprise assistants

#### **2. Function Calling**
- Triggering external APIs and internal functions dynamically
- Structured JSON schemas for function description
- Operational AI: From informative to actionable
- Real-world automation capabilities

#### **3. Vectorization**
- Converting text, images, code into high-dimensional vectors
- Semantic similarity measurement
- Vector databases (Pinecone, Weaviate, Qdrant)
- Intelligent search and recommendations

#### **4. Fine-Tuning**
- Domain-specific model adaptation
- Specialized applications (BloombergGPT, Med-PaLM)
- Supervised and instruction-based training
- Increased accuracy for niche problems

#### **5. Text-to-SQL**
- Natural language to database queries
- Democratizing data access
- Business Intelligence integration
- Prompt-driven analytics

### 🤖 **AI Agents & Model Context Protocol (MCP)**

#### **What are AI Agents?**
AI agents are autonomous software systems that use AI to pursue goals and complete tasks. They demonstrate:

- **Reasoning**: Logic and pattern analysis for informed decisions
- **Acting**: Performing tasks based on decisions and plans
- **Observing**: Gathering environmental information through perception
- **Planning**: Strategic goal achievement with obstacle consideration
- **Collaborating**: Working with humans and other agents
- **Self-refining**: Continuous learning and adaptation

#### **Model Context Protocol (MCP)**
MCP standardizes how applications provide context to LLMs - think "USB-C for AI applications."

**Architecture Components:**
- **MCP Hosts**: Applications like Claude Desktop, IDEs, AI tools
- **MCP Clients**: Protocol clients maintaining 1:1 server connections
- **MCP Servers**: Lightweight programs exposing specific capabilities
- **Data Sources**: Local files, databases, and remote services

## Project Structure

### 🐍 [`mcp-server-vector/`](./mcp-server-vector/)
**Python MCP Server with Vector Database Integration**

Complete implementation featuring:
- Vector column management for PostgreSQL tables
- OpenAI embedding generation and storage
- Semantic similarity search capabilities
- Production-ready error handling and retry logic

**Technologies:**
- Python 3.10+ with FastMCP framework
- PostgreSQL with pgvector extension
- OpenAI Embeddings API
- Docker containerization

### 🔧 [`typescript-mcp/`](./typescript-mcp/)
**TypeScript MCP Client/Server Implementation**

Supporting tools including:
- Code review automation
- MCP client integration examples
- Development and build tools

**Technologies:**
- Node.js 18+ with TypeScript
- MCP TypeScript SDK

## 🎯 Hands-On Challenge

### Workshop Exercise: Implement 3 Vector Tools

You'll implement these MCP tools in the Python server:

#### **1. add_embedding_columns_to_table**
**Parameters:**
- `table_name: str`
- `embedding_column_name: str`
- `connection_string: str`

**Function:** Add a `vector(1536)` column to existing tables

#### **2. generate_embedding**
**Parameters:**
- `column_name_from: str`
- `column_name_to: str`
- `table_name: str`
- `connection_string: str`
- `openai_api_key: str`

**Function:** Generate embeddings using OpenAI's `text-embedding-ada-002` model and store in database

#### **3. similarity_search**
**Parameters:**
- `query: str`
- `table_name: str`
- `embedding_column_name: str`
- `connection_string: str`
- `openai_api_key: str`
- `match_threshold: float` (0.0-1.0)

**Function:** Perform semantic similarity search using vector cosine distance

## 🏆 Competition & Prizes

After completing the hands-on exercises:

### **Submission Requirements**
1. Complete the three MCP tools implementation
2. Zip your code
3. Send to:
   - `andre.gustavo@joinplank.com`
   - `fernando.rocha@joinplank.com`

## Quick Start

### Prerequisites
- **Python**: 3.10 or higher
- **Node.js**: 18.0 or higher  
- **Docker**: 20.0 or higher (with Docker Compose)
- **OpenAI API Key**: Required for embedding generation

### Get Started
```bash
# 1. Start with the Python MCP Server
cd mcp-server-vector
# Follow setup instructions in mcp-server-vector/README.md

# 2. Explore TypeScript tools
cd typescript-mcp
# Follow setup instructions in typescript-mcp/README.md
```

## Learning Objectives

By the end of this workshop, you'll have:

✅ **Built a production-ready MCP server**  
✅ **Implemented vector database operations**  
✅ **Integrated OpenAI embeddings API**  
✅ **Created semantic search capabilities**  
✅ **Understood AI agent architecture**  
✅ **Mastered modern LLM features**  

## Architecture Overview

```
┌─────────────────────┐    ┌─────────────────────┐
│   AI Agent/Client   │───▶│   MCP Server        │
│   (Claude, GPT)     │    │   + Vector Tools    │
└─────────────────────┘    └─────────────────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │   PostgreSQL        │
                           │   + pgvector        │
                           └─────────────────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │   OpenAI API        │
                           │   (Embeddings)      │
                           └─────────────────────┘
```

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)
- [AI Agents Research](https://cloud.google.com/discover/what-are-ai-agents)

## Support

For workshop assistance, refer to:
- Detailed setup guides in each project folder
- TODO comments throughout the codebase
- Workshop instructors for hands-on help

---

<div align="center">

**Ready to build the future of AI?** 🚀  
*Let's create intelligent agents that understand and act!*

*Built with ❤️ by the Plank team*

</div> 