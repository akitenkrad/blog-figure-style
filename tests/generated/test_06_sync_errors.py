from __future__ import annotations

import pytest

from scripts.sync_spec import extract_yaml, load_editorial_palette


@pytest.mark.parametrize(
    "markdown",
    [
        "",
        "```yaml\nstyles: {}\n```\n",
        "```python\n# blog-figure-style.yaml\nstyles = {}\n```\n",
        (
            "```yaml\n# blog-figure-style.yaml\nstyles: {}\n```\n"
            "```yaml\n# blog-figure-style.yaml\nstyles: {}\n```\n"
        ),
    ],
)
def test_extract_yaml_rejects_missing_or_ambiguous_marked_blocks(markdown: str) -> None:
    with pytest.raises(ValueError, match="expected exactly one YAML block"):
        extract_yaml(markdown)


def test_extract_yaml_reports_an_unclosed_marked_fence() -> None:
    markdown = "```yaml\n# blog-figure-style.yaml\nstyles: {}\n"

    with pytest.raises(ValueError, match="no closing fence"):
        extract_yaml(markdown)


def test_palette_loader_reports_a_missing_editorial_palette() -> None:
    with pytest.raises(ValueError, match="styles.editorial_minimal.palette"):
        load_editorial_palette("styles: {}\n")
