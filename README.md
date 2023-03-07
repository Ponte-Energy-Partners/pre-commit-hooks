Public pre-commit hooks developed at Ponte Energy Partners

You can include the hooks like this in your repo:

```yaml
# in .pre-commit-config.yaml in your git repo root
repos:

  - repo: https://github.com/Ponte-Energy-Partners/pre-commit-hooks
    rev: 4305ba8
    hooks:
      - id: verify-git-email
        args: [--domain=ponte-energy.de]
      - id: mypy-with-poetry
```

The hook `mypy-with-poetry` requires `files` to be specified in `pyproject.toml`, e.g. like this:

```toml
[tool.mypy]

files = "."
```
