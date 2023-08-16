"""Verify a user's git email address."""
import re
import subprocess

import typer

app = typer.Typer()

_default_domain = typer.Option(
    default=[],
    help="Domain name (excluding @) the email has to match",
)


@app.command()
def verify_git_email(domains: list[str] = _default_domain) -> None:
    """Ensure that the currently active git config's email matches a domain."""
    if not domains or len(domains) < 1:
        raise ValueError("`domains` is required")  # noqa: EM101, TRY003
    command = ("git", "config", "--get", "user.email")
    for domain in domains:
        output = subprocess.check_output(command).decode().strip()
        if re.search(f".*@{re.escape(domain)}$", output):
            return
        raise DomainMisconfiguredError(command=command, output=output, domain=domain)


class DomainMisconfiguredError(Exception):
    """Signal that the email address to use with git is not configured as expected."""

    def __init__(
        self: "DomainMisconfiguredError",
        command: tuple[str, ...],
        output: str,
        domain: str,
    ) -> None:
        """Initiate the error with input command and output as well as the expected domain."""
        msg = (
            f"`{' '.join(command)}` returned {output}, "
            f"but an email address matching `{domain}` was expected."
        )
        super().__init__(msg)
