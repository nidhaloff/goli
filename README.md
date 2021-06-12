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

A sophisticated boilerplate generator based on best practices and modern useful templates

</div>

> **_NOTE:_**  The project is heavily inspired by cookiecutter and aim to make a good collection of modern boilerplate templates that proven useful in the last years.

## Why another boilerplate generator?
I like the cookiecutter package and I have been using it for years now. However, the field is changing too fast and many cookiecutter templates that I have been using are now outdated. So I find myself always searching for new templates and wasting time by searching on google, github etc.. for modern templates based on best practices (like which package to use for testing, format etc..)

Hence, I wanted to create this simple tool, where I integrated all useful templates that have proven useful in the last years and which follow best practices in the field.

Please note that goli is not only for python. It can be used with other languages too and I'm planning to add other features in the future.

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

For example, here is what my command will look like if I'm starting a data science project using python

```bash
goli new --language python --topic data-science
```
or the short version

```bash
goli new -l python -t data-science
```

This will pull the modern cookiecutter-data-science template (https://github.com/drivendata/cookiecutter-data-science) and execute it in your current working directory. So you don't have to search for templates since best practices are already built-in and being updated regularly. 
 
## FAQ

### I want to add a useful template that I didn't find in goli

If you want to contribute and add templates, just go to `goli/cookiecutters.py`, add your template as a class member variable and finally add it in the repos dictionary under the corresponding language and topic.
