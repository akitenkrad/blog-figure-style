"""Shared Blog Figure Design System tokens and matplotlib styling."""
from __future__ import annotations

from .mpl import JAPANESE_FONT_FALLBACKS, apply, select_japanese_font
from .tokens import (
    ACCENT,
    ACCENT_DK,
    ACCENT_TINT,
    BG,
    EDITORIAL_MINIMAL,
    FAINT,
    HAIR,
    INK,
    INK_SUB,
    NEUTRAL_FILL,
    ROW_FAINT,
)


__version__ = "0.1.0"

__all__ = [
    "ACCENT",
    "ACCENT_DK",
    "ACCENT_TINT",
    "BG",
    "EDITORIAL_MINIMAL",
    "FAINT",
    "HAIR",
    "INK",
    "INK_SUB",
    "JAPANESE_FONT_FALLBACKS",
    "NEUTRAL_FILL",
    "ROW_FAINT",
    "__version__",
    "apply",
    "select_japanese_font",
]
