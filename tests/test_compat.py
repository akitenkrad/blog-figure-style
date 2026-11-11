from __future__ import annotations

from blog_figure_style import compat, tokens


def test_legacy_color_names_alias_generated_tokens() -> None:
    assert compat.BACKGROUND == tokens.BG
    assert compat.INK == tokens.INK
    assert compat.MUTED == tokens.INK_SUB
    assert compat.HAIRLINE == tokens.HAIR
    assert compat.SERIF_NUMERAL == tokens.FAINT
    assert compat.ACCENT == tokens.ACCENT
    assert compat.ACCENT_TEXT == tokens.ACCENT_DK
    assert compat.ACCENT_FILL == tokens.ACCENT_TINT
    assert compat.NEUTRAL_FILL == tokens.NEUTRAL_FILL
    assert compat.TABLE_RULE == tokens.ROW_FAINT
    assert compat.PURPLE == tokens.ACCENT_DK
    assert compat.TEAL == tokens.INK
    assert compat.GRAY == tokens.INK_SUB


def test_legacy_apply_names_delegate_with_original_return_contract(monkeypatch) -> None:
    calls: list[str] = []
    monkeypatch.setattr(compat, "apply", lambda: calls.append("apply") or "Test Font")

    assert compat.apply_editorial_minimal() == "Test Font"
    assert compat.apply_style() is None
    assert calls == ["apply", "apply"]
