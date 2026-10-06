# CarrNexa Python CLI Template

This is the Python CLI template for CarrNexa projects.

New Python-based command-line interfaces (CLIs) should be created from this template. Starting here keeps the project shape and default settings consistent. The rest of this README covers local setup, day-to-day commands, and related project documentation.

## Prerequisites

- **Python**: [Tested with 3.12.10](https://www.python.org/downloads/)
- **Git**: [Tested with 2.55.0](https://git-scm.com/install/)
- **PowerShell 7**: [Tested with 7.6.4](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6)
- **uv**: [Tested with 0.11.24](https://docs.astral.sh/uv/getting-started/installation/)

## Quickstart

Clone the repository:

```bash
git clone git@github.com:carrnexa/template-python-cli.git
cd template-python-cli
```

Sync dependencies:

```bash
uv sync
```

Use `uv run` for normal local commands. This keeps the commands the same on Windows, Linux, and macOS without requiring shell-specific activation.

```bash
uv run app --help
uv run app example
```

Direct module execution also works:

```bash
uv run python -m carrnexa.app_name --help
```

## Optional: Activate the Virtual Environment

If you prefer to work inside the virtual environment instead of prefixing commands with `uv run`, use the command that matches your shell.

Unix shells:

```bash
source .venv/bin/activate
```

Windows PowerShell 7:

```pwsh
.\.venv\Scripts\Activate.ps1
```

Once the environment is active, the commands become:

```bash
app --help
app example
```

## Git Hooks

Install `pre-commit`, then copy the tracked post-commit hook into `.git/hooks`:

```bash
uv run pre-commit install
cp hooks/post-commit .git/hooks/post-commit
```

## Starting a New Project

After creating a project from this template, replace the placeholder names and metadata with the new project values.

Until the setup script is available, update these places manually:

- `project.name` in `pyproject.toml`
- `description` and repository URLs in `pyproject.toml`
- `tool.uv.build-backend.module-name`
- `project.scripts`
- `src/carrnexa/app_name`
- Imports that still reference `carrnexa.app_name`

The bundled `example` command is only there to verify the CLI wiring before you replace it with project-specific commands.

## Reference

- [Release Process](docs/release-process.md)
- [Changelog Fragments](docs/changelog-fragments.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)
