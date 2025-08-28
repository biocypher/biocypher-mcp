# biocypher-mcp

An MCP (Model Context Protocol) server for assisting with BioCypher workflows. This server provides hierarchical tools to help LLM agents create BioCypher adapters for any data source.

## Features

- **Hierarchical Tool Structure**: Navigate through BioCypher workflows with structured guidance
- **BioCypher Adapter Creation Workflow**: Complete 5-phase framework for creating adapters from any data source
- **Adaptive Implementation Process**: Step-by-step guidance for analyzing data sources and implementing appropriate adapter strategies
- **Implementation Patterns**: Reusable patterns for field mapping, conditional extraction, and progressive fallback
- **Decision Guidance**: AI-powered recommendations based on data characteristics

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

### Using the BioCypher Tools

The MCP server provides a hierarchical set of tools for BioCypher workflows:

#### 1. Main Entry Point: `get_available_workflows()`
Discover available BioCypher workflows and framework overview.

#### 2. Workflow Details: `get_adapter_creation_workflow()`
Get detailed information about the adapter creation workflow, including:
- 5-phase implementation process
- Decision framework for different extraction approaches
- Expected outputs for each phase

#### 3. Phase-Specific Guidance: `get_phase_guidance(phase_number)`
Get detailed instructions for any of the 5 phases:
- **Phase 1**: Data Analysis and Understanding
- **Phase 2**: Implementation Strategy Design  
- **Phase 3**: Implementation
- **Phase 4**: Quality Assurance
- **Phase 5**: Documentation and Maintenance

Each phase includes:
- Detailed step-by-step instructions
- Code examples and templates
- Expected outputs and deliverables

#### 4. Implementation Patterns: `get_implementation_patterns(pattern_type)`
Access reusable implementation patterns:
- **Field Mapping**: Map data fields to schema properties
- **Conditional Extraction**: Extract data using conditional rules
- **Progressive Fallback**: Try multiple extraction methods

#### 5. Decision Guidance: `get_decision_guidance(data_characteristics)`
Get AI-powered recommendations based on your data characteristics:
- Simple extraction for flat structures
- Series extraction for multiple resources
- Hierarchical extraction for nested data
- Custom extraction for complex scenarios

### Example Workflow

1. **Start with available workflows** to understand what's possible
2. **Get workflow details** to see the complete 5-phase process
3. **Navigate through phases** using phase-specific guidance
4. **Access implementation patterns** for specific scenarios
5. **Get decision guidance** based on your data characteristics

### Programmatic Usage

```python
from biocypher_mcp.main import (
    get_available_workflows,
    get_adapter_creation_workflow,
    get_phase_guidance,
    get_implementation_patterns,
    get_decision_guidance
)

# Discover available workflows
workflows = get_available_workflows()

# Get detailed workflow information
workflow = get_adapter_creation_workflow()

# Get guidance for a specific phase
phase_1_guidance = get_phase_guidance(1)

# Get implementation patterns
patterns = get_implementation_patterns()
field_mapping = get_implementation_patterns("field_mapping")

# Get decision guidance
data_chars = {"structure_type": "flat", "has_multiple_resources": False}
guidance = get_decision_guidance(data_chars)
```

### Example Script

See `example_usage.py` for a complete demonstration of the hierarchical tool navigation.

## MCP Specification Compliance

This MCP server implements the [Model Context Protocol Tools specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) and provides:

- **Hierarchical Tool Structure**: Tools that guide users through complex workflows
- **Comprehensive Documentation**: Each tool includes detailed descriptions and examples
- **Adaptive Guidance**: Tools that provide context-aware recommendations
- **FastMCP Integration**: Uses the FastMCP framework for efficient tool handling

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

### Adding New Tools

To add new tools to the hierarchical structure:

1. Define the tool function in `src/biocypher_mcp/main.py`
2. Register it with the FastMCP instance
3. Update the documentation to reflect the new tool

## License

MIT
