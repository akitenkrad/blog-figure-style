# blog-figure-style

`blog-figure-style` provides the light `editorial_minimal` color tokens from the
Blog Figure Design System and applies the matching matplotlib `rcParams`. It keeps
figures made by separate experiment repositories visually consistent without copying a
local `style.py` into each repository.

Only the static, light image palette is exposed. The HTML-only dark palette and the
other design-system styles are intentionally outside this package.

## Installation

Experiment repositories should use a Git dependency pinned to a release tag. With uv,
add the package requirement and its source to the consuming project's `pyproject.toml`:

```toml
[project]
dependencies = [
  "blog-figure-style",
]

[tool.uv.sources]
blog-figure-style = { git = "https://github.com/akitenkrad/blog-figure-style.git", tag = "v0.1.0" }
```

Then lock and sync the environment:

```bash
uv lock
uv sync
```

Keep the tag explicit so that regenerating an old experiment does not silently change
its figure styling. Upgrade by changing the tag and reviewing the resulting lockfile.

## Usage

Apply the shared matplotlib settings before creating a figure:

```python
import matplotlib.pyplot as plt

from blog_figure_style import ACCENT, apply

japanese_font = apply()

figure, axes = plt.subplots()
axes.plot([0, 1, 2], [0, 1, 0], color=ACCENT)
figure.savefig("figure.png", dpi=180, bbox_inches="tight")
```

`apply()` returns the selected Japanese font family. It raises `RuntimeError` if none
of the supported fallback fonts is installed.

For gradual migration from copied helpers, import the old names from the compatibility
module:

```python
from blog_figure_style.compat import ACCENT_TEXT, BACKGROUND, apply_editorial_minimal

apply_editorial_minimal()
```

The root package exports the generated palette constants, `EDITORIAL_MINIMAL`,
`apply()`, and `select_japanese_font()`.

## Updating the tokens

The canonical source is the fenced YAML block beginning with
`# blog-figure-style.yaml` in `Blog Figure Design System.md`. PyYAML is used only by
the development-time generator; it is not a runtime dependency.

From a maintainer checkout that can access the canonical Markdown file:

```bash
.venv/bin/python scripts/sync_spec.py
.venv/bin/python scripts/sync_spec.py --check
.venv/bin/python -m pytest
```

The canonical document is looked up at `$BLOG_DESIGN_SPEC`, falling back to
`~/Documents/Obsidian/My Design/Blog Design/Blog Figure Design System.md`. Use
`--source /path/to/Blog\ Figure\ Design\ System.md` to point at another copy. The generator copies the complete YAML block to
`spec/blog-figure-style.yaml` and regenerates `tokens.py` with the source YAML SHA-256.
Do not edit `tokens.py` directly.

In a public clone without the private canonical Markdown path,
`scripts/sync_spec.py --check` verifies `tokens.py` against the committed YAML spec and
reports that the canonical-source comparison was skipped. The test suite behaves the
same way. The comparison against a pre-migration `style.py` runs only when
`BFS_LEGACY_STYLE` points at that file.

## License

Dual-licensed under either [MIT](LICENSE-MIT) or
[Apache-2.0](LICENSE-APACHE), at your option.
