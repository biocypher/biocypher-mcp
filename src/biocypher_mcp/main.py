################################################################################
# biocypher_mcp/main.py
# This module provides a hierarchical MCP tool for BioCypher workflows
################################################################################
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP


def get_available_workflows() -> Dict[str, Any]:
    """
    Main entry point tool that provides information about available BioCypher workflows.
    
    Returns:
        Dict containing available workflows and their descriptions
    """
    return {
        "workflows": [
            {
                "id": "adapter_creation",
                "name": "BioCypher Adapter Creation",
                "description": "Create BioCypher adapters for any data source using adaptive analysis and implementation strategies",
                "status": "available",
                "complexity": "adaptive",
                "estimated_time": "30-120 minutes",
                "prerequisites": [
                    "Data source to be integrated",
                    "Basic understanding of BioCypher concepts",
                    "Python development environment"
                ]
            }
        ],
        "framework_overview": {
            "name": "BioCypher Adapter Creation Framework",
            "description": "A generalized framework for creating BioCypher adapters from any data source, with adaptive analysis and implementation strategies",
            "core_principles": [
                "Data-First Approach",
                "Schema-Driven Development", 
                "Iterative Refinement"
            ]
        }
    }


def get_adapter_creation_workflow() -> Dict[str, Any]:
    """
    Provides detailed information about the adapter creation workflow.
    
    Returns:
        Dict containing the workflow structure and phases
    """
    return {
        "workflow_id": "adapter_creation",
        "name": "BioCypher Adapter Creation Workflow",
        "description": "Complete workflow for creating BioCypher adapters from any data source",
        "phases": [
            {
                "phase": 1,
                "name": "Data Analysis and Understanding",
                "description": "Analyze the input data structure before making implementation decisions",
                "key_activities": [
                    "Resource Structure Analysis",
                    "Metadata Pattern Recognition", 
                    "Schema Assessment"
                ],
                "outputs": [
                    "Data source type identification",
                    "Structure analysis report",
                    "Schema requirements assessment"
                ]
            },
            {
                "phase": 2,
                "name": "Implementation Strategy Design",
                "description": "Design the adapter architecture and extraction strategy based on data analysis",
                "key_activities": [
                    "Adapter Architecture Decision",
                    "Data Extraction Strategy Design"
                ],
                "outputs": [
                    "Architecture choice (Simple/Series/Hierarchical/Custom)",
                    "Extraction strategy document"
                ]
            },
            {
                "phase": 3,
                "name": "Implementation",
                "description": "Implement the adapter using the designed strategy",
                "key_activities": [
                    "Base Adapter Template Creation",
                    "Implementation Pattern Application"
                ],
                "outputs": [
                    "Working adapter code",
                    "Field mapping configuration"
                ]
            },
            {
                "phase": 4,
                "name": "Quality Assurance",
                "description": "Test and validate the adapter implementation",
                "key_activities": [
                    "Adaptive Testing Strategy",
                    "Validation Framework Application"
                ],
                "outputs": [
                    "Test suite",
                    "Validation results"
                ]
            },
            {
                "phase": 5,
                "name": "Documentation and Maintenance",
                "description": "Document the implementation and prepare for maintenance",
                "key_activities": [
                    "Adaptive Documentation Generation",
                    "Maintenance Planning"
                ],
                "outputs": [
                    "Implementation documentation",
                    "Usage examples",
                    "Troubleshooting guide"
                ]
            }
        ],
        "decision_framework": {
            "simple_extraction": "Single resource with flat structure, consistent field names, no complex relationships",
            "series_extraction": "Multiple resources with shared structure, consistent metadata patterns, batch processing requirements",
            "hierarchical_extraction": "Nested data structures, parent-child relationships, complex metadata hierarchies",
            "custom_extraction": "Irregular data structures, complex transformation requirements, multiple data source integration"
        }
    }


