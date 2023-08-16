"""Verify a user's git email address."""
import re
import subprocess

import typer

app = typer.Typer()

_default_domains = typer.Option(
    default="",
    help="Comma-separated list of domai names (excluding @) the email has to match",
)


@app.command()
def verify_git_email(domains: str = _default_domains) -> None:
    """Ensure that the currently active git config's email matches a domain."""
    if not domains or len(domains) < 1:
        raise ValueError("`domains` is required")  # noqa: EM101, TRY003
    domains_ = domains.split(",")
    command = ("git", "config", "--get", "user.email")
    for domain in domains_:
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
