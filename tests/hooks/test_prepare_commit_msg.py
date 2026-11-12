import prepare_commit_msg
import pytest


@pytest.mark.parametrize(
    ("branch_name", "expected_issue_reference"),
    [
        ("feature/34-add-v2-api", "34"),
        ("34-quick-fix", "34"),
        ("fix/34", "34"),
        ("feature/ABC-7-config", "ABC-7"),
        ("ABC-123-login", "ABC-123"),
        ("main", None),
        ("feature/add-v2-api", None),
        ("release/v1.6.0", None),
        ("fix/oauth2-ABC-123", None),
        ("fix/abc-123-login", None),
        ("dependabot/pip/ruff-0.15.21", None),
    ],
)
def test_extract_issue_reference(branch_name: str, expected_issue_reference: str | None) -> None:
    issue_reference = prepare_commit_msg.extract_issue_reference(branch_name)
    assert issue_reference == expected_issue_reference
