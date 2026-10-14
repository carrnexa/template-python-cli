# Template | Python CLI

This is the template repository used at CarrNexa for Python command-line interface (CLI) projects.

## Required Software

The following software is required to use this repository:

| Name | Tested Versions |
| - | :-: |
| [Python](https://www.python.org/downloads/) | 3.12.10 |
| [Git](https://git-scm.com/install/) | 2.55.0 |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | 0.11.24 |

If you are using Windows, it is also recommended (and may be required) to have PowerShell 7 installed for proper script execution.

| Name | Tested Versions |
| - | :-: |
| [PowerShell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6) | 7.6.4 |

> [!NOTE]
> The software versions listed in the tables above are known to work with this repository. Other versions may work as well but it is not guaranteed.

## Quickstart

Clone the repository:

```bash
git clone git@github.com:carrnexa/template-python-cli.git
cd template-python-cli
```

Sync all dependencies:

```bash
uv sync
```

Execute commands using `uv run`. This keeps the commands the same on Windows, Linux, and macOS without requiring shell-specific activation.

```bash
uv run app -h
uv run app example -h
```

Direct module execution also works.

```bash
uv run python -m carrnexa.app_name -h
uv run python -m carrnexa.app_name example -h
```

## Using a Virtual Environment

If you don't want to prefix every command with `uv run`, you can activate a Python virtual environment instead. To do so, use the activation command from the table below that matches your shell:

| Shell | Activation Command |
| - | - |
| Bash/Zsh (Linux/macOS) | `source .venv/bin/activate` |
| PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Command Prompt | `.\.venv\Scripts\activate.bat` |

Once activated, the quickstart commands simply become:

```bash
app -h
app example -h
```

## Git Hooks

This repository uses Git hooks to run a series of checks before code is committed and pushed. If you are contributing to this project, you will need to set up the hooks locally by running the following commands:

```bash
uv run pre-commit install
cp hooks/post-commit .git/hooks/post-commit
```

## Starting a New Project

After generating a new project from this template, make sure to update all package-specific values to avoid conflicts with the original template repository.

At minimum, this includes:

- [pyproject.toml](pyproject.toml)
    - `[project]`
        - `name`
    - `[project.urls]`
    - `[tool.uv.build-backend]`
    - `[project.scripts]`
- [src/carrnexa/app_name/](src/carrnexa/app_name/)

> [!TIP]
> The `src/carrnexa/app_name/` directory should match the new project name once the namespace prefix is removed and all hyphens are replaced with underscores.

Once the updates are done, run the `uv sync` command to align all dependencies and package information with the new project configuration.

## References

The following documents provide additional information that may be useful when working on this project:

- [Release Process](docs/release-process.md)
- [Changelog Fragments](docs/changelog-fragments.md)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
