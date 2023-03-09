import os
import subprocess

import pytest

import pep_pre_commit_hooks.core as core


@pytest.fixture
def ch_tempdir(tmp_path):
    """
    Temporarily change the working directory to a temporary directory.
    """
    cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        yield
    finally:
        os.chdir(cwd)


@pytest.fixture
def temp_git_dir(ch_tempdir):
    subprocess.check_call(("git", "init"))


@pytest.fixture
def temp_git_dir_icloud_email(temp_git_dir):
    subprocess.check_call(("git", "config", "user.email", "test@icloud.com"))


def test_verify_domain(temp_git_dir_icloud_email):
    assert core.verify_git_email("icloud.com") is None


def test_failed_verify_domain(temp_git_dir_icloud_email):
    with pytest.raises(ChildProcessError, match="but an e-mail address matching "):
        core.verify_git_email("hotmail.com")
