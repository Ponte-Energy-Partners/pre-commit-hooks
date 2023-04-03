import os
import pathlib
import subprocess

import pytest


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