def get_phase_guidance(phase_number: int) -> Dict[str, Any]:
    """
    Provides detailed guidance for a specific phase of the adapter creation workflow.
    
    Args:
        phase_number: The phase number (1-5) to get guidance for
        
    Returns:
        Dict containing detailed guidance for the specified phase
    """
    phase_guidance = {
        1: {
            "phase_name": "Data Analysis and Understanding",
            "detailed_instructions": [
                "1.1 Resource Structure Analysis:",
                "   - Determine data source type (file-based, API-based, database-based, custom)",
                "   - Analyze the structure of the input data source",
                "   - Adapt analysis based on data type and format",
                "",
                "1.2 Metadata Pattern Recognition:",
                "   - For Single Resource: Extract all available metadata fields",
                "   - For Series/Collection: Identify shared vs. unique metadata patterns", 
                "   - For Hierarchical Data: Map parent-child relationships",
                "   - For Time Series: Identify temporal patterns and sequences",
                "",
                "1.3 Schema Assessment:",
                "   - Determine if existing schema is sufficient or needs creation/modification",
                "   - If no schema exists, create one based on data analysis",
                "   - Check if existing schema covers all data concepts",
                "   - Extend schema if missing concepts are identified"
            ],
            "code_examples": {
                "resource_analysis": """
def analyze_resource_structure(data_source):
    # Determine data source type
    if is_file_based(data_source):
        return analyze_file_structure(data_source)
    elif is_api_based(data_source):
        return analyze_api_structure(data_source)
    elif is_database_based(data_source):
        return analyze_database_structure(data_source)
    else:
        return analyze_custom_structure(data_source)
""",
                "schema_assessment": """
def assess_schema_requirements(data_analysis, existing_schema=None):
    if not existing_schema:
        return create_schema_from_analysis(data_analysis)
    
    # Check if existing schema covers all data concepts
    missing_concepts = identify_missing_concepts(data_analysis, existing_schema)
    if missing_concepts:
        return extend_schema(existing_schema, missing_concepts)
    
    return existing_schema
"""
            },
            "outputs_expected": [
                "Data source type identification",
                "Structure analysis report", 
                "Schema requirements assessment"
            ]
        },
        2: {
            "phase_name": "Implementation Strategy Design",
            "detailed_instructions": [
                "2.1 Adapter Architecture Decision:",
                "   - Choose appropriate architecture based on data analysis:",
                "     * Simple Adapter: Single resource, flat structure",
                "     * Series Adapter: Multiple resources, shared structure",
                "     * Hierarchical Adapter: Nested structure",
                "     * Custom Adapter: Complex, irregular structure",
                "",
                "2.2 Data Extraction Strategy:",
                "   - Design extraction strategy based on data characteristics",
                "   - Determine primary extraction method",
                "   - Identify fallback methods",
                "   - Design error handling approach",
                "   - Create validation rules"
            ],
            "code_examples": {
                "architecture_decision": """
# Simple Adapter (Single resource, flat structure)
class SimpleAdapter(BaseAdapter):
    def get_nodes(self):
        # Direct extraction from single resource
        pass

# Series Adapter (Multiple resources, shared structure)  
class SeriesAdapter(BaseAdapter):
    def get_nodes(self):
        # Iterate through series with shared extraction logic
        pass

# Hierarchical Adapter (Nested structure)
class HierarchicalAdapter(BaseAdapter):
    def get_nodes(self):
        # Extract parent and child nodes
        pass
    
    def get_edges(self):
        # Create parent-child relationships
        pass
""",
                "extraction_strategy": """
def design_extraction_strategy(data_analysis):
    strategy = {
        'primary_extraction': determine_primary_extraction_method(data_analysis),
        'fallback_methods': identify_fallback_methods(data_analysis),
        'error_handling': design_error_handling(data_analysis),
        'validation_rules': create_validation_rules(data_analysis)
    }
    return strategy
"""
            },
            "outputs_expected": [
                "Architecture choice (Simple/Series/Hierarchical/Custom)",
                "Extraction strategy document"
            ]
        },
        3: {
            "phase_name": "Implementation",
            "detailed_instructions": [
                "3.1 Base Adapter Template:",
                "   - Create adaptive adapter implementation template",
                "   - Implement data source analysis method",
                "   - Implement strategy design method",
                "   - Implement node and edge generation methods",
                "",
                "3.2 Implementation Patterns:",
                "   - Pattern 1: Field Mapping - Map data fields to schema properties",
                "   - Pattern 2: Conditional Extraction - Extract data using conditional rules",
                "   - Pattern 3: Progressive Fallback - Try multiple extraction methods"
            ],
            "code_examples": {
                "base_template": """
class AdaptiveAdapter(BaseAdapter):
    def __init__(self, data_source, schema_config):
        self.data_source = data_source
        self.schema_config = schema_config
        self.data_analysis = self.analyze_data_source()
        self.extraction_strategy = self.design_strategy()
    
    def analyze_data_source(self):
        # Implement based on data source type
        pass
    
    def design_strategy(self):
        # Implement based on analysis results
        pass
    
    def get_nodes(self):
        # Implement using designed strategy
        pass
    
    def get_edges(self):
        # Implement if relationships are present
        pass
""",
                "field_mapping": """
def map_fields_to_schema(self, data_item, field_mapping):
    attributes = {}
    for schema_prop, data_fields in field_mapping.items():
        for field in data_fields:
            value = self.extract_field(data_item, field)
            if value is not None:
                attributes[schema_prop] = value
                break
    return attributes
"""
            },
            "outputs_expected": [
                "Working adapter code",
                "Field mapping configuration"
            ]
        },
        4: {
            "phase_name": "Quality Assurance",
            "detailed_instructions": [
                "4.1 Adaptive Testing Strategy:",
                "   - Create test suite based on data characteristics",
                "   - Implement schema compliance tests",
                "   - Add data-specific tests (relationships, temporal, hierarchical)",
                "",
                "4.2 Validation Framework:",
                "   - Create adaptive validation framework",
                "   - Implement validation rules based on data characteristics",
                "   - Apply validation to adapter output"
            ],
            "code_examples": {
                "testing_strategy": """
def create_adaptive_test_suite(adapter, data_characteristics):
    tests = []
    
    # Schema compliance tests
    tests.extend(create_schema_tests(adapter))
    
    # Data quality tests based on characteristics
    if data_characteristics['has_relationships']:
        tests.extend(create_relationship_tests(adapter))
    
    if data_characteristics['has_temporal_data']:
        tests.extend(create_temporal_tests(adapter))
    
    return tests
""",
                "validation_framework": """
class AdaptiveValidator:
    def __init__(self, data_characteristics):
        self.characteristics = data_characteristics
        self.validation_rules = self.create_validation_rules()
    
    def create_validation_rules(self):
        rules = []
        rules.append(SchemaComplianceRule())
        
        if self.characteristics['has_relationships']:
            rules.append(RelationshipIntegrityRule())
        
        return rules
"""
            },
            "outputs_expected": [
                "Test suite",
                "Validation results"
            ]
        },
        5: {
            "phase_name": "Documentation and Maintenance",
            "detailed_instructions": [
                "5.1 Adaptive Documentation:",
                "   - Generate documentation based on adapter characteristics",
                "   - Create overview and data structure documentation",
                "   - Document extraction strategy and usage examples",
                "   - Create troubleshooting guide",
                "",
                "5.2 Maintenance Planning:",
                "   - Plan for future updates and modifications",
                "   - Document decision rationale for future reference"
            ],
            "code_examples": {
                "documentation_generation": """
def generate_adaptive_documentation(adapter, data_analysis):
    doc = {
        'overview': create_overview(adapter, data_analysis),
        'data_structure': document_data_structure(data_analysis),
        'extraction_strategy': document_strategy(adapter),
        'usage_examples': create_examples(adapter),
        'troubleshooting': create_troubleshooting_guide(adapter)
    }
    return doc
"""
            },
            "outputs_expected": [
                "Implementation documentation",
                "Usage examples", 
                "Troubleshooting guide"
            ]
        }
    }
    
    if phase_number not in phase_guidance:
        return {
            "error": f"Phase {phase_number} not found. Available phases: 1-5",
            "available_phases": list(phase_guidance.keys())
        }
    
    return phase_guidance[phase_number]


