# QQR - a python library for QR code restoration

A blazingly fast QR code restoration library for Python.

[![GitHub Actions Status](https://github.com/weeebdev/qqr/workflows/CI/CD/badge.svg)](https://github.com/weeebdev/qqr/actions)
[![Code Coverage](https://codecov.io/gh/weeebdev/qqr/graph/badge.svg?branch=master)](https://codecov.io/gh/weeebdev/qqr?branch=master)
[![CodeFactor](https://www.codefactor.io/repository/github/weeebdev/qqr/badge)](https://www.codefactor.io/repository/github/weeebdev/qqr)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Docs](https://img.shields.io/badge/docs-master-blue.svg)](https://weeebdev.github.io/qqr)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/weeebdev/qqr/master)

<!-- Here qqr should be replaced with your library's name on PyPI  -->
[![PyPI version](https://badge.fury.io/py/qqr.svg)](https://badge.fury.io/py/qqr)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/qqr.svg)](https://pypi.org/project/qqr/)


## Controlling the version number with bumpversion

When you want to increment the version number for a new release use [`bumpversion`](https://github.com/peritus/bumpversion) to do it correctly across the whole library.
For example, to increment to a new patch release you would simply run

```
bumpversion patch
```

which given the [`.bumpversion.cfg`](https://github.com/weeebdev/qqr/blob/master/.bumpversion.cfg) makes a new commit that increments the release version by one patch release.
