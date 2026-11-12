"""Prefix the commit message with the issue reference found in the current branch name."""

import os
import re
import subprocess
import sys
from pathlib import Path

# JIRA key (ABC-123) or GitHub issue number (123) at the start of a branch segment
ISSUE_REF = re.compile(r"(?:^|/)([A-Z]{2,}-[0-9]+|[0-9]+)(?=-|$)")


def _get_issue_ref(branch: str) -> str | None:
    match = ISSUE_REF.search(branch)
    if match is None:
        return None
    return match.group(1)


def main() -> int:
    if os.environ.get("PRE_COMMIT_COMMIT_MSG_SOURCE") in {"merge", "squash"}:
        return 0

    branch = subprocess.run(
        ["git", "symbolic-ref", "--short", "-q", "HEAD"],  # noqa: S607
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()
    ref = _get_issue_ref(branch)
    if ref is None:
        return 0

    # Use "GH-123" instead of "#123" because git strips lines starting with "#" from editor messages
    prefix = f"GH-{ref}: " if ref.isdigit() else f"{ref}: "

    msg_file = Path(sys.argv[1])
    message = msg_file.read_bytes()
    if not message.startswith(prefix.encode()):
        msg_file.write_bytes(prefix.encode() + message)

    return 0


if __name__ == "__main__":
    sys.exit(main())
