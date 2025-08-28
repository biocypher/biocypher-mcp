"""
Tests for the BioCypher MCP tool functionality.
"""

import pytest
import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from biocypher_mcp.main import (
    get_available_workflows,
    get_adapter_creation_workflow,
    get_phase_guidance,
    get_implementation_patterns,
    get_decision_guidance,
    mcp
)


class TestAvailableWorkflows:
    """Test the main entry point tool for available workflows."""

    def test_workflows_structure(self):
        """Test that the workflows response has the correct structure."""
        result = get_available_workflows()
        
        # Check required fields
        assert "workflows" in result
        assert "framework_overview" in result
        
        # Check workflows is a list
        assert isinstance(result["workflows"], list)
        assert len(result["workflows"]) > 0

    def test_workflow_structure(self):
        """Test that individual workflows have the correct structure."""
        result = get_available_workflows()
        workflow = result["workflows"][0]
        
        expected_fields = ["id", "name", "description", "status", "complexity", "estimated_time", "prerequisites"]
        for field in expected_fields:
            assert field in workflow, f"Missing field: {field}"

    def test_adapter_creation_workflow(self):
        """Test that the adapter creation workflow is available."""
        result = get_available_workflows()
        workflows = result["workflows"]
        
        adapter_workflow = next((w for w in workflows if w["id"] == "adapter_creation"), None)
        assert adapter_workflow is not None, "Adapter creation workflow should be available"
        
        assert adapter_workflow["name"] == "BioCypher Adapter Creation"
        assert "adaptive analysis" in adapter_workflow["description"]
        assert adapter_workflow["status"] == "available"

    def test_framework_overview(self):
        """Test that the framework overview is provided."""
        result = get_available_workflows()
        overview = result["framework_overview"]
        
        assert "name" in overview
        assert "description" in overview
        assert "core_principles" in overview
        
        assert overview["name"] == "BioCypher Adapter Creation Framework"
        assert isinstance(overview["core_principles"], list)
        assert len(overview["core_principles"]) == 3


class TestAdapterCreationWorkflow:
    """Test the adapter creation workflow tool."""

    def test_workflow_structure(self):
        """Test that the workflow has the correct structure."""
        result = get_adapter_creation_workflow()
        
        expected_fields = ["workflow_id", "name", "description", "phases", "decision_framework"]
        for field in expected_fields:
            assert field in result, f"Missing field: {field}"

    def test_workflow_content(self):
        """Test that the workflow has the correct content."""
        result = get_adapter_creation_workflow()
        
        assert result["workflow_id"] == "adapter_creation"
        assert result["name"] == "BioCypher Adapter Creation Workflow"
        assert "Complete workflow" in result["description"]

    def test_phases_structure(self):
        """Test that the phases have the correct structure."""
        result = get_adapter_creation_workflow()
        phases = result["phases"]
        
        assert len(phases) == 5, "Should have 5 phases"
        
        for phase in phases:
            expected_fields = ["phase", "name", "description", "key_activities", "outputs"]
            for field in expected_fields:
                assert field in phase, f"Missing field: {field}"

    def test_phase_numbers(self):
        """Test that phases are numbered correctly."""
        result = get_adapter_creation_workflow()
        phases = result["phases"]
        
        phase_numbers = [phase["phase"] for phase in phases]
        assert phase_numbers == [1, 2, 3, 4, 5], "Phases should be numbered 1-5"

    def test_phase_names(self):
        """Test that phase names are correct."""
        result = get_adapter_creation_workflow()
        phases = result["phases"]
        
        expected_names = [
            "Data Analysis and Understanding",
            "Implementation Strategy Design",
            "Implementation",
            "Quality Assurance",
            "Documentation and Maintenance"
        ]
        
        actual_names = [phase["name"] for phase in phases]
        assert actual_names == expected_names

    def test_decision_framework(self):
        """Test that the decision framework is provided."""
        result = get_adapter_creation_workflow()
        framework = result["decision_framework"]
        
        expected_approaches = ["simple_extraction", "series_extraction", "hierarchical_extraction", "custom_extraction"]
        for approach in expected_approaches:
            assert approach in framework, f"Missing approach: {approach}"


