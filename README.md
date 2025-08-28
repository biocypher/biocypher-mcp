# biocypher-mcp

An MCP (Model Context Protocol) server for assisting with BioCypher workflows. This server provides hierarchical tools to help LLM agents create BioCypher adapters for any data source.

## Features

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

# Run the MCP server locally
uv run biocypher-mcp

# Or run the web server locally
uv run python -m biocypher_mcp.web_server
```

### Docker Deployment

```bash
# Build and run with docker-compose
docker-compose up -d biocypher-mcp

# Check status
docker-compose ps
docker-compose logs biocypher-mcp
```

## API Endpoints

The web server provides the following endpoints:

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
git clone https://github.com/slobentanzer/biocypher-mcp.git
cd biocypher-mcp

# Install development dependencies
uv sync --dev

# Run tests
uv run pytest tests/ -v
```

## License

MIT
