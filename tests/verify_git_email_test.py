import pytest

from pep_pre_commit_hooks import verify_git_email


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


@pytest.fixture(params=(("--domain", "@live.com"),))
def domain(request):
    return request.param


def test__parse_args(domain):
    assert verify_git_email._parse_args(domain).domain == domain[1]