class TestPhaseGuidance:
    """Test the phase guidance tool."""

    def test_valid_phase_numbers(self):
        """Test that valid phase numbers return guidance."""
        for phase_num in [1, 2, 3, 4, 5]:
            result = get_phase_guidance(phase_num)
            
            assert "phase_name" in result
            assert "detailed_instructions" in result
            assert "code_examples" in result
            assert "outputs_expected" in result

    def test_invalid_phase_number(self):
        """Test that invalid phase numbers return an error."""
        result = get_phase_guidance(99)
        
        assert "error" in result
        assert "available_phases" in result
        assert result["available_phases"] == [1, 2, 3, 4, 5]

    def test_phase_1_content(self):
        """Test that phase 1 has the expected content."""
        result = get_phase_guidance(1)
        
        assert result["phase_name"] == "Data Analysis and Understanding"
        assert len(result["detailed_instructions"]) > 0
        assert "Resource Structure Analysis" in result["detailed_instructions"][0]

    def test_phase_2_content(self):
        """Test that phase 2 has the expected content."""
        result = get_phase_guidance(2)
        
        assert result["phase_name"] == "Implementation Strategy Design"
        assert "Adapter Architecture Decision" in result["detailed_instructions"][0]

    def test_code_examples_structure(self):
        """Test that code examples have the correct structure."""
        result = get_phase_guidance(1)
        examples = result["code_examples"]
        
        assert isinstance(examples, dict)
        assert len(examples) > 0
        
        for example_name, example_code in examples.items():
            assert isinstance(example_name, str)
            assert isinstance(example_code, str)
            assert len(example_code) > 0


class TestImplementationPatterns:
    """Test the implementation patterns tool."""

    def test_all_patterns(self):
        """Test that all patterns are returned when no specific type is requested."""
        result = get_implementation_patterns()
        
        expected_patterns = ["field_mapping", "conditional_extraction", "progressive_fallback"]
        for pattern in expected_patterns:
            assert pattern in result, f"Missing pattern: {pattern}"

    def test_specific_pattern(self):
        """Test that a specific pattern can be retrieved."""
        result = get_implementation_patterns("field_mapping")
        
        assert "name" in result
        assert "description" in result
        assert "use_case" in result
        assert "code" in result
        assert "example_mapping" in result

    def test_invalid_pattern(self):
        """Test that invalid pattern types return an error."""
        result = get_implementation_patterns("invalid_pattern")
        
        assert "error" in result
        assert "available_patterns" in result

    def test_field_mapping_pattern(self):
        """Test the field mapping pattern specifically."""
        result = get_implementation_patterns("field_mapping")
        
        assert result["name"] == "Field Mapping Pattern"
        assert "Map data fields to schema properties" in result["description"]
        assert "map_fields_to_schema" in result["code"]

    def test_conditional_extraction_pattern(self):
        """Test the conditional extraction pattern specifically."""
        result = get_implementation_patterns("conditional_extraction")
        
        assert result["name"] == "Conditional Extraction Pattern"
        assert "conditional rules" in result["description"]
        assert "extract_with_conditions" in result["code"]

    def test_progressive_fallback_pattern(self):
        """Test the progressive fallback pattern specifically."""
        result = get_implementation_patterns("progressive_fallback")
        
        assert result["name"] == "Progressive Fallback Pattern"
        assert "multiple extraction methods" in result["description"]
        assert "extract_with_fallbacks" in result["code"]


