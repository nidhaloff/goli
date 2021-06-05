# goli

<div align="center">

[![Build status](https://github.com/nidhaloff/goli/workflows/build/badge.svg?branch=master&event=push)](https://github.com/nidhaloff/goli/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/goli.svg)](https://pypi.org/project/goli/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/nidhaloff/goli/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/nidhaloff/goli/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/nidhaloff/goli/releases)
[![License](https://img.shields.io/github/license/nidhaloff/goli)](https://github.com/nidhaloff/goli/blob/master/LICENSE)

A sophisticated boilerplate generator based on best practices modern templates

</div>

> **_NOTE:_**  The project is heavily inspired by cookiecutter and aim to make a good collection of modern boilerplate templates that proven useful in the last years.


## Installation

```bash
pip install -U goli
```

or install with `Poetry`

```bash
poetry add goli
```

Then you can run `goli --help ` to show the help message on how to use the package

```bash

Usage: goli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  languages  Show all supported programming languages
  new        Generate new boilerplate code for your project
  topics     Show all supported topics.
```
As you can see, goli provides three commands. The languages and topics commands are additional to get more information about how to use the package. The new command is the most important and it is used to start a new project. More on that in the next section.

## Usage

goli provides the new command, which is used to create a new boilerplate depending on two optional parameters that you need to provide. 

- The `language` parameter, which indicates the programming language you want to use or you will use for your project. You can check supported languages if you run `goli languages`

- The `topic` parameter, which should indicate the topic of your project. You can check the topics supported by goli if you run `goli topics`

```bash
goli new --help
```

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/nidhaloff/goli/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

For Pull Request this labels are configured, by default:

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/nidhaloff/goli/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.