def get_implementation_patterns(pattern_type: Optional[str] = None) -> Dict[str, Any]:
    """
    Provides implementation patterns for different data scenarios.
    
    Args:
        pattern_type: Optional specific pattern type to retrieve
        
    Returns:
        Dict containing implementation patterns
    """
    patterns = {
        "field_mapping": {
            "name": "Field Mapping Pattern",
            "description": "Map data fields to schema properties using flexible mapping",
            "use_case": "When data fields don't exactly match schema properties",
            "code": """
def map_fields_to_schema(self, data_item, field_mapping):
    attributes = {}
    for schema_prop, data_fields in field_mapping.items():
        for field in data_fields:
            value = self.extract_field(data_item, field)
            if value is not None:
                attributes[schema_prop] = value
                break
    return attributes
""",
            "example_mapping": {
                "name": ["title", "name", "label"],
                "description": ["desc", "description", "summary"],
                "identifier": ["id", "identifier", "uid"]
            }
        },
        "conditional_extraction": {
            "name": "Conditional Extraction Pattern", 
            "description": "Extract data using conditional rules based on data structure",
            "use_case": "When data structure varies or has optional fields",
            "code": """
def extract_with_conditions(self, data_item, extraction_rules):
    for rule in extraction_rules:
        if self.evaluate_condition(data_item, rule['condition']):
            return self.apply_extraction(data_item, rule['extraction'])
    return self.apply_default_extraction(data_item)
""",
            "example_rules": [
                {
                    "condition": "has_field('metadata')",
                    "extraction": "extract_from_metadata"
                },
                {
                    "condition": "has_field('properties')", 
                    "extraction": "extract_from_properties"
                }
            ]
        },
        "progressive_fallback": {
            "name": "Progressive Fallback Pattern",
            "description": "Try multiple extraction methods in order of preference",
            "use_case": "When multiple extraction strategies might work",
            "code": """
def extract_with_fallbacks(self, data_item, extraction_methods):
    for method in extraction_methods:
        try:
            result = method(data_item)
            if self.validate_result(result):
                return result
        except Exception:
            continue
    return self.get_default_value()
""",
            "example_methods": [
                "extract_primary_field",
                "extract_secondary_field", 
                "extract_computed_field",
                "extract_default_value"
            ]
        }
    }
    
    if pattern_type:
        if pattern_type in patterns:
            return patterns[pattern_type]
        else:
            return {
                "error": f"Pattern type '{pattern_type}' not found",
                "available_patterns": list(patterns.keys())
            }
    
    return patterns


