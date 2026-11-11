from __future__ import annotations

from pathlib import Path
import subprocess
import sys

from scripts.sync_spec import render_tokens


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "sync_spec.py"
YAML_TEXT = (
    "# blog-figure-style.yaml\n"
    "styles:\n"
    "  editorial_minimal:\n"
    "    palette:\n"
    '      bg: "#fcfbf8"\n'
)


def run_sync(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *arguments],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_writing_the_same_source_twice_is_idempotent(tmp_path: Path) -> None:
    source = tmp_path / "design.md"
    spec = tmp_path / "style.yaml"
    tokens = tmp_path / "tokens.py"
    source.write_text(f"```yaml\n{YAML_TEXT}```\n", encoding="utf-8")
    arguments = (
        "--source",
        str(source),
        "--spec",
        str(spec),
        "--tokens",
        str(tokens),
    )

    first = run_sync(*arguments)
    first_contents = (spec.read_bytes(), tokens.read_bytes())
    second = run_sync(*arguments)

    assert first.returncode == second.returncode == 0
    assert (spec.read_bytes(), tokens.read_bytes()) == first_contents


def test_check_uses_committed_spec_when_canonical_source_is_missing(
    tmp_path: Path,
) -> None:
    source = tmp_path / "missing.md"
    spec = tmp_path / "style.yaml"
    tokens = tmp_path / "tokens.py"
    spec.write_text(YAML_TEXT, encoding="utf-8")
    tokens.write_text(render_tokens(YAML_TEXT), encoding="utf-8")
    before = (spec.stat().st_mtime_ns, tokens.stat().st_mtime_ns)

    result = run_sync(
        "--check",
        "--source",
        str(source),
        "--spec",
        str(spec),
        "--tokens",
        str(tokens),
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "canonical Markdown is not available" in result.stderr
    assert (spec.stat().st_mtime_ns, tokens.stat().st_mtime_ns) == before
