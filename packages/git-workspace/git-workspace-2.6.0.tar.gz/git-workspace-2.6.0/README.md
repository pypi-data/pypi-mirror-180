# Git Workspace

This script is intended to ease the development in multirepo environment. By defining a workspace file
that contains all the repositories one can easily share the environment setup without the need for manual
git clones. With git configuration user and host can also be set for the repositories. This allows one
to use e.g. multiple bitbucket repositories with different SSH keys easily without altering the host in
each git clone command.

This script also provides a command to check the overall state of the workspace (branches, untracked files etc.).
Few commands are overridden, but most are plain passthroughs to git and are run in all of the workspace
repositories.

### Installation:

```shell
pip install --user git-workspace
```
or
```shell
pip3 install git-workspace
```

### Usage

At first, create a new directory where the workspace will be initialized. There, run `git ws init` which creates a blank configuration. Fill in at least the remote configuration (examples later in this README).

For the repositories, fill those either by hand or if using Gitlab, you can use `git ws gitlab-sync` to automatically create a repository list either for a single group (and its subgroups) or for all that you have access to. `gitlab-sync` requires you to create a personal access token with Gitlab REST API access rights and supports only v4 API. The token can be saved to the systems secret storage (for details see Keyring python package documentation, but at least KWallet in KDE and Keychain in MacOS are supported). If stored, then the API TOKEN does not need to be filled in later on.

> NOTICE: Right now, only a single token can be used. Support for multiple different tokens coming soon-ish.

#### Command helps
```
Usage: git-ws [OPTIONS] COMMAND [ARGS]...

  Git Workspace

  Copyright 2021 Aki Mäkinen
  https://gitlab.com/blissfulreboot/python/git-workspace
  Licensed under MIT license

Options:
  --help  Show this message and exit.

Commands:
  autocomplete        Show the autocomplete line
  cleanup             Move repositories not included in the workspace...
  clone               Clone the repositories listed in the workspace...
  command             Run a command in each workspace git directory
  default-and-update  Stash potential changes, switch to the default...
  gitlab
  gitlab-sync         Sync the workspace to match the state of the gitlab...
  init                Initialize a new blank workspace
  state               Print the state of the repositories in the workspace

```
```
Usage: git-ws gitlab [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  sync  Sync the workspace to match the state of the gitlab group
```

#### Configuration

In contrast to the first version of this tool, the configuration resides now in a single YAML file. The format is:

```yaml
repositories: []
remote:
  gituser: ''
  githost: ''
  api_url: ''
  insecure: false
gitlab-integration:
  fetch-archived: <boolean, by default the sync no longer fetches archived repositories>
  suppress-insecure-warning: <boolean, suppresses the urllib3 insecure warnings if set to true>
```

where the repository entries are

```yaml
- path: some/repository/path.git 
  directory: some/repository/path
  default_branch: main
```

If the directory is defined for the repository entry, then the repository will be cloned there, otherwise the structure will be flattened. The default branch is used for the `git ws state` currently and defaults to `main` if not defined.

Example:

```yaml
# The remote configuration for gitlab.com using ssh (which is the only officially supported right now)
repositories: []
remote:
  gituser: git
  githost: gitlab.com
  api_url: https://gitlab.com/api/v4/
  insecure: false
```

### New features in 2.3.1
* Retry git clone
  * `git ws clone` now has retries for each git clone operation as well as a retry interval. These are hard coded for now, but will be configurable in the future
  * Defaults are:
    * retry count: 5
    * retry interval: 5 seconds
* Support for multiple gitlab personal access tokens
  * API URL is used as an identifier.
* EXPERIMENTAL: Support custom certificates
  * new field in the configuration under `remote`: `custom_certificate`. This is the absolute path to the file used for verification.
  * The `custom_certificate` field overrides the `insecure` field
* EXPERIMENTAL: autocompletion for `git-ws` command
  * Does not work with `git ws`. See help (`git-ws` or `git ws`) for details.