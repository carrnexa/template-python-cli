# Changelog Fragments

This repository uses fragment-based changelog management. Rather than editing `CHANGELOG.md` directly during feature development, developers add entries to fragment files within the `changes/` directory. The fragments are compiled into `CHANGELOG.md` during release preparation.

## Layout

Each branch has its own directory named after the branch, with `/` replaced by `-`. Each category has its own file, and each entry is a single `-` bullet line.

```text
changes/
    fix-34-auth-fails-on-azure/
        fixed.md
    feature-package-config/
        added.md
        changed.md
```

| Category | Heading | Purpose |
| - | - | - |
| `breaking` | Breaking Changes | Incompatible API, CLI flag, or configuration changes. |
| `added` | Added | New user-facing features or CLI commands. |
| `changed` | Changed | Changes to existing functionality that remain backward compatible. |
| `deprecated` | Deprecated | Features or flags that will be removed in a future version. |
| `removed` | Removed | Features or flags that have been removed. |
| `fixed` | Fixed | Bug fixes. |
| `security` | Security | Vulnerability fixes and security updates. |
