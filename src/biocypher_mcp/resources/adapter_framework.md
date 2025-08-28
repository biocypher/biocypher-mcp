# BioCypher Adapter Creation Framework

## Overview
This framework guides LLM agents in creating BioCypher adapters for any data source. The process is adaptive and data-driven, requiring analysis of the specific resource structure before implementation.

## Core Principles

### 1. Data-First Approach
- Analyze the input data structure before making implementation decisions
- Adapt the process to the specific characteristics of the data source
- No assumptions about data format, structure, or organization

### 2. Schema-Driven Development
- Use the schema configuration as the contract for adapter outputs
- If schema doesn't exist, help create one based on data analysis
- Ensure all adapter outputs align with schema requirements

### 3. Iterative Refinement
- Start with basic extraction, refine based on data quality
- Implement error handling and validation progressively
- Test and validate at each stage

## Adaptive Implementation Process

### Phase 1: Data Analysis and Understanding

#### 1.1 Resource Structure Analysis
```python
def analyze_resource_structure(data_source):
    """
    Analyze the structure of the input data source.
    Adapt analysis based on data type and format.
    """
    # Determine data source type
    if is_file_based(data_source):
        return analyze_file_structure(data_source)
    elif is_api_based(data_source):
        return analyze_api_structure(data_source)
    elif is_database_based(data_source):
        return analyze_database_structure(data_source)
    else:
        return analyze_custom_structure(data_source)
```

#### 1.2 Metadata Pattern Recognition
- **Single Resource**: Extract all available metadata fields
- **Series/Collection**: Identify shared vs. unique metadata patterns
- **Hierarchical Data**: Map parent-child relationships
- **Time Series**: Identify temporal patterns and sequences

#### 1.3 Schema Assessment
```python
def assess_schema_requirements(data_analysis, existing_schema=None):
    """
    Determine if existing schema is sufficient or needs creation/modification.
    """
    if not existing_schema:
        return create_schema_from_analysis(data_analysis)
    
    # Check if existing schema covers all data concepts
    missing_concepts = identify_missing_concepts(data_analysis, existing_schema)
    if missing_concepts:
        return extend_schema(existing_schema, missing_concepts)
    
    return existing_schema
```

### Phase 2: Implementation Strategy Design

#### 2.1 Adapter Architecture Decision
Based on data analysis, choose appropriate architecture:

**Simple Adapter** (Single resource, flat structure):
```python
class SimpleAdapter(BaseAdapter):
    def get_nodes(self):
        # Direct extraction from single resource
        pass
```

**Series Adapter** (Multiple resources, shared structure):
```python
class SeriesAdapter(BaseAdapter):
    def get_nodes(self):
        # Iterate through series with shared extraction logic
        pass
```

**Hierarchical Adapter** (Nested structure):
```python
class HierarchicalAdapter(BaseAdapter):
    def get_nodes(self):
        # Extract parent and child nodes
        pass
    
    def get_edges(self):
        # Create parent-child relationships
        pass
```

**Custom Adapter** (Complex, irregular structure):
```python
class CustomAdapter(BaseAdapter):
    def get_nodes(self):
        # Implement custom extraction logic
        pass
```

#### 2.2 Data Extraction Strategy
```python
def design_extraction_strategy(data_analysis):
    """
    Design extraction strategy based on data characteristics.
    """
    strategy = {
        'primary_extraction': determine_primary_extraction_method(data_analysis),
        'fallback_methods': identify_fallback_methods(data_analysis),
        'error_handling': design_error_handling(data_analysis),
        'validation_rules': create_validation_rules(data_analysis)
    }
    return strategy
```

### Phase 3: Implementation

#### 3.1 Base Adapter Template
```python
class AdaptiveAdapter(BaseAdapter):
    """
    Template for adaptive adapter implementation.
    """
    
    def __init__(self, data_source, schema_config):
        self.data_source = data_source
        self.schema_config = schema_config
        self.data_analysis = self.analyze_data_source()
        self.extraction_strategy = self.design_strategy()
    
    def analyze_data_source(self):
        """Analyze the data source structure."""
        # Implement based on data source type
        pass
    
    def design_strategy(self):
        """Design extraction strategy based on analysis."""
        # Implement based on analysis results
        pass
    
    def get_nodes(self):
        """Generate nodes based on designed strategy."""
        # Implement using designed strategy
        pass
    
    def get_edges(self):
        """Generate edges if relationships exist."""
        # Implement if relationships are present
        pass
```

#### 3.2 Implementation Patterns

