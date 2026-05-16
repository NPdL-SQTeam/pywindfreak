# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`pywindfreak` is a Python 3.9+ project managed with [uv](https://docs.astral.sh/uv/).

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

Source is in `pywindfreak/`. As the project grows, move to a `src/pywindfreak/` layout and add tests in `tests/`.

- `pywindfreak/enums.py` — `ReferenceMode` enum (shared by all drivers)
- `pywindfreak/synthhd_mini.py` — `SynthHDMini` single-channel driver
- `pywindfreak/synthhd.py` — `SynthHD` two-channel driver (covers SynthHD and SynthHD PRO)
- `pywindfreak/__init__.py` — re-exports `ReferenceMode`, `SynthHDMini`, `SynthHD`

## Key dependency

- `pyserial` — USB/serial communication with Windfreak devices
