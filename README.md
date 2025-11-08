# biocypher-mcp

An MCP (Model Context Protocol) server for assisting with BioCypher workflows. This server provides hierarchical tools to help LLM agents create BioCypher adapters for any data source.

## Features

- **Hierarchical Tool Structure**: Navigate through BioCypher workflows with structured guidance
- **BioCypher Adapter Creation Workflow**: Complete 5-phase framework for creating adapters from any data source
- **Project Creation Tool**: Generate complete BioCypher projects from templates with Docker support
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

## Available Tools

The MCP server provides the following tools:

### Core Workflow Tools
- **`get_available_workflows`** - List all available BioCypher workflows
- **`get_adapter_creation_workflow`** - Get detailed adapter creation workflow
- **`get_phase_guidance`** - Get step-by-step guidance for specific workflow phases
- **`get_implementation_patterns`** - Get reusable implementation patterns
- **`get_decision_guidance`** - Get AI-powered recommendations based on data characteristics

### Project Creation Tool
- **`create_biocypher_project`** - Create a complete BioCypher project from template. Can create in existing directories, preserving data files in 'data/' subdirectory.

### Configuration Tools
- **`get_schema_configuration_guidance`** - Get guidance on BioCypher schema configuration
- **`get_resource_management_guidance`** - Get guidance on resource management and caching

## API Endpoints

The web server provides the following endpoints:

- `GET /` - Root endpoint with API overview
- `GET /workflows` - Available workflows
- `GET /workflows/adapter-creation` - Adapter creation workflow details
- `GET /phases/{phase_number}` - Phase-specific guidance
- `GET /patterns` - Implementation patterns
- `GET /patterns/{pattern_type}` - Specific patterns
- `POST /decision-guidance` - Decision guidance
- `POST /project/create` - Create a new BioCypher project
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation

## Usage Examples

### Creating a BioCypher Project

```python
# Create a new project
create_biocypher_project(
    project_name="my-protein-project",
    project_description="Project for protein-protein interaction data",
    template_method="cookiecutter",
    target_directory=".",
    include_docker=True,
    include_tests=True,
    adapter_name="protein_interaction_adapter",
    data_source_type="api",
    schema_config=True
)

# Create in existing directory with data files
create_biocypher_project(
    project_name="my-data-project",
    existing_directory_handling="move",  # or "copy" to keep originals
    template_method="cookiecutter",
    data_source_type="file"
)
```

Existing files are preserved in `data/` subdirectory when using `existing_directory_handling="move"` or `"copy"`.

### Next Steps After Project Creation

1. Navigate to your project: `cd my-protein-project`
2. Install dependencies: `uv sync` (or `poetry install`)
3. Implement your adapter: Edit `src/my_protein_project/adapters/protein_interaction_adapter.py`
4. Run the project: `python create_knowledge_graph.py`

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
