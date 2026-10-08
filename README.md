# Template | Python CLI

This is the template repository used for Python command-line interfaces (CLIs) built by CarrNexa.

## Required Software

The following software is required to use this template:

| Name | Tested Versions |
| - | :-: |
| [Python](https://www.python.org/downloads/) | 3.12.10 |
| [Git](https://git-scm.com/install/) | 2.55.0 |
| [PowerShell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6) | 7.6.4 |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | 0.11.24 |

> [!NOTE]
> The software versions listed in the table above are known to work with this repository. Other versions may work as well but it is not guaranteed.

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

This template uses Git hooks to run certain checks before code is committed and pushed. If you are contributing to this project, you need to set up the hooks locally by running the following commands:

```bash
uv run pre-commit install
cp hooks/post-commit .git/hooks/post-commit
```

## Starting a New Project

After generating a new project from this template, you will need to update all package-specific values to avoid conflicts with the original template repository.

At minimum, this includes:

- [src/carrnexa/app_name/](src/carrnexa/app_name/)
- [pyproject.toml](pyproject.toml)
    - `[project]`
        - `name`
    - `[project.urls]`
    - `[tool.uv.build-backend]`
    - `[project.scripts]`

> [!TIP]
> The `src/carrnexa/app_name/` directory and its parent should be renamed to match the new package name and namespace respectively. Additionally, any imports that reference these directories will also need to be updated to match.

Once everything has been updated, make sure to re-run the `uv sync` command to ensure all dependencies and package information are correctly synchronized.

## References

The following documents provide additional information that may be useful when working with this project:

- [Release Process](docs/release-process.md)
- [Changelog Fragments](docs/changelog-fragments.md)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
