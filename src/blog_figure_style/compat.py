"""Compatibility names for styles copied into earlier experiment repositories."""
from __future__ import annotations

from .mpl import apply
from .tokens import (
    ACCENT,
    ACCENT_DK,
    ACCENT_TINT,
    BG,
    FAINT,
    HAIR,
    INK,
    INK_SUB,
    NEUTRAL_FILL,
    ROW_FAINT,
)


BACKGROUND = BG
MUTED = INK_SUB
HAIRLINE = HAIR
SERIF_NUMERAL = FAINT
ACCENT_TEXT = ACCENT_DK
ACCENT_FILL = ACCENT_TINT
TABLE_RULE = ROW_FAINT

PURPLE = ACCENT_DK
TEAL = INK
GRAY = INK_SUB


def apply_editorial_minimal() -> str:
    """Apply the style under its legacy function name."""
    return apply()


def apply_style() -> None:
    """Apply the style while preserving the rumor helper's return contract."""
    apply()


__all__ = [
    "ACCENT",
    "ACCENT_FILL",
    "ACCENT_TEXT",
    "BACKGROUND",
    "GRAY",
    "HAIRLINE",
    "INK",
    "MUTED",
    "NEUTRAL_FILL",
    "PURPLE",
    "SERIF_NUMERAL",
    "TABLE_RULE",
    "TEAL",
    "apply_editorial_minimal",
    "apply_style",
]
