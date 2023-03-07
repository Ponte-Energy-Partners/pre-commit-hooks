import contextlib
import os
import subprocess
import tempfile

import pytest

import pep_pre_commit_hooks.core as core


@contextlib.contextmanager
def temp_git_dir():
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        try:
            os.chdir(tmp)
            subprocess.check_call(("git", "init"))
            yield
        finally:
            # Change the directory back to home on any occasion
            os.chdir(cwd)


def test_verify_domain():
    with temp_git_dir():
        subprocess.check_call(("git", "config", "user.email", "test@icloud.com"))
        assert core.verify_git_email("icloud.com") is None


def test_failed_verify_domain():
    with temp_git_dir():
        subprocess.check_call(("git", "config", "user.email", "test@me.com"))
        with pytest.raises(ChildProcessError, match="but an e-mail address matching "):
            core.verify_git_email("icloud.com")