class TestDecisionGuidance:
    """Test the decision guidance tool."""

    def test_basic_structure(self):
        """Test that the decision guidance has the correct structure."""
        data_chars = {"structure_type": "flat"}
        result = get_decision_guidance(data_chars)
        
        assert "data_characteristics" in result
        assert "recommendations" in result
        assert "decision_framework" in result

    def test_simple_extraction_recommendation(self):
        """Test that flat structure triggers simple extraction recommendation."""
        data_chars = {"structure_type": "flat"}
        result = get_decision_guidance(data_chars)
        
        recommendations = result["recommendations"]
        simple_rec = next((r for r in recommendations if r["approach"] == "Simple Extraction"), None)
        
        assert simple_rec is not None
        assert "Flat structure with consistent field names" in simple_rec["reason"]

    def test_series_extraction_recommendation(self):
        """Test that multiple resources triggers series extraction recommendation."""
        data_chars = {"has_multiple_resources": True}
        result = get_decision_guidance(data_chars)
        
        recommendations = result["recommendations"]
        series_rec = next((r for r in recommendations if r["approach"] == "Series Extraction"), None)
        
        assert series_rec is not None
        assert "Multiple resources with shared structure" in series_rec["reason"]

    def test_hierarchical_extraction_recommendation(self):
        """Test that hierarchy triggers hierarchical extraction recommendation."""
        data_chars = {"has_hierarchy": True}
        result = get_decision_guidance(data_chars)
        
        recommendations = result["recommendations"]
        hierarchy_rec = next((r for r in recommendations if r["approach"] == "Hierarchical Extraction"), None)
        
        assert hierarchy_rec is not None
        assert "Nested data structures" in hierarchy_rec["reason"]

    def test_custom_extraction_recommendation(self):
        """Test that irregular structure triggers custom extraction recommendation."""
        data_chars = {"has_irregular_structure": True}
        result = get_decision_guidance(data_chars)
        
        recommendations = result["recommendations"]
        custom_rec = next((r for r in recommendations if r["approach"] == "Custom Extraction"), None)
        
        assert custom_rec is not None
        assert "Irregular data structures" in custom_rec["reason"]

    def test_multiple_recommendations(self):
        """Test that multiple characteristics trigger multiple recommendations."""
        data_chars = {
            "structure_type": "flat",
            "has_multiple_resources": True,
            "has_hierarchy": True
        }
        result = get_decision_guidance(data_chars)
        
        recommendations = result["recommendations"]
        assert len(recommendations) >= 3

    def test_decision_framework_structure(self):
        """Test that the decision framework has the correct structure."""
        data_chars = {}
        result = get_decision_guidance(data_chars)
        framework = result["decision_framework"]
        
        expected_approaches = ["simple_extraction", "series_extraction", "hierarchical_extraction", "custom_extraction"]
        for approach in expected_approaches:
            assert approach in framework


class TestMCPToolIntegration:
    """Test the integration of tools with the MCP server."""

    def test_mcp_server_creation(self):
        """Test that the MCP server is created successfully."""
        assert mcp is not None, "MCP server should be created"
        assert hasattr(mcp, 'run'), "MCP server should have a run method"

    def test_tool_functions_are_callable(self):
        """Test that all tool functions are callable."""
        tools = [
            get_available_workflows,
            get_adapter_creation_workflow,
            get_phase_guidance,
            get_implementation_patterns,
            get_decision_guidance
        ]
        
        for tool in tools:
            assert callable(tool), f"Tool {tool.__name__} should be callable"

    def test_tool_functions_return_expected_types(self):
        """Test that tool functions return the expected types."""
        assert isinstance(get_available_workflows(), dict)
        assert isinstance(get_adapter_creation_workflow(), dict)
        assert isinstance(get_phase_guidance(1), dict)
        assert isinstance(get_implementation_patterns(), dict)
        assert isinstance(get_decision_guidance({}), dict)

    def test_hierarchical_navigation(self):
        """Test that the tools support hierarchical navigation."""
        # Start with available workflows
        workflows = get_available_workflows()
        assert "adapter_creation" in [w["id"] for w in workflows["workflows"]]
        
        # Get workflow details
        workflow = get_adapter_creation_workflow()
        assert workflow["workflow_id"] == "adapter_creation"
        
        # Get phase guidance
        phase_1 = get_phase_guidance(1)
        assert phase_1["phase_name"] == "Data Analysis and Understanding"
        
        # Get implementation patterns
        patterns = get_implementation_patterns()
        assert "field_mapping" in patterns
        
        # Get decision guidance
        guidance = get_decision_guidance({"structure_type": "flat"})
        assert len(guidance["recommendations"]) > 0
