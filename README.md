# biocypher-mcp

An MCP (Model Context Protocol) server for assisting with BioCypher workflows. This server provides resources and tools to help LLM agents create BioCypher adapters for any data source.

## Features

- **BioCypher Adapter Creation Framework**: A comprehensive resource that provides guidance for creating BioCypher adapters from any data source
- **Adaptive Implementation Process**: Step-by-step framework for analyzing data sources and implementing appropriate adapter strategies
- **MCP Resource Support**: Exposes the adapter creation framework as an MCP resource for easy access by LLM agents

## Installation

Install the package with uv:

```bash
uv sync --dev
```

## Usage

### Running the MCP Server

You can run the MCP server:

```bash
uv run biocypher-mcp
```

Or install globally and run:

```bash
uvx biocypher-mcp
```

### Using the BioCypher Adapter Creation Framework

The MCP server exposes the BioCypher Adapter Creation Framework as a resource at:
- **URI**: `https://biocypher.org/resources/adapter-creation-framework`
- **Content URI**: `https://biocypher.org/resources/adapter-creation-framework/content`

This resource provides comprehensive guidance for creating BioCypher adapters, including:

- **Data-First Approach**: Analyze data structure before implementation
- **Schema-Driven Development**: Use schema configuration as contract
- **Adaptive Implementation Process**: 5-phase approach from analysis to maintenance
- **Implementation Patterns**: Field mapping, conditional extraction, progressive fallback
- **Quality Assurance**: Testing strategies and validation frameworks
- **Decision Framework**: When to use different extraction approaches

### Programmatic Usage

```python
from biocypher_mcp.main import (
    get_biocypher_adapter_framework_resource,
    get_biocypher_adapter_framework_content
)

# Get the resource definition
resource = get_biocypher_adapter_framework_resource()

# Get the framework content
content = get_biocypher_adapter_framework_content()
```

## MCP Specification Compliance

This MCP server implements the [Model Context Protocol Resources specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources) and provides:

- **Resource Definition**: Properly structured resource metadata with URI, name, title, description, and MIME type
- **Resource Content**: Markdown-formatted content accessible via the resource URI
- **Annotations**: Resource metadata including audience, priority, and last modified timestamp
- **FastMCP Integration**: Uses the FastMCP framework for efficient resource handling

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
