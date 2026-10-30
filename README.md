# Template | Python CLI

CarrNexa's template repository for Python CLI projects.

## Required Software

The following software is required to use this repository:

| Name | Tested Versions | Notes |
| - | :-: | - |
| [Python](https://www.python.org/downloads/) | 3.12.10 | |
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | 0.11.24 | |
| [Git](https://git-scm.com/install/) | 2.55.0 | Only needed if cloning or contributing |
| [PowerShell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell?view=powershell-7.6) | 7.6.4 | For Windows users only |

> [!NOTE]
> The software versions listed above are known to work with this repository. Other versions may work as well, but it's not guaranteed.

## Using This Template

Generate a new project from this template with one of the following methods:

- **GitHub Web**: Go to [carrnexa/template-python-cli](https://github.com/carrnexa/template-python-cli) on GitHub and click the "Use this template" button in the top right corner.
- **GitHub CLI**: Utilize the GitHub CLI template feature by running:

    ```bash
    gh repo create <new-repo-name> --template carrnexa/template-python-cli --clone
    ```

- **Git Clone**: Create an empty GitHub repository first, then clone the template repository and push it up to your remote.

    ```bash
    git clone git@github.com:carrnexa/template-python-cli.git <new-repo-name>
    cd <new-repo-name>
    git remote set-url origin git@github.com:carrnexa/<new-repo-name>.git
    git push -u origin main
    ```

- **Direct Download**: Create an empty GitHub repository first, then download the template repository as a ZIP file from GitHub, extract it, and push it up to your remote.

    ```bash
    # Assuming the ZIP file has been extracted into the <new-repo-name> directory
    cd <new-repo-name>
    git init
    git branch -M main
    git remote add origin git@github.com:carrnexa/<new-repo-name>.git
    git add .
    git commit -m "Initial commit from template"
    git push -u origin main
    ```

Once generated, update all package-specific values to avoid conflicts with the original template repository. At minimum, this includes:

- [pyproject.toml](pyproject.toml)
    - `[project]`
        - `name`
    - `[project.urls]`
    - `[tool.uv.build-backend]`
    - `[project.scripts]`
- [src/carrnexa/app_name/](src/carrnexa/app_name/)

> [!TIP]
> The `src/carrnexa/app_name/` directory should match the new project name once the namespace prefix is removed and all hyphens are replaced with underscores. For example, if your new project name is `carrnexa-new-project`, the directory should be renamed to `src/carrnexa/new_project/`.

After those updates are made, run `uv sync` to align dependencies and package information with the new project configuration; then, remove this section and update any remaining references below.

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

View available app commands and their usage:

```bash
# Project Script Usage (Recommended)
uv run app -h
uv run app example -h

# Direct Module Execution
uv run python -m carrnexa.app_name -h
uv run python -m carrnexa.app_name example -h
```

## Using a Virtual Environment

If you don't want to prefix every package-related command with `uv run`, you can activate a Python virtual environment instead.

Some common shell environments and their corresponding activation commands are listed below:

| Shell | Activation Command |
| - | - |
| Bash/Zsh (Linux/macOS) | `source .venv/bin/activate` |
| PowerShell | `.\.venv\Scripts\activate.ps1` |
| Command Prompt | `.\.venv\Scripts\activate.bat` |

Once activated, the quickstart commands simply become:

```bash
app -h
app example -h
```

> [!NOTE]
> Any environment-specific commands shown in a document will be prefixed with `uv run` unless stated otherwise. Doing so ensures compatibility across different operating systems and shell environments.

## Git Hooks

This repository uses Git hooks to run a series of checks before code is committed and pushed. If you are contributing to this project, you will need to set up the hooks locally by running the following commands:

```bash
uv run pre-commit install
cp hooks/post-commit .git/hooks/post-commit
```

## References

The following documents provide additional information that may be useful when working on this project:

- [Release Process](docs/release-process.md)
- [Changelog Fragments](docs/changelog-fragments.md)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
