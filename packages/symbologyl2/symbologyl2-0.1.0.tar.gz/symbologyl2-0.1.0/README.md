[![Build](https://github.com/onechronos/symbologyl2-py/actions/workflows/build.yml/badge.svg)](https://github.com/onechronos/symbologyl2-py/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/onechronos/symbologyl2-py/badge.svg)](https://coveralls.io/github/onechronos/symbologyl2-py)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/symbologyl2)](https://pypi.org/project/symbologyl2/)
[![PyPI - Format](https://img.shields.io/pypi/format/symbologyl2)](https://pypi.org/project/symbologyl2/)
[![PyPI - License](https://img.shields.io/pypi/l/symbologyl2)](https://pypi.org/project/symbologyl2/)
[![Documentation Status](https://readthedocs.org/projects/symbologyl2/badge/?version=latest)](https://symbologyl2.readthedocs.io/en/latest/?badge=latest)

# Symbology Normalization (symbologyl2-py)

## Introduction

Utility functions for parsing, normalizing, and translating between various capital market symbology types. This
library is a thin wrapper over the [symbologyl2](https://github.com/onechronos/symbologyl2) library, written in rust.

## Current Support

- [x] US equities
  - [x] CMS Concatenated/Suffix
  - [x] Nasdaq Integrated
  - [x] CQS (NYSE/CTA plan)

## Development

```
poetry shell
maturin develop
```
