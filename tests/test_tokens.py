from __future__ import annotations

import re
from pathlib import Path

import yaml

import blog_figure_style as bfs
from blog_figure_style import tokens


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "spec" / "blog-figure-style.yaml"
PALETTE_KEYS = (
    "bg",
    "ink",
    "ink_sub",
    "hair",
    "faint",
    "accent",
    "accent_dk",
    "accent_tint",
    "row_faint",
    "neutral_fill",
)


def test_generated_tokens_match_committed_yaml_spec() -> None:
    document = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    palette = document["styles"]["editorial_minimal"]["palette"]

    assert tuple(palette) == PALETTE_KEYS
    assert tokens.EDITORIAL_MINIMAL == palette
    assert {key: getattr(tokens, key.upper()) for key in PALETTE_KEYS} == palette


def test_all_exported_palette_values_are_lowercase_hex_colors() -> None:
    assert all(
        re.fullmatch(r"#[0-9a-f]{6}", value)
        for value in tokens.EDITORIAL_MINIMAL.values()
    )


def test_dark_palette_is_not_exported() -> None:
    assert not hasattr(tokens, "PALETTE_DARK")
    assert "palette_dark" not in tokens.EDITORIAL_MINIMAL


def test_public_api_reexports_version_tokens_and_mpl_helpers() -> None:
    assert bfs.__version__ == "0.1.0"
    assert bfs.EDITORIAL_MINIMAL is tokens.EDITORIAL_MINIMAL
    assert bfs.BG == tokens.BG
    assert callable(bfs.apply)
    assert callable(bfs.select_japanese_font)
