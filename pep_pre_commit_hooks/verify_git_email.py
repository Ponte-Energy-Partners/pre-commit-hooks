"""Verify a user's git e-mail address."""
import argparse
import re
import subprocess


def verify_git_email(domain: str) -> None:
    """Ensure that the currently active git config's e-mail matches a domain."""
    command = ("git", "config", "--get", "user.email")
    output = subprocess.check_output(command).decode().strip()
    if re.search(f".*@{re.escape(domain)}$", output):
        return
    raise DomainMisconfiguredError(command=command, output=output, domain=domain)


def cli_verify_git_email() -> None:
    """Command-line exposable to verify the git e-mail."""
    parser = argparse.ArgumentParser(
        prog="verify email",
        description=(
            "Verify that the domain of the e-mail address configured "
            "with git matches a domain"
        ),
    )
    parser.add_argument("--domain", required=True)
    args = parser.parse_args()
    verify_git_email(domain=args.domain)


class DomainMisconfiguredError(Exception):
    """Signal that the e-mail address to use with git is not configured as expected."""

    def __init__(
        self: "DomainMisconfiguredError",
        command: tuple[str, ...],
        output: str,
        domain: str,
    ) -> None:
        """Initiate the error with input command and output as well as the expected domain."""
        msg = (
            f"`{' '.join(command)}` returned {output}, "
            f"but an e-mail address matching `{domain}` was expected."
        )
        super().__init__(msg)
