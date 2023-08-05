# [2.6.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.5.0...v2.6.0) (2022-12-04)


### Features

* add cleanup, add gitlab command group for future ([b8817b5](https://gitlab.com/blissfulreboot/python/git-workspace/commit/b8817b57610a9baeb5b2d38ec4f32f358c0a1d53))

# [2.5.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.4.1...v2.5.0) (2022-12-01)


### Features

* **gitlab-sync:** add options for fetch-archived and to suppress urllib3 warnings ([f2a2a1c](https://gitlab.com/blissfulreboot/python/git-workspace/commit/f2a2a1c3056a55e009286309b0c5d7d74d71cd8c))

## [2.4.1](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.4.0...v2.4.1) (2022-06-12)


### Bug Fixes

* remove unused dependency ([15efa14](https://gitlab.com/blissfulreboot/python/git-workspace/commit/15efa14cecb4b8f4139aa725f806f347c3caf066))
* write the configuration to correct place, there should not be nested workspaces ([2ce2dc5](https://gitlab.com/blissfulreboot/python/git-workspace/commit/2ce2dc596ef2ce8eac40e7fa944ca3d258733d03))

# [2.4.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.3.1...v2.4.0) (2022-04-18)


### Features

* **git clone:** skip clone if target directory is not empty ([0c6d542](https://gitlab.com/blissfulreboot/python/git-workspace/commit/0c6d5425a95ca109d9f4eb5dc248be0fdef5b6e3))
* **graphops:** remove experimental graphops functionality as unnecessary ([0e7c249](https://gitlab.com/blissfulreboot/python/git-workspace/commit/0e7c24981a490c1f824c3f866aca869c256a2958))

## [2.3.1](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.3.0...v2.3.1) (2021-12-31)


### Bug Fixes

* **clone:** add retry to cloning ([c3448b7](https://gitlab.com/blissfulreboot/python/git-workspace/commit/c3448b765a575c79fab48a3f4ab0c5fa85a5e5bb))
* **gitlab:** add warning to gitlab-sync if replacing the existing repository list ([f0db4bb](https://gitlab.com/blissfulreboot/python/git-workspace/commit/f0db4bba1571196aa809ed1c4eec612ff9427fe9))
* **gitlab:** change the PAT entry to be api url specific ([66156f3](https://gitlab.com/blissfulreboot/python/git-workspace/commit/66156f3f3c550079cb5f4009381e2df142794ab7))
* **state:** catch exceptions happening when running the state command ([397f1f8](https://gitlab.com/blissfulreboot/python/git-workspace/commit/397f1f8ab48fe380523d2c49f5ed3f7d7fd1a31c))

# [2.3.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.2.0...v2.3.0) (2021-12-27)


### Features

* **autocompletion:** add basic implementation for autocompletion ([e635a55](https://gitlab.com/blissfulreboot/python/git-workspace/commit/e635a55c84b0ca4236885efaf4a81981963737b5))
* **gitlab-sync:** add support for multiple gitlab personal access tokens ([5bd8431](https://gitlab.com/blissfulreboot/python/git-workspace/commit/5bd84311a8e6f04349684bc08ba8ac7a3b563092))
* **gitlab-sync:** experimental feature: support custom certificates ([bb56859](https://gitlab.com/blissfulreboot/python/git-workspace/commit/bb5685999df62d5147e7a95e2ea33f640bf974bf))

# [2.2.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.1.0...v2.2.0) (2021-12-15)


### Features

* **git:** experimental feature: switch to default branch and pull the changes ([e09b1d4](https://gitlab.com/blissfulreboot/python/git-workspace/commit/e09b1d415bb7a90bac97294c4d4a5154352ac123))

# [2.1.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.0.5...v2.1.0) (2021-12-15)


### Features

* **graphops:** refactor and enable graphops for v2 ([ed5df3c](https://gitlab.com/blissfulreboot/python/git-workspace/commit/ed5df3cfa6668befcd2dc253f68a5a34b9139dc1))

## [2.0.5](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.0.4...v2.0.5) (2021-12-15)


### Bug Fixes

* if there is no api_token from the keyring, ask it ([57569eb](https://gitlab.com/blissfulreboot/python/git-workspace/commit/57569eba4f672ebfd73df80581f749214055111d))

## [2.0.4](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.0.3...v2.0.4) (2021-12-15)


### Bug Fixes

* **gitlab-sync:** set the  next page ([8b3a1bc](https://gitlab.com/blissfulreboot/python/git-workspace/commit/8b3a1bc0babb4adc9d91d9283355589e09ca9dbf))

## [2.0.3](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.0.2...v2.0.3) (2021-12-14)


### Bug Fixes

* change the package name and the module references ([4e61959](https://gitlab.com/blissfulreboot/python/git-workspace/commit/4e61959c7bb00e2d34adca11e3913cdab3ea1e19))

## [2.0.2](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.0.1...v2.0.2) (2021-12-14)


### Bug Fixes

* restructure the repo for packaging ([2fad36a](https://gitlab.com/blissfulreboot/python/git-workspace/commit/2fad36a6e6a3cce6ed7f644eede2ceb1899bb34e))

## [2.0.1](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v2.0.0...v2.0.1) (2021-12-14)


### Bug Fixes

* use correct development status classifier ([8f88033](https://gitlab.com/blissfulreboot/python/git-workspace/commit/8f880333db7b2f736bbe63a2348b2adcce93a0a5))

# [2.0.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.5.2...v2.0.0) (2021-12-14)


### Features

* refactor the whole tool ([cc85fba](https://gitlab.com/blissfulreboot/python/git-workspace/commit/cc85fbae5b088a19744c431121b7d0859f3edffa))


### BREAKING CHANGES

* pretty much complete overhaul

## [1.5.2](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.5.1...v1.5.2) (2020-06-25)


### Bug Fixes

* bullet was forgotten in the install_requires instead of having prompt-toolkit ([9d96ad5](https://gitlab.com/blissfulreboot/python/git-workspace/commit/9d96ad56b9d4062f2cbfdb086417749ced4ac475))

## [1.5.1](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.5.0...v1.5.1) (2020-06-25)


### Bug Fixes

* multiple fixes, see detailed commit message ([20f94ea](https://gitlab.com/blissfulreboot/python/git-workspace/commit/20f94ea206009814982cb57a0e33744f1de0453c))
* package.json directory without graphops file and operations crashes the tool ([52e40ea](https://gitlab.com/blissfulreboot/python/git-workspace/commit/52e40ea31b10c93611a5326df10dbdd7734fb0fa))

# [1.5.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.4.0...v1.5.0) (2020-06-24)


### Features

* (experimental) fully interactive graphops commands ([a5e3898](https://gitlab.com/blissfulreboot/python/git-workspace/commit/a5e38987e52b7429338182fa1b11e83f479befc3))
* Add support for package.json as a source of operations ([34906f6](https://gitlab.com/blissfulreboot/python/git-workspace/commit/34906f6b59f8a9f0815613ceac79a68126596278))

# [1.4.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.3.0...v1.4.0) (2020-06-24)


### Features

* Experimental feature: interactive operation selection ([2fab729](https://gitlab.com/blissfulreboot/python/git-workspace/commit/2fab729c3247e2e0b1c7b99dc9603c7eac98f96b))

# [1.3.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.2.0...v1.3.0) (2020-06-23)


### Bug Fixes

* print also stderr from operation scripts ([e3657f3](https://gitlab.com/blissfulreboot/python/git-workspace/commit/e3657f366c7174ef8235e5bf82a805710ec4e4ce))


### Features

* Add command to list available operations ([75a4562](https://gitlab.com/blissfulreboot/python/git-workspace/commit/75a456227209892a537799b22ad37a014f1974ee))

# [1.2.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.1.2...v1.2.0) (2020-06-22)


### Features

* define environment variables for operations ([d3b76d3](https://gitlab.com/blissfulreboot/python/git-workspace/commit/d3b76d3db9945f0b1f482669d5d6a8f57253b981))

## [1.1.2](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.1.1...v1.1.2) (2020-06-22)


### Bug Fixes

* further corrections to in repository commands ([829b2de](https://gitlab.com/blissfulreboot/python/git-workspace/commit/829b2dea1e681c135d2d03da6bbc4c06b9d8b820))

## [1.1.1](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.1.0...v1.1.1) (2020-06-22)


### Bug Fixes

* clicommand arg is being accessed wrong ([06b9376](https://gitlab.com/blissfulreboot/python/git-workspace/commit/06b937611aa8d3dbafb0a76bb4bce2614ab2d4db))

# [1.1.0](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.0.5...v1.1.0) (2020-06-21)


### Features

* add graphops pipelines ([e760c50](https://gitlab.com/blissfulreboot/python/git-workspace/commit/e760c50e6aad54bdc17df99b15b27e41599c5eeb))

## [1.0.5](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.0.4...v1.0.5) (2020-06-21)


### Bug Fixes

* install as executable script ([04eb893](https://gitlab.com/blissfulreboot/python/git-workspace/commit/04eb893fe5d7c407aadd36ac2a3593108d943375))

## [1.0.4](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.0.3...v1.0.4) (2020-06-20)


### Bug Fixes

* remove long description as a quick upload fix ([a8d40fc](https://gitlab.com/blissfulreboot/python/git-workspace/commit/a8d40fc63e1889d74aad5149dfa1370032f6519e))

## [1.0.3](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.0.2...v1.0.3) (2020-06-20)


### Bug Fixes

* add readme.md to the package_data ([6ddb220](https://gitlab.com/blissfulreboot/python/git-workspace/commit/6ddb2202a1fa25774afe3ef48ad59a1c8308c76e))

## [1.0.2](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.0.1...v1.0.2) (2020-06-20)


### Bug Fixes

* fix install: Add version and changelog.md into the bundle ([48f02d9](https://gitlab.com/blissfulreboot/python/git-workspace/commit/48f02d972ef0dfd3001ffb7d64b14a9832451b39))

## [1.0.1](https://gitlab.com/blissfulreboot/python/git-workspace/compare/v1.0.0...v1.0.1) (2020-06-20)


### Bug Fixes

* Check if repository exists when running in repository operations. ([0a47e47](https://gitlab.com/blissfulreboot/python/git-workspace/commit/0a47e4775a00e6e412cb9e1aa644ad94fce33af6))
* fix clone bug: workspace cannot be cloned unless in the workspace directory ([afe421d](https://gitlab.com/blissfulreboot/python/git-workspace/commit/afe421ddbbd881fd0389a3e08d822e30836f3ad8))
* Removed extra import, improved some prints and error handlings. ([e9dff72](https://gitlab.com/blissfulreboot/python/git-workspace/commit/e9dff7265e077e940dfd4cf72351be52a19432a5))
