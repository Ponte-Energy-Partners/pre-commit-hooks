import argparse
import re
import subprocess
import typing


def verify_git_email(domain: str) -> typing.Literal[True]:
    command = ("git", "config", "--get", "user.email")
    output = subprocess.check_output(command).decode().strip()
    if re.search(f".*@{re.escape(domain)}$", output):
        return True
    else:
        raise ChildProcessError(
            f"Output for command `{' '.join(command)}` returned {output}, "
            f"but an e-mail address matching `{domain}` was expected."
        )


def cli_verify_git_email() -> typing.Literal[True]:
    parser = argparse.ArgumentParser(
        prog="verify email",
        description=(
            "Verify that the domain of the e-mail address configured "
            "with git matches a domain"
        ),
    )
    parser.add_argument("--domain", required=True)
    args = parser.parse_args()
    return verify_git_email(domain=args.domain)
