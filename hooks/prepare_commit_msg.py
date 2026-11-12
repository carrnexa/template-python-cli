"""Prefix the commit message with the issue reference found in the current branch name."""

import os
import re
import subprocess
import sys
from pathlib import Path

# JIRA key (ABC-123) or GitHub issue number (123) at the start of a branch segment
ISSUE_REF = re.compile(r"(?:^|/)([A-Z]{2,}-[0-9]+|[0-9]+)(?=-|$)")


def extract_issue_reference(branch_name: str) -> str | None:
    """Search for an issue reference in the branch name and return it if found.

    Args:
        branch_name (str): The name of the current branch.

    Returns:
        str | None: The issue reference if found, otherwise None.
    """
    match = ISSUE_REF.search(branch_name)
    if match is None:
        return None
    return match.group(1)


def main() -> int:
    # Skip commit message modification for merge or squash commits
    if os.environ.get("PRE_COMMIT_COMMIT_MSG_SOURCE") in {"merge", "squash"}:
        return 0

    branch_name = subprocess.run(
        ["git", "symbolic-ref", "--short", "-q", "HEAD"],  # noqa: S607
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()

    issue_reference = extract_issue_reference(branch_name)
    if issue_reference is None:
        return 0

    # Prefix a raw number (GitHub format) with "GH-" instead of "#" since git can strip those lines
    if issue_reference.isdigit():
        issue_reference = f"GH-{issue_reference}"
    commit_message_prefix = f"{issue_reference}: ".encode()

    msg_file = Path(sys.argv[1])
    commit_message = msg_file.read_bytes()
    if not commit_message.startswith(commit_message_prefix):
        msg_file.write_bytes(commit_message_prefix + commit_message)

    return 0


if __name__ == "__main__":
    sys.exit(main())


__all__ = [
    "extract_issue_reference",
]
