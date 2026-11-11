from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from types import SimpleNamespace

import matplotlib

matplotlib.use("Agg", force=True)
from matplotlib import pyplot as plt, rcParams  # noqa: E402
import pytest  # noqa: E402

from blog_figure_style import mpl  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
LEGACY_STYLE = (
    Path(os.environ["BFS_LEGACY_STYLE"]) if os.environ.get("BFS_LEGACY_STYLE") else None
)  # a pre-migration style.py to compare against; the comparison is skipped when unset
RC_KEYS = (
    "figure.facecolor",
    "axes.facecolor",
    "savefig.facecolor",
    "text.color",
    "axes.labelcolor",
    "axes.edgecolor",
    "axes.linewidth",
    "axes.spines.top",
    "axes.spines.right",
    "font.family",
    "font.sans-serif",
    "font.size",
    "xtick.color",
    "ytick.color",
    "xtick.labelsize",
    "ytick.labelsize",
    "legend.frameon",
    "legend.fontsize",
    "lines.linewidth",
    "svg.fonttype",
)


def test_select_japanese_font_uses_declared_fallback_order(monkeypatch) -> None:
    installed = [SimpleNamespace(name="Yu Gothic"), SimpleNamespace(name="MS Gothic")]
    monkeypatch.setattr(mpl.font_manager.fontManager, "ttflist", installed)

    assert mpl.select_japanese_font() == "Yu Gothic"


def test_select_japanese_font_raises_when_no_fallback_is_installed(monkeypatch) -> None:
    monkeypatch.setattr(
        mpl.font_manager.fontManager,
        "ttflist",
        [SimpleNamespace(name="Unrelated Font")],
    )

    with pytest.raises(RuntimeError, match="No supported Japanese font is installed"):
        mpl.select_japanese_font()


def test_apply_matches_legacy_rcparams_when_legacy_source_is_available() -> None:
    if LEGACY_STYLE is None or not LEGACY_STYLE.exists():
        pytest.skip(f"legacy style source is not available: {LEGACY_STYLE}")

    module_spec = importlib.util.spec_from_file_location("legacy_style", LEGACY_STYLE)
    assert module_spec is not None and module_spec.loader is not None
    legacy = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(legacy)

    with matplotlib.rc_context():
        legacy_font = legacy.apply_editorial_minimal()
        legacy_values = {key: rcParams[key] for key in RC_KEYS}

    with matplotlib.rc_context():
        selected_font = mpl.apply()
        actual_values = {key: rcParams[key] for key in RC_KEYS}

    assert selected_font == legacy_font
    assert actual_values == legacy_values


def test_apply_can_render_a_small_png_with_agg(tmp_path: Path) -> None:
    output = tmp_path / "smoke.png"

    with matplotlib.rc_context():
        selected_font = mpl.apply()
        figure, axes = plt.subplots()
        axes.plot([0, 1, 2], [0, 1, 0])
        figure.savefig(output)
        plt.close(figure)

    assert selected_font in mpl.JAPANESE_FONT_FALLBACKS
    assert output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
