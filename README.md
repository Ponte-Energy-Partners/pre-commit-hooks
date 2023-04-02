Public pre-commit hooks developed at Ponte Energy Partners


## Available hooks

### `verify-git-email`

This hook verifies that a committer's email address matches a domain.

This hook can serve two use cases:
- Ensure people hide their private email addresses, e.g. by using the respective [GitHub setting](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address). `--domain` is set to `users.noreply.github.com` by default to cover this use case. Note that GitHub provides a way to [block pushes that contain private email addresses](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address) that are enforced on push, while this hook enforces on commit.

- Ensure that people within an organisation commit with their org email address instead of their private address. This is most useful for private repositories where the email does not need to be hidden and where people should be prevented to accidentially commit with their private email address.

### `mypy-with-poetry`

Runs mypy with your system's `poetry` executable (through `language: system`). The advantage over the [mypy mirror repo](https://github.com/pre-commit/mirrors-mypy#using-mypy-with-pre-commit) is that the virtual environment configured with poetry gets used instead of one that pre-commit manages (with `language: python`). That way, you don't need to configure `additional_dependencies:` for the mypy hook to work. The hook `mypy-with-poetry` requires

* either [`files`](https://mypy.readthedocs.io/en/stable/config_file.html#confval-files) to be specified in `pyproject.toml`, e.g. like this:

    ```toml
    [tool.mypy]

    files = "."
    ```
* or `.` to be passed as an additional argument to the hook in `.pre-commit-config.yaml` like this:

    ```yaml
    repos:
      - repo: https://github.com/Ponte-Energy-Partners/pre-commit-hooks
        rev: 4305ba8
        hooks:
        - id: mypy-with-poetry
          args: [.]
    ```


## How to use the hooks

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
