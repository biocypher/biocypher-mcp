def test_reality():
    """Basic reality check test."""
    assert 1 == 1


def test_imports():
    """Test that the main module can be imported."""
    try:
        from biocypher_mcp.main import mcp
        assert mcp is not None
    except ImportError as e:
        assert False, f"Failed to import main module: {e}"
