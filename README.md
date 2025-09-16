# biocypher-mcp

An MCP (Model Context Protocol) server for assisting with BioCypher workflows. This server provides hierarchical tools to help LLM agents create BioCypher adapters for any data source.

## Features

- **Streamable HTTP Transport**: Full MCP protocol support with Server-Sent Events (SSE)
- **Hierarchical Tool Structure**: Navigate through BioCypher workflows with structured guidance
- **BioCypher Adapter Creation Workflow**: Complete 5-phase framework for creating adapters from any data source
- **Adaptive Implementation Process**: Step-by-step guidance for analyzing data sources and implementing appropriate adapter strategies
- **Implementation Patterns**: Reusable patterns for field mapping, conditional extraction, and progressive fallback
- **Decision Guidance**: AI-powered recommendations based on data characteristics

## Quick Start

### Local Development

```bash
# Install dependencies
uv sync

# Run the MCP server with streamable HTTP transport
uv run python -m biocypher_mcp.main

# Or run the web server with REST API endpoints
uv run python -m biocypher_mcp.web_server
```

### Docker Deployment

```bash
# Build and run with docker-compose (production)
docker-compose up -d biocypher-mcp

# Or run development version with hot reload
docker-compose up -d biocypher-mcp-dev

# Check status
docker-compose ps
docker-compose logs biocypher-mcp
```

### MCP Client Configuration

For MCP clients like Cursor, configure the server with:

```json
{
  "mcpServers": {
    "biocypher-mcp": {
      "url": "https://mcp.biocypher.org/",
      "transport": "http"
    }
  }
}
```

## API Endpoints

### MCP Streamable HTTP Transport (main.py)

The primary MCP server provides streamable HTTP transport at the root endpoint:

- `POST /` - MCP protocol endpoint (streamable HTTP with SSE)
- Supports all MCP protocol methods: `initialize`, `tools/list`, `tools/call`, etc.

### REST API Endpoints (web_server.py)

The web server provides REST API endpoints for traditional HTTP clients:

- `GET /` - Root endpoint with API overview
- `GET /workflows` - Available workflows
- `GET /workflows/adapter-creation` - Adapter creation workflow details
- `GET /phases/{phase_number}` - Phase-specific guidance
- `GET /patterns` - Implementation patterns
- `GET /patterns/{pattern_type}` - Specific patterns
- `POST /decision-guidance` - Decision guidance
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation

## Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/biocypher/biocypher-mcp.git
cd biocypher-mcp

# Install development dependencies
uv sync --dev

# Run tests
uv run pytest tests/ -v
```

### Architecture

The project provides two server implementations:

1. **main.py**: MCP streamable HTTP transport server (primary)
   - Uses FastMCP with streamable HTTP transport
   - Mounted at root path (`/`)
   - Designed for MCP clients like Cursor

2. **web_server.py**: REST API server (secondary)
   - Provides traditional REST endpoints
   - Useful for web applications and testing
   - Can run alongside the main server on different ports

## License

MIT
