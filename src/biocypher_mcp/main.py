################################################################################
# biocypher_mcp/main.py
# This module provides a FastMCP wrapper for the biocypher API
################################################################################
import json
from typing import Any, Dict, List, Optional, Union
import requests
from fastmcp import FastMCP


# API WRAPPER SECTION, in case you need to interact with API
def fetch_records_paged(
    endpoint: str,
    max_page_size: int = 100,
    projection: Optional[Union[str, List[str]]] = None,
    page_token: Optional[str] = None,
    filter_criteria: Optional[Dict[str, Any]] = None,
    additional_params: Optional[Dict[str, Any]] = None,
    max_records: Optional[int] = None,
    verbose: bool = False,
) -> List[Dict[str, Any]]:
    """
    This function retrieves records from the biocypher API, handling pagination
    automatically to return the complete set of results.

    Args:
        endpoint: API endpoint to query.
        max_page_size: Maximum number of records to retrieve per API call.
        projection: Fields to include in the response. Can be a comma-separated string
            or a list of field names.
        page_token: Token for retrieving a specific page of results, typically
            obtained from a previous response.
        filter_criteria: MongoDB-style query dictionary for filtering results.
        additional_params: Additional query parameters to include in the API request.
        max_records: Maximum total number of records to retrieve across all pages.
        verbose: If True, print progress information during retrieval.

    Returns:
        A list of dictionaries, where each dictionary represents a record.
    """
    base_url: str = "https://biocypher.org/mcp"

    all_records = []
    endpoint_url = f"{base_url}/{endpoint}"
    params = {"max_page_size": max_page_size}

    if projection:
        if isinstance(projection, list):
            params["projection"] = ",".join(projection)
        else:
            params["projection"] = projection

    if page_token:
        params["page_token"] = page_token

    if filter_criteria:
        params["filter"] = json.dumps(filter_criteria)

    if additional_params:
        params.update(additional_params)

    while True:
        response = requests.get(endpoint_url, params=params)
        response.raise_for_status()
        data = response.json()

        records = data.get("resources", [])
        all_records.extend(records)

        if verbose:
            print(f"Fetched {len(records)} records; total so far: {len(all_records)}")

        # Check if we've hit the max_records limit
        if max_records is not None and len(all_records) >= max_records:
            all_records = all_records[:max_records]
            if verbose:
                print(f"Reached max_records limit: {max_records}. Stopping fetch.")
            break

        next_page_token = data.get("next_page_token")
        if next_page_token:
            params["page_token"] = next_page_token
        else:
            break

    return all_records


# MCP TOOL SECTION
def sample_tool_function(
    parameter1: str,
    parameter2: int = 10
) -> List[Dict[str, Any]]:
    """
    Sample tool function to demonstrate how to create a tool for your MCP.

    Args:
        parameter1: Description of parameter1
        parameter2: Description of parameter2, with default value

    Returns:
        List[Dict[str, Any]]: List of records matching the criteria
    """
    # Example of how to use the API wrapper
    filter_criteria = {"field1": parameter1, "field2": {"$gt": parameter2}}

    records = fetch_records_paged(
        endpoint="your_endpoint",
        filter_criteria=filter_criteria,
        max_records=parameter2,
    )

    # Process records if needed
    processed_records = []
    for record in records:
        # Process each record
        processed_record = {
            "id": record.get("id"),
            "name": record.get("name"),
            # Add other fields as needed
        }
        processed_records.append(processed_record)

    return processed_records


# MCP RESOURCES SECTION
from pathlib import Path


def get_biocypher_adapter_framework_resource() -> Dict[str, Any]:
    """
    Returns the BioCypher Adapter Creation Framework resource.
    
    Returns:
        Dict containing the resource definition and content
    """
    return {
        "uri": "https://biocypher.org/resources/adapter-creation-framework",
        "name": "adapter-creation-framework",
        "title": "BioCypher Adapter Creation Framework",
        "mimeType": "text/markdown",
        "description": "Generalized framework for creating BioCypher adapters from any data source, with adaptive analysis and implementation strategies",
        "annotations": {
            "audience": ["user", "assistant"],
            "priority": 0.9,
            "lastModified": "2025-01-12T15:00:58Z"
        }
    }


def get_biocypher_adapter_framework_content() -> str:
    """
    Returns the content of the BioCypher Adapter Creation Framework.
    
    Returns:
        String containing the markdown content
    """
    # Get the path to the resources directory
    current_dir = Path(__file__).parent
    resource_file = current_dir / "resources" / "adapter_framework.md"
    
    try:
        with open(resource_file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "# BioCypher Adapter Creation Framework\n\nResource file not found. Please check the installation."


# MAIN SECTION
# Create the FastMCP instance
mcp = FastMCP("biocypher_mcp")

# Register all tools
mcp.tool(sample_tool_function)

# Register resources
@mcp.resource("https://biocypher.org/resources/adapter-creation-framework")
def get_adapter_framework_resource():
    """Get the BioCypher Adapter Creation Framework resource."""
    return get_biocypher_adapter_framework_resource()


@mcp.resource("https://biocypher.org/resources/adapter-creation-framework/content")
def get_adapter_framework_content():
    """Get the content of the BioCypher Adapter Creation Framework."""
    return get_biocypher_adapter_framework_content()


def main():
    """Main entry point for the application."""
    mcp.run()


if __name__ == "__main__":
    main()
