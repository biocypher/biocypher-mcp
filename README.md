# biocypher-mcp

An MCP for assisting with BioCypher workflows.

## Installation

Install the package with uv:

```bash
uv sync --dev
```

## Usage

You can run the MCP:

```bash
uv run biocypher-mcp
```

Or install globally and run:

```bash
uvx biocypher-mcp
```

Or import in your Python code:

```python
from biocypher_mcp.main import create_mcp

mcp = create_mcp()
mcp.run()
```

## Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/slobentanzer/biocypher-mcp.git
cd biocypher-mcp

# Install development dependencies
uv sync --dev
```


## License

MIT
