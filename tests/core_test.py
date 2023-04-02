import os
import pathlib
import subprocess

import pytest

from pep_pre_commit_hooks import verify_git_email


@pytest.fixture()
def _ch_tempdir(tmp_path):
    """Temporarily change the working directory to a temporary directory."""
    cwd = pathlib.Path.cwd()
    try:
        os.chdir(tmp_path)
        yield
    finally:
        os.chdir(cwd)


@pytest.fixture()
def _git_init():
    subprocess.check_call(("git", "init"))


@pytest.fixture()
def _git_config_icloud_email():
    subprocess.check_call(("git", "config", "user.email", "test@icloud.com"))


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_verify_domain():
    assert verify_git_email.verify_git_email("icloud.com") is None


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_failed_verify_domain():
    with pytest.raises(
        verify_git_email.DomainMisconfiguredError,
        match="but an email address matching ",
    ):
        verify_git_email.verify_git_email("hotmail.com")
