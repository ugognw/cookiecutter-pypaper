from pathlib import Path
from tempfile import NamedTemporaryFile

import nox
from nox_poetry import Session
from nox_poetry import session

nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = [
    "format_check",
    "lint_check",
    "type_check",
    "test",
]


@session(python=["3.10", "3.11"])
def test(s: Session) -> None:
    s.install(".", "pytest", "pytest-cov", "pytest-datadir")
    s.run(
        "python",
        "-m",
        "pytest",
        "--cov=src/ccu",
        "--cov-report=html",
        "--cov-report=lcov",
        "--cov-report=xml",
        "--cov-report=term-missing",
        "tests",
        *s.posargs,
    )


# For some sessions, set venv_backend="none" to simply execute scripts within the existing Poetry
# environment. This requires that nox is run within `poetry shell` or using `poetry run nox ...`.
@session(venv_backend="none")
def format_fix(s: Session) -> None:
    s.run("ruff", "format", "." "--fix")


@session(venv_backend="none")
def format_check(s: Session) -> None:
    s.run("ruff", "check", ".")


@session(venv_backend="none")
def lint_fix(s: Session) -> None:
    s.run("ruff", "check", ".", "--fix")


@session(venv_backend="none")
def lint_check(s: Session) -> None:
    s.run("ruff", "check", ".")


@session(venv_backend="none")
def type_check(s: Session) -> None:
    s.run("mypy", "src", "tests", "noxfile.py")
