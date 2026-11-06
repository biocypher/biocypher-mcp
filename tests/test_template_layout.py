"""
Check the expected project layout against the pinned cookiecutter template.

These tests clone the template and need network access. They are skipped by
default; run them with `pytest -m network`.
"""

from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

from biocypher_mcp.main import (
    TEMPLATE_COMMIT,
    TEMPLATE_URL,
    get_expected_project_structure,
)


@pytest.mark.network
@pytest.mark.parametrize(
    ("include_docker", "include_tests"),
    [("y", "y"), ("n", "y"), ("y", "n"), ("n", "n")],
)
def test_expected_structure_matches_template(tmp_path, include_docker, include_tests):
    """Test that the listed files and directories are exactly what is generated."""
    expected = get_expected_project_structure(
        "synthetic-ppi",
        include_docker=include_docker,
        include_tests=include_tests,
    )

    project = Path(
        cookiecutter(
            TEMPLATE_URL,
            checkout=TEMPLATE_COMMIT,
            no_input=True,
            output_dir=str(tmp_path),
            extra_context={
                "project_name": expected["project_name"],
                "package_name": expected["package_name"],
                "adapter_name": expected["adapter_name"],
                "include_docker": include_docker,
                "include_tests": include_tests,
            },
        )
    )

    paths = [
        path
        for path in project.rglob("*")
        if ".git" not in path.relative_to(project).parts
    ]
    files = {path.relative_to(project).as_posix() for path in paths if path.is_file()}
    directories = {
        f"{path.relative_to(project).as_posix()}/" for path in paths if path.is_dir()
    }

    assert project.name == expected["expected_structure"]["root"].rstrip("/")
    assert files == set(expected["expected_structure"]["files"])
    assert directories == set(expected["expected_structure"]["directories"])
