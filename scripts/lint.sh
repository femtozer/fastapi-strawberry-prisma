#!/usr/bin/env bash
set -x
set -e
flake8 app
black app --check
isort app --check-only
mypy app
