# Embellish Folder

[![Documentation Status](https://readthedocs.org/projects/embellish-folder/badge/?version=latest)](https://embellish-folder.readthedocs.io/en/latest/?badge=latest)

![CI](https://github.com/sixty-north/embellish_folder/actions/workflows/actions.yml/badge.svg)


[![codecov](https://codecov.io/gh/sixty-north/embellish_folder/branch/master/graph/badge.svg?token=66QU3UW6N3)](https://codecov.io/gh/sixty-north/embellish_folder)

## Installation

    $ pip install embellish_folder


## Examples

Embellish a folder icon with a badge, symbol, or other image.

    >>> from embellish_folder import *
    >>> embellish_folder("/Users/janet/MyStuff", stuff_image)
    

## CI/CD

    $ bumpversion patch
    $ git push --follow-tags