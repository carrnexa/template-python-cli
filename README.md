# Template | Python CLI

This repository acts as the main template for creating Python CLIs within CarrNexa. It consolidates many of the best practices and design decisions that have been established and refined over time.

## Required Software

The following software and their tested versions are required to work with this template:

| Name | Tested Versions |
| - | :-: |
| [Python](https://www.python.org/downloads/) | 3.12.10 |
| [Git](https://git-scm.com/install/) | 2.55.0 |
| [PowerShell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6) | v7.6.4 |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | 0.11.24 |

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

Then use `uv run` to execute commands. This keeps the commands the same on Windows, Linux, and macOS without requiring shell-specific activation.

```bash
uv run app --help
uv run app example
```

Direct module execution also works:

```bash
uv run python -m carrnexa.app_name --help
```

## Using a Virtual Environment

If you don't want to prefix every command with `uv run`, you can activate a Python virtual environment with the corresponding command and work from that instead.

| Environment | Activation Command |
| - | - |
| Linux/macOS | `source .venv/bin/activate` |
| PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Command Prompt | `.\.venv\Scripts\activate.bat` |

Once active, the previously mentioned commands become:

```bash
app --help
app example
python -m carrnexa.app_name --help
```

## Git Hooks

Install `pre-commit`, then copy the tracked post-commit hook into `.git/hooks`:

```bash
uv run pre-commit install
cp hooks/post-commit .git/hooks/post-commit
```

## Starting a New Project

After creating a project from this template, replace the placeholder names and metadata with the new project values.

Until a setup script is available, update these places manually:

- `project.name` in `pyproject.toml`
- `description` and repository URLs in `pyproject.toml`
- `tool.uv.build-backend.module-name`
- `project.scripts`
- `src/carrnexa/app_name`
- Imports that still reference `carrnexa.app_name`

The bundled `example` command is only there to verify the CLI wiring before you replace it with project-specific commands.

## References

The following documents provide more detailed information:

- [Release Process](docs/release-process.md)
- [Changelog Fragments](docs/changelog-fragments.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)
