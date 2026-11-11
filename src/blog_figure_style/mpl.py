"""Matplotlib configuration for the editorial-minimal figure style."""
from __future__ import annotations

from matplotlib import font_manager, rcParams

from . import tokens


JAPANESE_FONT_FALLBACKS = [
    "Hiragino Sans",
    "Noto Sans CJK JP",
    "IPAexGothic",
    "Yu Gothic",
    "MS Gothic",
    "Arial Unicode MS",
]


def select_japanese_font() -> str:
    """Select the first installed font in the declared Japanese fallback list."""
    installed = {font.name for font in font_manager.fontManager.ttflist}
    for family in JAPANESE_FONT_FALLBACKS:
        if family in installed:
            return family
    raise RuntimeError(
        "No supported Japanese font is installed; tried: "
        + ", ".join(JAPANESE_FONT_FALLBACKS)
    )


def apply() -> str:
    """Apply editorial-minimal rcParams and return the selected Japanese font."""
    japanese_font = select_japanese_font()
    rcParams.update(
        {
            "figure.facecolor": tokens.BG,
            "axes.facecolor": tokens.BG,
            "savefig.facecolor": tokens.BG,
            "text.color": tokens.INK,
            "axes.labelcolor": tokens.INK,
            "axes.edgecolor": tokens.HAIR,
            "axes.linewidth": 0.6,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.family": "sans-serif",
            "font.sans-serif": JAPANESE_FONT_FALLBACKS,
            "font.size": 14,
            "xtick.color": tokens.INK_SUB,
            "ytick.color": tokens.INK_SUB,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
            "legend.frameon": False,
            "legend.fontsize": 11,
            "lines.linewidth": 1.5,
            "svg.fonttype": "none",
        }
    )
    return japanese_font


__all__ = ["JAPANESE_FONT_FALLBACKS", "apply", "select_japanese_font"]
