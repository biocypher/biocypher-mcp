# biocypher-mcp

An MCP (Model Context Protocol) server for assisting with BioCypher workflows. This server provides hierarchical tools to help LLM agents create BioCypher adapters for any data source.

## Features

- **Streamable HTTP Transport**: Full MCP protocol support with Server-Sent Events (SSE)
- **Hierarchical Tool Structure**: Navigate through BioCypher workflows with structured guidance
- **BioCypher Adapter Creation Workflow**: Complete 5-phase framework for creating adapters from any data source
- **Project Creation Guidance**: Verify existing directories and get scripted cookiecutter instructions
- **Adaptive Implementation Process**: Step-by-step guidance for analyzing data sources and implementing appropriate adapter strategies
- **Implementation Patterns**: Reusable patterns for field mapping, conditional extraction, and progressive fallback
- **Decision Guidance**: AI-powered recommendations based on data characteristics

## Quick Start

### Local Development

```bash
# Install dependencies
uv sync

# Run the MCP server (stdio transport by default; pass --transport http for HTTP mode)
uv run python -m biocypher_mcp.main

# Or run the web server with REST API endpoints
uv run python -m biocypher_mcp.web_server
```

#### Using with MCP (Model Context Protocol)

Add the following configuration to your MCP settings (typically `mcp.json`):

**Option 1: Connect to Remote Service** (for use only, not development)

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

**Option 2: Local Development** (using uv)

```json
{
  "mcpServers": {
    "biocypher-mcp": {
      "command": "uv",
      "args": ["run", "python", "-u", "-m", "biocypher_mcp.main"],
      "workingDirectory": "/path/to/biocypher-mcp",
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
```

Replace `/path/to/biocypher-mcp` with the actual path to your cloned repository.

**Option 3: Local Development** (using virtual environment)

```json
{
  "mcpServers": {
    "biocypher-mcp": {
      "command": "/path/to/biocypher-mcp/.venv/bin/python",
      "args": ["-u", "-m", "biocypher_mcp.main"],
      "workingDirectory": "/path/to/biocypher-mcp",
      "env": { "PYTHONUNBUFFERED": "1" }
    }
  }
}
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

## Available Tools

The MCP server provides the following tools:

### Core Workflow Tools
- **`get_available_workflows`** - List all available BioCypher workflows
- **`get_adapter_creation_workflow`** - Get detailed adapter creation workflow
- **`get_phase_guidance`** - Get step-by-step guidance for specific workflow phases
- **`get_implementation_patterns`** - Get reusable implementation patterns
- **`get_decision_guidance`** - Get AI-powered recommendations based on data characteristics

### Project Creation Tools
- **`check_project_exists`** - Show the expected cookiecutter layout and instructions for handling missing projects
- **`get_cookiecutter_instructions`** - Provide scripted, non-interactive cookiecutter commands and defaults

### Configuration Tools
- **`get_schema_configuration_guidance`** - Get guidance on BioCypher schema configuration
- **`get_resource_management_guidance`** - Get guidance on resource management and caching

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
- `POST /project/check` - Validate whether a BioCypher project already exists at a path
- `GET /project/cookiecutter-instructions` - Retrieve scripted cookiecutter guidance
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation

## Usage Examples

### Preparing a BioCypher Project

```python
from biocypher_mcp.main import check_project_exists, get_cookiecutter_instructions

# Inspect the expected cookiecutter layout for your target directory
structure = check_project_exists("/path/to/project")
print(structure["expected_structure"])
print(structure["instruction_if_not_exists"])

# Retrieve scripted cookiecutter instructions and defaults
instructions = get_cookiecutter_instructions()
print(instructions["usage"]["non_interactive_mode"]["command_template"])
```

### Next Steps After Running Cookiecutter

1. Run the printed command (fill in project-specific values) to generate the project
2. Navigate to the new directory and install dependencies (`uv sync` or `poetry install`)
3. Implement your adapter under `src/<package_name>/adapters/`
4. Execute your pipeline, e.g. `python create_knowledge_graph.py`

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
