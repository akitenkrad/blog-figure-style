from __future__ import annotations

import pytest

from scripts.sync_spec import extract_yaml, load_editorial_palette


def test_extract_yaml_preserves_unicode_comments_and_trailing_newline() -> None:
    yaml_block = (
        "# blog-figure-style.yaml\n"
        "styles:\n"
        "  editorial_minimal:\n"
        "    palette:\n"
        '      accent: "#d94f30"  # 朱・強調\n'
    )
    markdown = f"前文\n```yaml\n{yaml_block}```\n後文\n"

    assert extract_yaml(markdown) == yaml_block


def test_palette_loader_drops_yaml_comments_from_color_values() -> None:
    yaml_text = (
        "styles:\n"
        "  editorial_minimal:\n"
        "    palette:\n"
        '      ink: "#2b2926"  # 主線・主テキスト\n'
    )

    assert load_editorial_palette(yaml_text) == {"ink": "#2b2926"}


@pytest.mark.parametrize(
    "yaml_text",
    [
        "styles:\n  editorial_minimal:\n    palette: []\n",
        "styles:\n  editorial_minimal:\n    palette:\n      bg: 123\n",
    ],
)
def test_palette_loader_rejects_non_mapping_or_non_string_values(yaml_text: str) -> None:
    with pytest.raises(ValueError, match="palette"):
        load_editorial_palette(yaml_text)