def get_decision_guidance(data_characteristics: Dict[str, Any]) -> Dict[str, Any]:
    """
    Provides guidance on which implementation approach to use based on data characteristics.
    
    Args:
        data_characteristics: Dictionary describing the data source characteristics
        
    Returns:
        Dict containing decision guidance and recommendations
    """
    recommendations = []
    
    # Analyze characteristics and provide recommendations
    if data_characteristics.get("structure_type") == "flat":
        recommendations.append({
            "approach": "Simple Extraction",
            "reason": "Flat structure with consistent field names",
            "implementation": "Direct field mapping with minimal transformation"
        })
    
    if data_characteristics.get("has_multiple_resources", False):
        recommendations.append({
            "approach": "Series Extraction", 
            "reason": "Multiple resources with shared structure",
            "implementation": "Iterate through resources with shared extraction logic"
        })
    
    if data_characteristics.get("has_hierarchy", False):
        recommendations.append({
            "approach": "Hierarchical Extraction",
            "reason": "Nested data structures with parent-child relationships", 
            "implementation": "Extract parent and child nodes, create relationship edges"
        })
    
    if data_characteristics.get("has_irregular_structure", False):
        recommendations.append({
            "approach": "Custom Extraction",
            "reason": "Irregular data structures requiring complex transformation",
            "implementation": "Implement custom extraction logic with multiple fallback strategies"
        })
    
    return {
        "data_characteristics": data_characteristics,
        "recommendations": recommendations,
        "decision_framework": {
            "simple_extraction": "Single resource with flat structure, consistent field names, no complex relationships",
            "series_extraction": "Multiple resources with shared structure, consistent metadata patterns, batch processing requirements", 
            "hierarchical_extraction": "Nested data structures, parent-child relationships, complex metadata hierarchies",
            "custom_extraction": "Irregular data structures, complex transformation requirements, multiple data source integration"
        }
    }


# Create the FastMCP instance
mcp = FastMCP("biocypher_mcp")

# Register all tools
mcp.tool(get_available_workflows)
mcp.tool(get_adapter_creation_workflow)
mcp.tool(get_phase_guidance)
mcp.tool(get_implementation_patterns)
mcp.tool(get_decision_guidance)


def main():
    """Main entry point for the application."""
    mcp.run()


if __name__ == "__main__":
    main()
