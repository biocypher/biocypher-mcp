"""
Tests for the pinned snapshot of the BioCypher LLM guides.
"""

import asyncio
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from biocypher_mcp.biocypher_docs import (
    BIOCYPHER_DOCS_REF,
    BIOCYPHER_DOCS_URL,
    DOCS_TOPICS,
    KNOWLEDGE_DIR,
    SOURCE_FILE,
    get_biocypher_docs,
    rewrite_links,
    snapshot_ref,
)
from biocypher_mcp.main import (
    get_adapter_creation_workflow,
    get_available_workflows,
    get_implementation_patterns,
    get_phase_guidance,
    get_resource_management_guidance,
    get_schema_configuration_guidance,
    mcp,
)

MAIN_PY = Path(__file__).parent.parent / "src" / "biocypher_mcp" / "main.py"


def _guidance_output() -> str:
    outputs = [
        get_available_workflows(),
        get_adapter_creation_workflow(),
        get_implementation_patterns(),
        get_schema_configuration_guidance(),
        get_resource_management_guidance(),
    ]
    outputs += [get_phase_guidance(n) for n in range(1, 6)]
    return json.dumps(outputs)


class TestSnapshot:
    def test_every_topic_has_a_file(self):
        for topic, spec in DOCS_TOPICS.items():
            path = KNOWLEDGE_DIR / spec["file"]
            assert path.is_file(), f"{topic}: {path} missing, run the sync script"
            assert path.read_text(encoding="utf-8").strip()

    def test_no_stray_files(self):
        expected = {spec["file"] for spec in DOCS_TOPICS.values()} | {SOURCE_FILE.name}
        assert {p.name for p in KNOWLEDGE_DIR.iterdir()} == expected

    def test_snapshot_matches_pinned_ref(self):
        assert snapshot_ref() == BIOCYPHER_DOCS_REF

    def test_source_lists_served_files(self):
        source = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))
        assert source["files"] == sorted(s["file"] for s in DOCS_TOPICS.values())

    def test_no_links_to_served_guides(self):
        # Links between served guides must point to get_biocypher_docs, not the web.
        served = {spec["file"] for spec in DOCS_TOPICS.values()}
        for spec in DOCS_TOPICS.values():
            text = (KNOWLEDGE_DIR / spec["file"]).read_text(encoding="utf-8")
            linked = set(
                re.findall(re.escape(BIOCYPHER_DOCS_URL) + r"/([\w.-]+)", text)
            )
            assert not linked & served, f"{spec['file']} links to {linked & served}"


class TestRewriteLinks:
    def test_markdown_link(self):
        text = f"- [Adapters]({BIOCYPHER_DOCS_URL}/llms-adapters.txt): formats"
        assert rewrite_links(text) == (
            '- Adapters (get_biocypher_docs(topic="adapters")): formats'
        )

    def test_bare_link(self):
        text = f"index: {BIOCYPHER_DOCS_URL}/llms.txt"
        assert rewrite_links(text) == 'index: get_biocypher_docs(topic="index")'

    def test_unserved_guide_keeps_url(self):
        text = f"Runnable example: {BIOCYPHER_DOCS_URL}/llms-example-adapter.txt"
        assert rewrite_links(text) == text

    def test_other_links_unchanged(self):
        text = "see https://biocypher.org/BioCypher/reference/schema-config/"
        assert rewrite_links(text) == text


class TestGetBiocypherDocs:
    @pytest.mark.parametrize("topic", sorted(DOCS_TOPICS))
    def test_returns_snapshot_content(self, topic):
        result = get_biocypher_docs(topic)
        expected = (KNOWLEDGE_DIR / DOCS_TOPICS[topic]["file"]).read_text(
            encoding="utf-8"
        )
        assert result["topic"] == topic
        assert result["content"] == expected
        assert result["source"]["ref"] == BIOCYPHER_DOCS_REF
        assert BIOCYPHER_DOCS_REF in result["source"]["url"]
        assert topic not in result["other_topics"]

    def test_default_is_index(self):
        assert get_biocypher_docs()["topic"] == "index"

    def test_unknown_topic(self):
        result = get_biocypher_docs("example_adapter")
        assert "error" in result
        assert set(result["available_topics"]) == set(DOCS_TOPICS)

    def test_registered_as_tool_with_topic_enum(self):
        async def get_tools():
            return await mcp.get_tools()

        tools = asyncio.run(get_tools())
        assert "get_biocypher_docs" in tools
        schema = tools["get_biocypher_docs"].parameters
        assert set(schema["properties"]["topic"]["enum"]) == set(DOCS_TOPICS)

    def test_listed_in_available_workflows(self):
        tools = [t["tool"] for t in get_available_workflows()["supporting_tools"]]
        assert "get_biocypher_docs" in tools


class TestGuidanceReferences:
    """Guidance points to get_biocypher_docs, not to web copies of the guides."""

    def test_no_links_to_guides(self):
        for text in (MAIN_PY.read_text(), _guidance_output()):
            assert "biocypher.org/BioCypher/llms" not in text
            assert "biocypher.org/BioCypher/agents" not in text

    def test_topic_references_are_valid(self):
        topics = set(
            re.findall(r'get_biocypher_docs\(topic=\\?"(\w+)\\?"\)', _guidance_output())
        )
        assert topics, "expected references to get_biocypher_docs"
        assert topics <= set(DOCS_TOPICS)

    def test_no_nonexistent_download_functions(self):
        # The pitfalls guide lists download_and_cache_*() as APIs that do not exist.
        assert "download_and_cache_" not in _guidance_output()


@pytest.mark.network
def test_snapshot_matches_upstream():
    """Re-download the guides at the pinned ref and compare with the snapshot."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
    from sync_biocypher_docs import build_snapshot

    for file_name, content in build_snapshot().items():
        assert (KNOWLEDGE_DIR / file_name).read_text(encoding="utf-8") == content
