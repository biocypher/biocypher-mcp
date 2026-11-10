"""Copy the BioCypher LLM guides into the MCP's knowledge snapshot.

Downloads each guide listed in ``DOCS_TOPICS`` from the BioCypher repository at
``BIOCYPHER_DOCS_REF``, rewrites links between guides into ``get_biocypher_docs``
calls, and writes the result to ``src/biocypher_mcp/knowledge/``.

Usage (from the repository root):

    uv run python scripts/sync_biocypher_docs.py

To move to a newer version of the guides, change ``BIOCYPHER_DOCS_REF`` in
``src/biocypher_mcp/biocypher_docs.py`` first, then run this script and commit
the changed files.
"""

import json
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from biocypher_mcp.biocypher_docs import (  # noqa: E402
    BIOCYPHER_DOCS_DIR,
    BIOCYPHER_DOCS_REF,
    BIOCYPHER_DOCS_REPO,
    DOCS_TOPICS,
    KNOWLEDGE_DIR,
    SOURCE_FILE,
    rewrite_links,
)


def raw_url(file_name: str, ref: str = BIOCYPHER_DOCS_REF) -> str:
    return (
        f"https://raw.githubusercontent.com/{BIOCYPHER_DOCS_REPO}/{ref}/"
        f"{BIOCYPHER_DOCS_DIR}/{file_name}"
    )


def fetch(file_name: str, ref: str = BIOCYPHER_DOCS_REF) -> str:
    response = requests.get(raw_url(file_name, ref), timeout=30)
    response.raise_for_status()
    return response.text


def build_snapshot(ref: str = BIOCYPHER_DOCS_REF) -> dict[str, str]:
    """Return {file name: rewritten content} for every served topic."""
    return {
        spec["file"]: rewrite_links(fetch(spec["file"], ref))
        for spec in DOCS_TOPICS.values()
    }


def main() -> None:
    snapshot = build_snapshot()
    KNOWLEDGE_DIR.mkdir(exist_ok=True)

    expected = set(snapshot) | {SOURCE_FILE.name}
    for path in KNOWLEDGE_DIR.iterdir():
        if path.name not in expected:
            path.unlink()
            print(f"removed {path.name}")

    for file_name, content in snapshot.items():
        (KNOWLEDGE_DIR / file_name).write_text(content, encoding="utf-8")
        print(f"wrote {file_name}")

    SOURCE_FILE.write_text(
        json.dumps(
            {
                "repository": BIOCYPHER_DOCS_REPO,
                "ref": BIOCYPHER_DOCS_REF,
                "path": BIOCYPHER_DOCS_DIR,
                "files": sorted(snapshot),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"snapshot pinned to {BIOCYPHER_DOCS_REPO}@{BIOCYPHER_DOCS_REF}")


if __name__ == "__main__":
    main()
