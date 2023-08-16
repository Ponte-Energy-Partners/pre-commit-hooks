## 1.0.0 (2023-08-16)

### Feat

- **verify-git-email**: Breaking: Allow multiple domains
- support for python 3.9 as well
- **verify-git-email**: add executable and pre-commit hook for verifying the email used in the git config

### Fix

- **verify-git-email**: link correct executable after renaming of module
- **verify-git-email**: raise proper exit on success
- **verify-git-email**: wrong spelling of pre-commit-hook file
- **verify-git-email**: actually using that hook

### Refactor

- **verify-git-email**: use typer
- **verify-git-email**: re-name test file to reflect source structure
- **verify-git-email**: use git's spelling of email
- **poetry**: use latest release to put version number in `poetry.lock`
- **verify-git-email**: omitting elese if last statement is more pythonic
- **verify-git-email**: more concise error
- end all files with newline
