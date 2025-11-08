"""
Web server for exposing BioCypher MCP tools via HTTP.

This module provides a FastAPI server that exposes the BioCypher MCP tools
as REST API endpoints, making them accessible via HTTP at the /mcp directory.
"""

from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from .main import (
    get_available_workflows,
    get_adapter_creation_workflow,
    get_phase_guidance,
    get_implementation_patterns,
    get_decision_guidance,
    check_project_exists,
    get_cookiecutter_instructions
)


# Pydantic models for request/response validation
class DataCharacteristics(BaseModel):
    """Model for data characteristics used in decision guidance."""
    structure_type: Optional[str] = None
    has_multiple_resources: Optional[bool] = None
    has_hierarchy: Optional[bool] = None
    has_irregular_structure: Optional[bool] = None
    has_temporal_data: Optional[bool] = None
    has_relationships: Optional[bool] = None
    has_required_fields: Optional[bool] = None


class ErrorResponse(BaseModel):
    """Model for error responses."""
    error: str
    detail: Optional[str] = None


class ProjectPathRequest(BaseModel):
    """Model for project path check requests."""
    project_path: str = "."


# Create FastAPI app
app = FastAPI(
    title="BioCypher MCP Server",
    description="A web server exposing BioCypher MCP tools for adapter creation workflows",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=Dict[str, Any])
async def root():
    """Root endpoint providing an overview of the MCP server."""
    return {
        "name": "BioCypher MCP Server",
        "description": "Web server exposing BioCypher MCP tools for adapter creation workflows",
        "version": "0.1.0",
        "endpoints": {
            "workflows": "/workflows",
            "workflow_details": "/workflows/adapter-creation",
            "phase_guidance": "/phases/{phase_number}",
            "patterns": "/patterns",
            "patterns_specific": "/patterns/{pattern_type}",
            "decision_guidance": "/decision-guidance",
            "check_project": "/project/check",
            "cookiecutter_instructions": "/project/cookiecutter-instructions",
            "docs": "/docs"
        }
    }


@app.get("/workflows", response_model=Dict[str, Any])
async def get_workflows():
    """Get available BioCypher workflows."""
    try:
        return get_available_workflows()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving workflows: {str(e)}")


@app.get("/workflows/adapter-creation", response_model=Dict[str, Any])
async def get_adapter_workflow():
    """Get detailed information about the adapter creation workflow."""
    try:
        return get_adapter_creation_workflow()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving workflow: {str(e)}")


@app.get("/phases/{phase_number}", response_model=Dict[str, Any])
async def get_phase(phase_number: int):
    """Get detailed guidance for a specific phase."""
    try:
        result = get_phase_guidance(phase_number)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving phase guidance: {str(e)}")


@app.get("/patterns", response_model=Dict[str, Any])
async def get_patterns():
    """Get all implementation patterns."""
    try:
        return get_implementation_patterns()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving patterns: {str(e)}")


@app.get("/patterns/{pattern_type}", response_model=Dict[str, Any])
async def get_specific_pattern(pattern_type: str):
    """Get a specific implementation pattern."""
    try:
        result = get_implementation_patterns(pattern_type)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving pattern: {str(e)}")


@app.post("/decision-guidance", response_model=Dict[str, Any])
async def get_decision(data_characteristics: DataCharacteristics):
    """Get decision guidance based on data characteristics."""
    try:
        # Convert Pydantic model to dict, excluding None values
        data_dict = {k: v for k, v in data_characteristics.model_dump().items() if v is not None}
        return get_decision_guidance(data_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating decision guidance: {str(e)}")


@app.post("/project/check", response_model=Dict[str, Any])
async def check_project(request: ProjectPathRequest):
    """Check if a BioCypher project exists at the given path."""
    try:
        return check_project_exists(request.project_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking project: {str(e)}")


@app.get("/project/cookiecutter-instructions", response_model=Dict[str, Any])
async def get_cookiecutter_info():
    """Get instructions for creating a BioCypher project using cookiecutter."""
    try:
        return get_cookiecutter_instructions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving instructions: {str(e)}")


@app.get("/health", response_model=Dict[str, str])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "biocypher-mcp"}


def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """Run the web server."""
    uvicorn.run(
        "biocypher_mcp.web_server:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


if __name__ == "__main__":
    run_server()
