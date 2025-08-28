"""
Tests for the BioCypher MCP resource functionality.
"""

import pytest
from pathlib import Path
import sys

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from biocypher_mcp.main import (
    get_biocypher_adapter_framework_resource,
    get_biocypher_adapter_framework_content,
    mcp
)


class TestBiocypherAdapterFrameworkResource:
    """Test the BioCypher Adapter Creation Framework resource."""

    def test_resource_definition_structure(self):
        """Test that the resource definition has the correct structure."""
        resource = get_biocypher_adapter_framework_resource()
        
        # Check required fields
        expected_fields = ["uri", "name", "title", "mimeType", "description", "annotations"]
        for field in expected_fields:
            assert field in resource, f"Missing field: {field}"
        
        # Check field types
        assert isinstance(resource["uri"], str)
        assert isinstance(resource["name"], str)
        assert isinstance(resource["title"], str)
        assert isinstance(resource["mimeType"], str)
        assert isinstance(resource["description"], str)
        assert isinstance(resource["annotations"], dict)

    def test_resource_definition_values(self):
        """Test that the resource definition has the correct values."""
        resource = get_biocypher_adapter_framework_resource()
        
        # Check specific values
        assert resource["uri"] == "https://biocypher.org/resources/adapter-creation-framework"
        assert resource["name"] == "adapter-creation-framework"
        assert resource["title"] == "BioCypher Adapter Creation Framework"
        assert resource["mimeType"] == "text/markdown"
        assert "Generalized framework for creating BioCypher adapters" in resource["description"]

    def test_resource_annotations(self):
        """Test that the resource annotations are correct."""
        resource = get_biocypher_adapter_framework_resource()
        annotations = resource["annotations"]
        
        # Check annotation fields
        assert "audience" in annotations
        assert "priority" in annotations
        assert "lastModified" in annotations
        
        # Check annotation values
        assert isinstance(annotations["audience"], list)
        assert "user" in annotations["audience"]
        assert "assistant" in annotations["audience"]
        assert isinstance(annotations["priority"], (int, float))
        assert 0 <= annotations["priority"] <= 1
        assert isinstance(annotations["lastModified"], str)

    def test_resource_content_not_empty(self):
        """Test that the resource content is not empty."""
        content = get_biocypher_adapter_framework_content()
        
        assert len(content) > 0, "Content should not be empty"
        assert isinstance(content, str)

    def test_resource_content_structure(self):
        """Test that the resource content has the expected structure."""
        content = get_biocypher_adapter_framework_content()
        
        # Check for main sections
        expected_sections = [
            "# BioCypher Adapter Creation Framework",
            "## Overview",
            "## Core Principles",
            "## Adaptive Implementation Process",
            "## Implementation Guidelines",
            "## Example Workflows"
        ]
        
        for section in expected_sections:
            assert section in content, f"Missing section: {section}"

    def test_resource_content_subsections(self):
        """Test that the resource content has the expected subsections."""
        content = get_biocypher_adapter_framework_content()
        
        # Check for important subsections
        expected_subsections = [
            "### 1. Data-First Approach",
            "### 2. Schema-Driven Development",
            "### 3. Iterative Refinement",
            "### Phase 1: Data Analysis and Understanding",
            "### Phase 2: Implementation Strategy Design",
            "### Phase 3: Implementation",
            "### Phase 4: Quality Assurance",
            "### Phase 5: Documentation and Maintenance"
        ]
        
        for subsection in expected_subsections:
            assert subsection in content, f"Missing subsection: {subsection}"

    def test_resource_content_code_blocks(self):
        """Test that the resource content contains code examples."""
        content = get_biocypher_adapter_framework_content()
        
        # Check for Python code blocks
        assert "```python" in content
        assert "def analyze_resource_structure" in content
        assert "class AdaptiveAdapter" in content
        assert "def map_fields_to_schema" in content

    def test_resource_content_implementation_patterns(self):
        """Test that the resource content includes implementation patterns."""
        content = get_biocypher_adapter_framework_content()
        
        # Check for implementation patterns
        assert "**Pattern 1: Field Mapping**" in content
        assert "**Pattern 2: Conditional Extraction**" in content
        assert "**Pattern 3: Progressive Fallback**" in content

    def test_resource_content_workflows(self):
        """Test that the resource content includes example workflows."""
        content = get_biocypher_adapter_framework_content()
        
        # Check for workflow examples
        assert "### Workflow 1: Simple File-Based Data" in content
        assert "### Workflow 2: API-Based Series Data" in content
        assert "### Workflow 3: Complex Database Integration" in content

    def test_mcp_server_creation(self):
        """Test that the MCP server is created successfully."""
        assert mcp is not None, "MCP server should be created"
        assert hasattr(mcp, 'run'), "MCP server should have a run method"

    def test_resource_file_exists(self):
        """Test that the resource markdown file exists."""
        current_dir = Path(__file__).parent.parent / "src" / "biocypher_mcp"
        resource_file = current_dir / "resources" / "adapter_framework.md"
        
        assert resource_file.exists(), f"Resource file should exist at {resource_file}"
        assert resource_file.is_file(), f"Resource file should be a file: {resource_file}"

    def test_resource_file_readable(self):
        """Test that the resource markdown file is readable."""
        current_dir = Path(__file__).parent.parent / "src" / "biocypher_mcp"
        resource_file = current_dir / "resources" / "adapter_framework.md"
        
        try:
            with open(resource_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert len(content) > 0, "Resource file should not be empty"
        except Exception as e:
            pytest.fail(f"Resource file should be readable: {e}")

    def test_resource_content_consistency(self):
        """Test that the resource content is consistent between file and function."""
        current_dir = Path(__file__).parent.parent / "src" / "biocypher_mcp"
        resource_file = current_dir / "resources" / "adapter_framework.md"
        
        with open(resource_file, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        function_content = get_biocypher_adapter_framework_content()
        
        assert file_content == function_content, "Content should be consistent between file and function"

    def test_resource_uri_format(self):
        """Test that the resource URI follows the expected format."""
        resource = get_biocypher_adapter_framework_resource()
        uri = resource["uri"]
        
        # Check URI format
        assert uri.startswith("https://"), "URI should start with https://"
        assert "biocypher.org" in uri, "URI should contain biocypher.org"
        assert "resources" in uri, "URI should contain resources path"
        assert "adapter-creation-framework" in uri, "URI should contain resource name"

    def test_resource_priority_range(self):
        """Test that the resource priority is within the expected range."""
        resource = get_biocypher_adapter_framework_resource()
        priority = resource["annotations"]["priority"]
        
        assert 0.0 <= priority <= 1.0, "Priority should be between 0.0 and 1.0"
        assert priority == 0.9, "Priority should be 0.9 as specified"

    def test_resource_audience_values(self):
        """Test that the resource audience values are correct."""
        resource = get_biocypher_adapter_framework_resource()
        audience = resource["annotations"]["audience"]
        
        expected_audience = ["user", "assistant"]
        assert audience == expected_audience, f"Audience should be {expected_audience}"

    def test_resource_last_modified_format(self):
        """Test that the resource last modified timestamp is in ISO format."""
        resource = get_biocypher_adapter_framework_resource()
        last_modified = resource["annotations"]["lastModified"]
        
        # Check ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        import re
        iso_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$'
        assert re.match(iso_pattern, last_modified), f"Last modified should be in ISO 8601 format: {last_modified}"


class TestMCPResourceIntegration:
    """Test the integration of resources with the MCP server."""

    def test_mcp_server_has_resources(self):
        """Test that the MCP server has registered resources."""
        # This is a basic test - in a real scenario, you'd test the actual MCP protocol
        assert mcp is not None, "MCP server should exist"
        
        # Check if the server has the expected methods
        assert hasattr(mcp, 'run'), "MCP server should have a run method"

    def test_resource_functions_are_callable(self):
        """Test that the resource functions are callable."""
        assert callable(get_biocypher_adapter_framework_resource)
        assert callable(get_biocypher_adapter_framework_content)

    def test_resource_functions_return_expected_types(self):
        """Test that the resource functions return the expected types."""
        resource = get_biocypher_adapter_framework_resource()
        content = get_biocypher_adapter_framework_content()
        
        assert isinstance(resource, dict), "Resource should return a dictionary"
        assert isinstance(content, str), "Content should return a string"
