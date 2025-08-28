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
    get_resource_management_guidance,
    get_schema_configuration_guidance,
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
        
        assert len(phases) == 6, "Should have 6 phases"
        
        for phase in phases:
            expected_fields = ["phase", "name", "description", "key_activities", "outputs"]
            for field in expected_fields:
                assert field in phase, f"Missing field: {field}"

    def test_phase_numbers(self):
        """Test that phases are numbered correctly."""
        result = get_adapter_creation_workflow()
        phases = result["phases"]
        
        phase_numbers = [phase["phase"] for phase in phases]
        assert phase_numbers == [1, 2, 3, 4, 5, 6], "Phases should be numbered 1-6"

    def test_phase_names(self):
        """Test that phase names are correct."""
        result = get_adapter_creation_workflow()
        phases = result["phases"]
        
        expected_names = [
            "Resource Management and Data Acquisition",
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
        for phase_num in [1, 2, 3, 4, 5, 6]:
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
        assert result["available_phases"] == [1, 2, 3, 4, 5, 6]

    def test_phase_1_content(self):
        """Test that phase 1 has the expected content."""
        result = get_phase_guidance(1)
        
        assert result["phase_name"] == "Resource Management and Data Acquisition"
        assert len(result["detailed_instructions"]) > 0
        assert "Resource Identification" in result["detailed_instructions"][0]

    def test_phase_2_content(self):
        """Test that phase 2 has the expected content."""
        result = get_phase_guidance(2)
        
        assert result["phase_name"] == "Data Analysis and Understanding"
        assert "Resource Structure Analysis" in result["detailed_instructions"][0]

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
            get_decision_guidance,
            get_resource_management_guidance,
            get_schema_configuration_guidance
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
        assert isinstance(get_resource_management_guidance(), dict)
        assert isinstance(get_schema_configuration_guidance(), dict)

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
        assert phase_1["phase_name"] == "Resource Management and Data Acquisition"
        
        # Get implementation patterns
        patterns = get_implementation_patterns()
        assert "field_mapping" in patterns
        
        # Get decision guidance
        guidance = get_decision_guidance({"structure_type": "flat"})
        assert len(guidance["recommendations"]) > 0


class TestResourceManagementGuidance:
    """Test the resource management guidance tool."""

    def test_basic_structure(self):
        """Test that the resource management guidance has the correct structure."""
        result = get_resource_management_guidance()
        
        expected_sections = [
            "resource_management_overview",
            "core_components",
            "resource_initialization",
            "downloader_usage",
            "caching_behavior",
            "implementation_patterns",
            "best_practices",
            "integration_with_adapters",
            "troubleshooting",
            "resources"
        ]
        
        for section in expected_sections:
            assert section in result, f"Missing section: {section}"

    def test_overview_content(self):
        """Test that the overview section has the correct content."""
        result = get_resource_management_guidance()
        overview = result["resource_management_overview"]
        
        assert overview["name"] == "BioCypher Resource Management"
        assert "downloading, caching, and managing data sources" in overview["description"]
        assert overview["documentation_reference"] == "https://biocypher.org/BioCypher/reference/source/download-cache/"
        assert overview["pipeline_position"] == "Beginning of pipeline - data source acquisition"

    def test_core_components(self):
        """Test that core components are properly defined."""
        result = get_resource_management_guidance()
        components = result["core_components"]
        
        # Check resource base class
        assert "resource_base_class" in components
        base_class = components["resource_base_class"]
        assert base_class["name"] == "Resource Base Class"
        assert "biocypher/biocypher/_get.py" in base_class["location"]
        
        # Check downloader
        assert "downloader" in components
        downloader = components["downloader"]
        assert downloader["name"] == "Downloader"
        assert "Automatic caching" in downloader["key_features"]
        
        # Check resource types
        assert "resource_types" in components
        resource_types = components["resource_types"]
        assert "file_download" in resource_types
        assert "api_request" in resource_types

    def test_resource_initialization(self):
        """Test that resource initialization examples are provided."""
        result = get_resource_management_guidance()
        init = result["resource_initialization"]
        
        assert "basic_structure" in init
        structure = init["basic_structure"]
        assert "description" in structure
        assert "required_parameters" in structure
        assert "example" in structure
        
        # Check required parameters
        params = structure["required_parameters"]
        assert len(params) == 3
        assert any("name: Resource identifier" in param for param in params)
        assert any("url_s: URL or list of URLs" in param for param in params)
        assert any("lifetime: Cache lifetime in days" in param for param in params)

    def test_downloader_usage(self):
        """Test that downloader usage examples are provided."""
        result = get_resource_management_guidance()
        usage = result["downloader_usage"]
        
        assert "initialization" in usage
        assert "downloading_resources" in usage
        
        # Check initialization examples
        init_examples = usage["initialization"]["example"]
        assert "Downloader()" in init_examples
        assert "cache_dir" in init_examples
        
        # Check downloading examples
        download_examples = usage["downloading_resources"]["example"]
        assert "downloader.download" in download_examples
        assert "get_cached_version" in download_examples

    def test_caching_behavior(self):
        """Test that caching behavior is properly documented."""
        result = get_resource_management_guidance()
        caching = result["caching_behavior"]
        
        assert "cache_management" in caching
        assert "lifetime_settings" in caching
        
        # Check cache management features
        features = caching["cache_management"]["features"]
        assert "JSON record of download dates" in features
        assert "Automatic cache expiration" in features
        
        # Check lifetime settings
        lifetime = caching["lifetime_settings"]
        assert "permanent" in lifetime
        assert "temporary" in lifetime
        assert lifetime["permanent"]["value"] == 0

    def test_implementation_patterns(self):
        """Test that implementation patterns are provided."""
        result = get_resource_management_guidance()
        patterns = result["implementation_patterns"]
        
        assert "single_file_resource" in patterns
        assert "multiple_file_resource" in patterns
        assert "api_resource" in patterns
        
        # Check single file resource
        single = patterns["single_file_resource"]
        assert "FileDownload" in single["example"]
        assert "lifetime=0" in single["example"]
        
        # Check multiple file resource
        multiple = patterns["multiple_file_resource"]
        assert "url_s=[" in multiple["example"]
        assert "lifetime=7" in multiple["example"]

    def test_best_practices(self):
        """Test that best practices are documented."""
        result = get_resource_management_guidance()
        practices = result["best_practices"]
        
        assert "resource_naming" in practices
        assert "lifetime_management" in practices
        assert "cache_organization" in practices
        assert "error_handling" in practices
        
        # Check resource naming practices
        naming = practices["resource_naming"]
        assert len(naming) >= 2
        assert any("descriptive, unique names" in practice for practice in naming)

    def test_integration_with_adapters(self):
        """Test that adapter integration examples are provided."""
        result = get_resource_management_guidance()
        integration = result["integration_with_adapters"]
        
        assert "adapter_usage" in integration
        usage = integration["adapter_usage"]
        assert "description" in usage
        assert "example" in usage
        
        # Check example contains adapter class
        example = usage["example"]
        assert "class ProteinAdapter" in example
        assert "self.downloader = Downloader()" in example
        assert "self.protein_paths = self.downloader.download" in example

    def test_troubleshooting(self):
        """Test that troubleshooting guide is provided."""
        result = get_resource_management_guidance()
        troubleshooting = result["troubleshooting"]
        
        assert "common_issues" in troubleshooting
        issues = troubleshooting["common_issues"]
        assert len(issues) >= 3
        
        # Check specific issues
        issue_names = [issue["issue"] for issue in issues]
        assert "Cache not found" in issue_names
        assert "Download failures" in issue_names
        assert "Cache expiration issues" in issue_names

    def test_resources(self):
        """Test that resources section is provided."""
        result = get_resource_management_guidance()
        resources = result["resources"]
        
        assert "documentation" in resources
        assert "examples" in resources
        
        # Check documentation links
        docs = resources["documentation"]
        assert len(docs) >= 2
        assert "https://biocypher.org/BioCypher/reference/source/download-cache/" in docs


class TestSchemaConfigurationGuidance:
    """Test the schema configuration guidance tool."""

    def test_basic_structure(self):
        """Test that the schema configuration guidance has the correct structure."""
        result = get_schema_configuration_guidance()
        
        expected_sections = [
            "schema_configuration_overview",
            "schema_file_structure",
            "core_concepts",
            "schema_configuration_guidelines",
            "implementation_workflow",
            "best_practices",
            "common_patterns",
            "troubleshooting",
            "resources"
        ]
        
        for section in expected_sections:
            assert section in result, f"Missing section: {section}"

    def test_overview_content(self):
        """Test that the overview section has the correct content."""
        result = get_schema_configuration_guidance()
        overview = result["schema_configuration_overview"]
        
        assert overview["name"] == "BioCypher Schema Configuration"
        assert "data sources map to BioCypher's ontological structure" in overview["description"]
        assert overview["file_location"] == "config/schema_config.yaml"
        assert overview["documentation_reference"] == "https://biocypher.org/BioCypher/learn/tutorials/tutorial002_handling_ontologies/"

    def test_schema_file_structure(self):
        """Test that schema file structure is properly documented."""
        result = get_schema_configuration_guidance()
        file_structure = result["schema_file_structure"]
        
        assert file_structure["standard_location"] == "config/schema_config.yaml"
        assert file_structure["file_format"] == "YAML"
        assert file_structure["naming_convention"] == "schema_config.yaml"
        
        # Check alternative locations
        alternatives = file_structure["alternative_locations"]
        assert len(alternatives) >= 3
        assert "schema_config.yaml" in alternatives

    def test_core_concepts(self):
        """Test that core concepts are properly defined."""
        result = get_schema_configuration_guidance()
        concepts = result["core_concepts"]
        
        # Check ontology grounding
        assert "ontology_grounding" in concepts
        grounding = concepts["ontology_grounding"]
        assert "Machine readability and automation capabilities" in grounding["benefits"]
        assert grounding["default_ontology"] == "Biolink model"
        
        # Check schema configuration
        assert "schema_configuration" in concepts
        schema_config = concepts["schema_configuration"]
        assert "YAML file that maps data concepts to ontological classes" in schema_config["description"]

    def test_schema_configuration_guidelines(self):
        """Test that schema configuration guidelines are provided."""
        result = get_schema_configuration_guidance()
        guidelines = result["schema_configuration_guidelines"]
        
        assert "basic_structure" in guidelines
        assert "inheritance_patterns" in guidelines
        assert "synonym_usage" in guidelines
        
        # Check basic structure
        basic = guidelines["basic_structure"]
        assert "required_fields" in basic
        assert "optional_fields" in basic
        
        required_fields = basic["required_fields"]
        assert len(required_fields) >= 3
        assert any("represented_as: node or edge" in field for field in required_fields)

    def test_implementation_workflow(self):
        """Test that implementation workflow is provided."""
        result = get_schema_configuration_guidance()
        workflow = result["implementation_workflow"]
        
        assert "step_1" in workflow
        assert "step_2" in workflow
        assert "step_3" in workflow
        assert "step_4" in workflow
        
        # Check step 1
        step1 = workflow["step_1"]
        assert step1["action"] == "Analyze data source structure"
        assert "entities, relationships, and properties" in step1["description"]

    def test_best_practices(self):
        """Test that best practices are documented."""
        result = get_schema_configuration_guidance()
        practices = result["best_practices"]
        
        assert "naming_conventions" in practices
        assert "ontology_usage" in practices
        assert "schema_organization" in practices
        assert "validation" in practices
        
        # Check naming conventions
        naming = practices["naming_conventions"]
        assert len(naming) >= 2
        assert any("lowercase with underscores" in convention for convention in naming)

    def test_common_patterns(self):
        """Test that common patterns are provided."""
        result = get_schema_configuration_guidance()
        patterns = result["common_patterns"]
        
        assert "simple_entity" in patterns
        assert "multi_source_entity" in patterns
        assert "synonym_mapping" in patterns
        assert "relationship_mapping" in patterns
        
        # Check simple entity pattern
        simple = patterns["simple_entity"]
        assert "Basic entity mapping to ontology class" in simple["description"]
        assert "protein:" in simple["example"]
        assert "represented_as: node" in simple["example"]
        
        # Check multi-source entity pattern
        multi = patterns["multi_source_entity"]
        assert "Entity with multiple data sources" in multi["description"]
        assert "preferred_id: [reactome, wikipathways]" in multi["example"]

    def test_troubleshooting(self):
        """Test that troubleshooting guide is provided."""
        result = get_schema_configuration_guidance()
        troubleshooting = result["troubleshooting"]
        
        assert "common_issues" in troubleshooting
        issues = troubleshooting["common_issues"]
        assert len(issues) >= 3
        
        # Check specific issues
        issue_names = [issue["issue"] for issue in issues]
        assert "Schema validation errors" in issue_names
        assert "Missing ontology classes" in issue_names
        assert "Incorrect property mappings" in issue_names

    def test_resources(self):
        """Test that resources section is provided."""
        result = get_schema_configuration_guidance()
        resources = result["resources"]
        
        assert "documentation" in resources
        assert "ontologies" in resources
        assert "tools" in resources
        
        # Check documentation links
        docs = resources["documentation"]
        assert len(docs) >= 2
        assert "https://biocypher.org/BioCypher/learn/tutorials/tutorial002_handling_ontologies/" in docs


class TestUpdatedWorkflow:
    """Test the updated workflow with resource management."""

    def test_workflow_has_six_phases(self):
        """Test that the workflow now has 6 phases instead of 5."""
        result = get_adapter_creation_workflow()
        phases = result["phases"]
        
        assert len(phases) == 6, "Workflow should have 6 phases"
        
        phase_numbers = [phase["phase"] for phase in phases]
        assert phase_numbers == [1, 2, 3, 4, 5, 6], "Phases should be numbered 1-6"

    def test_phase_1_is_resource_management(self):
        """Test that phase 1 is now Resource Management and Data Acquisition."""
        result = get_adapter_creation_workflow()
        phase_1 = result["phases"][0]
        
        assert phase_1["phase"] == 1
        assert phase_1["name"] == "Resource Management and Data Acquisition"
        assert "Set up resource management" in phase_1["description"]
        
        # Check key activities
        activities = phase_1["key_activities"]
        assert "Resource Identification" in activities
        assert "Download Strategy Design" in activities
        assert "Cache Configuration" in activities

    def test_phase_2_is_data_analysis(self):
        """Test that phase 2 is Data Analysis and Understanding."""
        result = get_adapter_creation_workflow()
        phase_2 = result["phases"][1]
        
        assert phase_2["phase"] == 2
        assert phase_2["name"] == "Data Analysis and Understanding"
        assert "Analyze the input data structure" in phase_2["description"]

    def test_phase_3_is_implementation_strategy(self):
        """Test that phase 3 is Implementation Strategy Design."""
        result = get_adapter_creation_workflow()
        phase_3 = result["phases"][2]
        
        assert phase_3["phase"] == 3
        assert phase_3["name"] == "Implementation Strategy Design"
        assert "Design the adapter architecture" in phase_3["description"]

    def test_phase_4_is_implementation(self):
        """Test that phase 4 is Implementation."""
        result = get_adapter_creation_workflow()
        phase_4 = result["phases"][3]
        
        assert phase_4["phase"] == 4
        assert phase_4["name"] == "Implementation"
        assert "Implement the adapter" in phase_4["description"]

    def test_phase_5_is_quality_assurance(self):
        """Test that phase 5 is Quality Assurance."""
        result = get_adapter_creation_workflow()
        phase_5 = result["phases"][4]
        
        assert phase_5["phase"] == 5
        assert phase_5["name"] == "Quality Assurance"
        assert "Test and validate" in phase_5["description"]

    def test_phase_6_is_documentation(self):
        """Test that phase 6 is Documentation and Maintenance."""
        result = get_adapter_creation_workflow()
        phase_6 = result["phases"][5]
        
        assert phase_6["phase"] == 6
        assert phase_6["name"] == "Documentation and Maintenance"
        assert "Document the implementation" in phase_6["description"]


class TestUpdatedPhaseGuidance:
    """Test the updated phase guidance with 6 phases."""

    def test_six_phases_available(self):
        """Test that all 6 phases have guidance available."""
        for phase_num in [1, 2, 3, 4, 5, 6]:
            result = get_phase_guidance(phase_num)
            
            assert "phase_name" in result
            assert "detailed_instructions" in result
            assert "code_examples" in result
            assert "outputs_expected" in result

    def test_phase_1_resource_management_content(self):
        """Test that phase 1 has resource management content."""
        result = get_phase_guidance(1)
        
        assert result["phase_name"] == "Resource Management and Data Acquisition"
        assert len(result["detailed_instructions"]) > 0
        assert "Resource Identification" in result["detailed_instructions"][0]
        assert "Download Strategy Design" in result["detailed_instructions"][6]
        assert "Cache Configuration" in result["detailed_instructions"][12]

    def test_phase_2_data_analysis_content(self):
        """Test that phase 2 has data analysis content."""
        result = get_phase_guidance(2)
        
        assert result["phase_name"] == "Data Analysis and Understanding"
        assert "Resource Structure Analysis" in result["detailed_instructions"][0]
        # Check that schema configuration planning is mentioned somewhere in the instructions
        instructions_text = " ".join(result["detailed_instructions"])
        assert "Schema Configuration Planning" in instructions_text

    def test_phase_3_strategy_design_content(self):
        """Test that phase 3 has strategy design content."""
        result = get_phase_guidance(3)
        
        assert result["phase_name"] == "Implementation Strategy Design"
        assert "Adapter Architecture Decision" in result["detailed_instructions"][0]
        # Check that schema configuration implementation is mentioned somewhere in the instructions
        instructions_text = " ".join(result["detailed_instructions"])
        assert "Schema Configuration Implementation" in instructions_text

    def test_phase_4_implementation_content(self):
        """Test that phase 4 has implementation content."""
        result = get_phase_guidance(4)
        
        assert result["phase_name"] == "Implementation"
        assert "Base Adapter Template" in result["detailed_instructions"][0]
        assert "Implementation Patterns" in result["detailed_instructions"][6]

    def test_phase_5_quality_assurance_content(self):
        """Test that phase 5 has quality assurance content."""
        result = get_phase_guidance(5)
        
        assert result["phase_name"] == "Quality Assurance"
        assert "Adaptive Testing Strategy" in result["detailed_instructions"][0]
        # Check that validation framework is mentioned somewhere in the instructions
        instructions_text = " ".join(result["detailed_instructions"])
        assert "Validation Framework" in instructions_text

    def test_phase_6_documentation_content(self):
        """Test that phase 6 has documentation content."""
        result = get_phase_guidance(6)
        
        assert result["phase_name"] == "Documentation and Maintenance"
        assert "Adaptive Documentation" in result["detailed_instructions"][0]
        assert "Maintenance Planning" in result["detailed_instructions"][6]

    def test_invalid_phase_number_updated(self):
        """Test that invalid phase numbers return updated error message."""
        result = get_phase_guidance(99)
        
        assert "error" in result
        assert "available_phases" in result
        assert result["available_phases"] == [1, 2, 3, 4, 5, 6]

    def test_phase_outputs_updated(self):
        """Test that phase outputs are correctly updated."""
        # Test phase 1 outputs
        phase_1 = get_phase_guidance(1)
        expected_outputs_1 = ["Resource definitions", "Download strategy", "Cache configuration"]
        assert phase_1["outputs_expected"] == expected_outputs_1
        
        # Test phase 2 outputs
        phase_2 = get_phase_guidance(2)
        expected_outputs_2 = ["Data source type identification", "Structure analysis report", "Schema requirements assessment", "Schema configuration plan"]
        assert phase_2["outputs_expected"] == expected_outputs_2
        
        # Test phase 3 outputs
        phase_3 = get_phase_guidance(3)
        expected_outputs_3 = ["Architecture choice (Simple/Series/Hierarchical/Custom)", "Extraction strategy document", "Schema configuration file (config/schema_config.yaml)"]
        assert phase_3["outputs_expected"] == expected_outputs_3


class TestMCPToolIntegrationUpdated:
    """Test the integration of updated tools with the MCP server."""

    def test_new_tools_are_callable(self):
        """Test that new tool functions are callable."""
        new_tools = [
            get_resource_management_guidance,
            get_schema_configuration_guidance
        ]
        
        for tool in new_tools:
            assert callable(tool), f"Tool {tool.__name__} should be callable"

    def test_new_tools_return_expected_types(self):
        """Test that new tool functions return the expected types."""
        assert isinstance(get_resource_management_guidance(), dict)
        assert isinstance(get_schema_configuration_guidance(), dict)

    def test_complete_workflow_navigation(self):
        """Test that the complete workflow navigation works with new tools."""
        # Start with available workflows
        workflows = get_available_workflows()
        assert "adapter_creation" in [w["id"] for w in workflows["workflows"]]
        
        # Get workflow details (now with 6 phases)
        workflow = get_adapter_creation_workflow()
        assert workflow["workflow_id"] == "adapter_creation"
        assert len(workflow["phases"]) == 6
        
        # Get phase 1 guidance (Resource Management)
        phase_1 = get_phase_guidance(1)
        assert phase_1["phase_name"] == "Resource Management and Data Acquisition"
        
        # Get resource management guidance
        resource_guidance = get_resource_management_guidance()
        assert resource_guidance["resource_management_overview"]["name"] == "BioCypher Resource Management"
        
        # Get schema configuration guidance
        schema_guidance = get_schema_configuration_guidance()
        assert schema_guidance["schema_configuration_overview"]["name"] == "BioCypher Schema Configuration"
        
        # Get phase 3 guidance (Implementation Strategy)
        phase_3 = get_phase_guidance(3)
        assert phase_3["phase_name"] == "Implementation Strategy Design"
        
        # Get implementation patterns
        patterns = get_implementation_patterns()
        assert "field_mapping" in patterns
        
        # Get decision guidance
        guidance = get_decision_guidance({"structure_type": "flat"})
        assert len(guidance["recommendations"]) > 0
