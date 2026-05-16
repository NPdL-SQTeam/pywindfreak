# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`pywindfreak` is a Python 3.13 project managed with [uv](https://docs.astral.sh/uv/).

## Commands

```bash
# Install dependencies
uv sync

# Add a dependency
uv add <package>

# Run a script or module
uv run python <file.py>

# Run tests (once a test framework is added)
uv run pytest

# Run a single test
uv run pytest path/to/test_file.py::test_name
```

## Structure

Source files live at the project root alongside `__init__.py`. As the project grows, move source into a `src/pywindfreak/` layout and tests into `tests/`.

- `synthhd_mini.py` — `SynthHDMini` driver class and `ReferenceMode` enum
- `__init__.py` — re-exports `SynthHDMini` and `ReferenceMode`

## Key dependency

- `pyserial` — USB/serial communication with the SynthHD Mini
