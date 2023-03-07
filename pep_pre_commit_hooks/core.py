import argparse
import re
import subprocess


def verify_git_email(domain: str) -> None:
    command = ("git", "config", "--get", "user.email")
    output = subprocess.check_output(command).decode().strip()
    if re.search(f".*@{re.escape(domain)}$", output):
        return
    else:
        raise ChildProcessError(
            f"`{' '.join(command)}` returned {output}, "
            f"but an e-mail address matching `{domain}` was expected."
        )


def cli_verify_git_email() -> None:
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