**Pattern 1: Field Mapping**
```python
def map_fields_to_schema(self, data_item, field_mapping):
    """
    Map data fields to schema properties using flexible mapping.
    """
    attributes = {}
    for schema_prop, data_fields in field_mapping.items():
        for field in data_fields:
            value = self.extract_field(data_item, field)
            if value is not None:
                attributes[schema_prop] = value
                break
    return attributes
```

**Pattern 2: Conditional Extraction**
```python
def extract_with_conditions(self, data_item, extraction_rules):
    """
    Extract data using conditional rules based on data structure.
    """
    for rule in extraction_rules:
        if self.evaluate_condition(data_item, rule['condition']):
            return self.apply_extraction(data_item, rule['extraction'])
    return self.apply_default_extraction(data_item)
```

**Pattern 3: Progressive Fallback**
```python
def extract_with_fallbacks(self, data_item, extraction_methods):
    """
    Try multiple extraction methods in order of preference.
    """
    for method in extraction_methods:
        try:
            result = method(data_item)
            if self.validate_result(result):
                return result
        except Exception:
            continue
    return self.get_default_value()
```

### Phase 4: Quality Assurance

#### 4.1 Adaptive Testing Strategy
```python
def create_adaptive_test_suite(adapter, data_characteristics):
    """
    Create test suite based on data characteristics.
    """
    tests = []
    
    # Schema compliance tests
    tests.extend(create_schema_tests(adapter))
    
    # Data quality tests based on characteristics
    if data_characteristics['has_relationships']:
        tests.extend(create_relationship_tests(adapter))
    
    if data_characteristics['has_temporal_data']:
        tests.extend(create_temporal_tests(adapter))
    
    if data_characteristics['has_hierarchical_structure']:
        tests.extend(create_hierarchy_tests(adapter))
    
    return tests
```

#### 4.2 Validation Framework
```python
class AdaptiveValidator:
    """
    Adaptive validation framework for different data types.
    """
    
    def __init__(self, data_characteristics):
        self.characteristics = data_characteristics
        self.validation_rules = self.create_validation_rules()
    
    def create_validation_rules(self):
        """Create validation rules based on data characteristics."""
        rules = []
        
        # Basic schema compliance
        rules.append(SchemaComplianceRule())
        
        # Data-specific rules
        if self.characteristics['has_relationships']:
            rules.append(RelationshipIntegrityRule())
        
        if self.characteristics['has_required_fields']:
            rules.append(RequiredFieldsRule())
        
        return rules
    
    def validate(self, adapter_output):
        """Validate adapter output using adaptive rules."""
        for rule in self.validation_rules:
            rule.validate(adapter_output)
```

### Phase 5: Documentation and Maintenance

#### 5.1 Adaptive Documentation
```python
def generate_adaptive_documentation(adapter, data_analysis):
    """
    Generate documentation based on adapter characteristics.
    """
    doc = {
        'overview': create_overview(adapter, data_analysis),
        'data_structure': document_data_structure(data_analysis),
        'extraction_strategy': document_strategy(adapter),
        'usage_examples': create_examples(adapter),
        'troubleshooting': create_troubleshooting_guide(adapter)
    }
    return doc
```

## Implementation Guidelines

### For LLM Agents

1. **Start with Analysis**: Always analyze the data source before making implementation decisions
2. **Adapt to Structure**: Choose implementation patterns based on data characteristics
3. **Validate Continuously**: Test and validate at each implementation stage
4. **Document Decisions**: Document why specific approaches were chosen
5. **Iterate and Refine**: Improve implementation based on testing results

### Decision Framework

**When to use simple extraction:**
- Single resource with flat structure
- Consistent field names
- No complex relationships

**When to use series extraction:**
- Multiple resources with shared structure
- Consistent metadata patterns
- Batch processing requirements

**When to use hierarchical extraction:**
- Nested data structures
- Parent-child relationships
- Complex metadata hierarchies

**When to use custom extraction:**
- Irregular data structures
- Complex transformation requirements
- Multiple data source integration

## Example Workflows

### Workflow 1: Simple File-Based Data
1. Analyze file structure and format
2. Create simple adapter with direct field mapping
3. Implement basic validation
4. Test with sample data

### Workflow 2: API-Based Series Data
1. Analyze API structure and response patterns
2. Create series adapter with pagination handling
3. Implement relationship extraction
4. Add comprehensive error handling

### Workflow 3: Complex Database Integration
1. Analyze database schema and relationships
2. Create hierarchical adapter with relationship mapping
3. Implement complex validation rules
4. Add performance optimization

This framework provides the flexibility to handle any data source while maintaining the core BioCypher principles of schema compliance and data quality.
