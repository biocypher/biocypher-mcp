################################################################################
# biocypher_mcp/biocypher_docs.py
# Serves a pinned snapshot of the BioCypher guides for AI assistants.
################################################################################
"""Pinned snapshot of the BioCypher LLM guides.

The guides are owned by the BioCypher repository (``docs/agents/``). This module
records which commit the snapshot was taken from and which file belongs to
which topic. ``scripts/sync_biocypher_docs.py`` copies the files into
``knowledge/`` and rewrites the links between them into ``get_biocypher_docs``
calls, so the server never needs network access to serve them.

To update the snapshot, change ``BIOCYPHER_DOCS_REF`` and re-run the script.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, Literal

BIOCYPHER_DOCS_REPO = "biocypher/biocypher"

# Commit the snapshot was taken from (head of biocypher #605).
BIOCYPHER_DOCS_REF = "2652a1f245e99447999b4187cacebcd0d2eb1094"

BIOCYPHER_DOCS_DIR = "docs/agents"

# Where the guides are published on the web; links to them are rewritten.
BIOCYPHER_DOCS_URL = "https://biocypher.org/BioCypher/agents"

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"
SOURCE_FILE = KNOWLEDGE_DIR / "SOURCE.json"

DocsTopic = Literal[
    "index", "adapters", "schema_config", "biocypher_config", "pitfalls"
]

# The example adapter guide (llms-example-adapter.txt) is left out on purpose:
# the project generated from the cookiecutter template is the working example,
# and serving a second one would let the two drift apart.
DOCS_TOPICS: Dict[str, Dict[str, str]] = {
    "index": {
        "file": "llms.txt",
        "description": "Index, core facts and a minimal pipeline. Start here.",
    },
    "adapters": {
        "file": "llms-adapters.txt",
        "description": "Node and edge tuple formats, how BioCypher filters and "
        "deduplicates them, downloading and caching, testing an adapter.",
    },
    "schema_config": {
        "file": "llms-schema-config.txt",
        "description": "schema_config.yaml fields, class naming, list-valued "
        "fields, relationships as nodes, strict mode.",
    },
    "biocypher_config": {
        "file": "llms-biocypher-config.txt",
        "description": "biocypher_config.yaml loading and merging, output "
        "backends, offline and online mode, headless mode.",
    },
    "pitfalls": {
        "file": "llms-pitfalls.txt",
        "description": "Known bugs with workarounds, silent data loss, "
        "configuration surprises, APIs that do not exist.",
    },
}

_FILE_TO_TOPIC = {spec["file"]: topic for topic, spec in DOCS_TOPICS.items()}

_GUIDE_URL = re.compile(re.escape(BIOCYPHER_DOCS_URL) + r"/(llms[\w-]*\.txt)")
_MARKDOWN_GUIDE_LINK = re.compile(
    r"\[([^\]]+)\]\(" + re.escape(BIOCYPHER_DOCS_URL) + r"/(llms[\w-]*\.txt)\)"
)


def topic_call(topic: str) -> str:
    """How a guide refers to another topic once it is in the snapshot."""
    return f'get_biocypher_docs(topic="{topic}")'


def rewrite_links(text: str) -> str:
    """Replace links to served guides with ``get_biocypher_docs`` calls.

    Links to guides that are not served (such as the example adapter) keep
    their URL.
    """

    def markdown(match: re.Match) -> str:
        topic = _FILE_TO_TOPIC.get(match.group(2))
        if topic is None:
            return match.group(0)
        return f"{match.group(1)} ({topic_call(topic)})"

    def bare(match: re.Match) -> str:
        topic = _FILE_TO_TOPIC.get(match.group(1))
        return match.group(0) if topic is None else topic_call(topic)

    text = _MARKDOWN_GUIDE_LINK.sub(markdown, text)
    return _GUIDE_URL.sub(bare, text)


def source_url(file_name: str) -> str:
    """URL of a guide at the pinned commit."""
    return (
        f"https://github.com/{BIOCYPHER_DOCS_REPO}/blob/{BIOCYPHER_DOCS_REF}/"
        f"{BIOCYPHER_DOCS_DIR}/{file_name}"
    )


def get_biocypher_docs(topic: DocsTopic = "index") -> Dict[str, Any]:
    """
    Returns a BioCypher guide for AI assistants, from a snapshot pinned to a
    known BioCypher commit.

    Read "index" first. Use "adapters" for node and edge tuple formats,
    "schema_config" for schema_config.yaml, "biocypher_config" for
    biocypher_config.yaml and output backends, and "pitfalls" for known bugs and
    APIs that do not exist. Check generated code against "pitfalls".

    Args:
        topic: One of "index", "adapters", "schema_config", "biocypher_config",
            "pitfalls"

    Returns:
        Dict with the guide's Markdown content and where it comes from
    """
    if topic not in DOCS_TOPICS:
        return {
            "error": f"Unknown topic {topic!r}.",
            "available_topics": {t: s["description"] for t, s in DOCS_TOPICS.items()},
        }

    spec = DOCS_TOPICS[topic]
    content = (KNOWLEDGE_DIR / spec["file"]).read_text(encoding="utf-8")
    return {
        "topic": topic,
        "description": spec["description"],
        "content": content,
        "source": {
            "repository": BIOCYPHER_DOCS_REPO,
            "ref": BIOCYPHER_DOCS_REF,
            "url": source_url(spec["file"]),
        },
        "other_topics": {
            t: s["description"] for t, s in DOCS_TOPICS.items() if t != topic
        },
    }


def snapshot_ref() -> str:
    """The commit recorded by the last sync."""
    return json.loads(SOURCE_FILE.read_text(encoding="utf-8"))["ref"]
