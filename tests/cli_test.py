import pytest
from typer.testing import CliRunner

from pep_pre_commit_hooks import verify_git_email

runner = CliRunner()


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_success():
    result = runner.invoke(verify_git_email.app, ["--domains", "icloud.com"])
    assert result.exit_code == 0
    assert not result.stdout


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_not_correctly_configured_email():
    result = runner.invoke(verify_git_email.app, ["--domains", "gmail.com"])
    assert result.exit_code == 1
    assert isinstance(result.exception, verify_git_email.DomainMisconfiguredError)
    expected_msg = (
        "`git config --get user.email` returned test@icloud.com, "
        "but an email address matching one of `['gmail.com']` was expected.",
    )
    assert result.exception.args == expected_msg


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_missing_domain():
    result = runner.invoke(verify_git_email.app)
    assert isinstance(result.exception, ValueError)
    assert result.exception.args == ("`domains` is required",)
