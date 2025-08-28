#!/usr/bin/env python3
"""
Example usage of the BioCypher MCP hierarchical tools.

This script demonstrates how to navigate through the BioCypher workflow
using the new tool-based approach instead of resources.
"""

from biocypher_mcp.main import (
    get_available_workflows,
    get_adapter_creation_workflow,
    get_phase_guidance,
    get_implementation_patterns,
    get_decision_guidance
)


def main():
    """Demonstrate the hierarchical tool navigation."""
    
    print("=== BioCypher MCP Tool Example ===\n")
    
    # 1. Start with available workflows
    print("1. Discovering available workflows...")
    workflows = get_available_workflows()
    
    print(f"   Found {len(workflows['workflows'])} workflow(s):")
    for workflow in workflows['workflows']:
        print(f"   - {workflow['name']}: {workflow['description']}")
    
    print(f"\n   Framework: {workflows['framework_overview']['name']}")
    print(f"   Core principles: {', '.join(workflows['framework_overview']['core_principles'])}")
    
    # 2. Get detailed workflow information
    print("\n2. Getting detailed workflow information...")
    workflow = get_adapter_creation_workflow()
    
    print(f"   Workflow: {workflow['name']}")
    print(f"   Description: {workflow['description']}")
    print(f"   Number of phases: {len(workflow['phases'])}")
    
    print("\n   Phases:")
    for phase in workflow['phases']:
        print(f"   - Phase {phase['phase']}: {phase['name']}")
        print(f"     Activities: {', '.join(phase['key_activities'])}")
    
    # 3. Get guidance for a specific phase
    print("\n3. Getting detailed guidance for Phase 1...")
    phase_1 = get_phase_guidance(1)
    
    print(f"   Phase: {phase_1['phase_name']}")
    print(f"   Number of instructions: {len(phase_1['detailed_instructions'])}")
    print(f"   Code examples available: {list(phase_1['code_examples'].keys())}")
    
    print("\n   First instruction:")
    print(f"   {phase_1['detailed_instructions'][0]}")
    
    # 4. Get implementation patterns
    print("\n4. Getting implementation patterns...")
    patterns = get_implementation_patterns()
    
    print(f"   Available patterns: {list(patterns.keys())}")
    
    field_mapping = get_implementation_patterns("field_mapping")
    print(f"\n   Field Mapping Pattern:")
    print(f"   - Name: {field_mapping['name']}")
    print(f"   - Use case: {field_mapping['use_case']}")
    print(f"   - Example mapping: {field_mapping['example_mapping']}")
    
    # 5. Get decision guidance
    print("\n5. Getting decision guidance...")
    
    # Test with different data characteristics
    test_cases = [
        {"structure_type": "flat", "has_multiple_resources": False},
        {"has_multiple_resources": True, "has_hierarchy": False},
        {"has_hierarchy": True, "has_irregular_structure": False},
        {"has_irregular_structure": True}
    ]
    
    for i, data_chars in enumerate(test_cases, 1):
        print(f"\n   Test case {i}: {data_chars}")
        guidance = get_decision_guidance(data_chars)
        
        print(f"   Recommendations:")
        for rec in guidance['recommendations']:
            print(f"   - {rec['approach']}: {rec['reason']}")
    
    print("\n=== Example completed successfully! ===")
    print("\nThis demonstrates how the hierarchical MCP tools provide:")
    print("- Structured workflow navigation")
    print("- Detailed phase-specific guidance")
    print("- Reusable implementation patterns")
    print("- Context-aware decision recommendations")


if __name__ == "__main__":
    main()
