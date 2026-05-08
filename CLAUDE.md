# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
Personal learning and experimentation repository focused on AI agents and the Model Context Protocol (MCP). Learning notes are kept as Markdown files alongside experimental Python code.

## Development Environment
- Python 3.13.13, managed with a virtual environment in `.venv/`
- Activate venv: `.venv/Scripts/activate` (Windows)
- IDE: PyCharm (`.idea/` is gitignored)
- No dependencies yet; when adding one, `pip install` it and then run `pip freeze --local > requirements.txt` so it's tracked alongside `pyproject.toml`

## Project Structure
- `mcp/` — Model Context Protocol experiments and learning notes
- Python source goes at the repo root or in purpose-named subdirectories
- Learning notes are Markdown files kept alongside the code they reference
- `.idea/` is the only gitignored item; add new ignore patterns as the project grows
