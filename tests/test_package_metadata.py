from __future__ import annotations

from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]


def test_pyproject_declares_the_public_package_and_runtime_dependency() -> None:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["build-system"]["build-backend"] == "hatchling.build"
    assert pyproject["project"]["name"] == "blog-figure-style"
    assert pyproject["project"]["version"] == "0.1.0"
    assert pyproject["project"]["dependencies"] == ["matplotlib>=3.8"]
    assert pyproject["project"]["license"] == "MIT OR Apache-2.0"
    assert pyproject["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"] == [
        "src/blog_figure_style"
    ]


def test_pyyaml_and_pytest_are_development_only_dependencies() -> None:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    development = {dependency.lower() for dependency in pyproject["dependency-groups"]["dev"]}

    assert development == {"pytest", "pyyaml"}
