# pyemllib

[![Release](https://img.shields.io/pypi/v/pyemllib.svg)](https://pypi.org/pypi/pyemllib/)
[![Build status](https://img.shields.io/github/workflow/status/jusana/pyemllib/merge-to-main)](https://img.shields.io/github/workflow/status/jusana/pyemllib/merge-to-main)
[![codecov](https://codecov.io/gh/jusana/pyemllib/branch/main/graph/badge.svg)](https://codecov.io/gh/jusana/pyemllib)
[![Commit activity](https://img.shields.io/github/commit-activity/m/jusana/pyemllib)](https://img.shields.io/github/commit-activity/m/jusana/pyemllib)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://jusana.github.io/pyemllib/)
[![Code style with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports with isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/github/license/jusana/pyemllib)](https://img.shields.io/github/license/jusana/pyemllib)

This package is a python lib to help dealing with EML - Ecological Metadata Language.

It's built uppon [dataclasses](https://docs.python.org/3.9/library/dataclasses.html) generated with [xsdata](https://github.com/tefra/xsdata) from [EML xsd](https://eml.ecoinformatics.org/schema/) hence heavily relies on xsdata capabilities

*For history reasons, i also provide the former pyxb and generateDS (built with py38) that i used to use on my projects but that i now find
more cumbersome to use than the dataclass implementation. They might be useful anyway !!*


NB: This lib is currently developped under a local gitlab forge and will be release on github on important releases
- *Github repository*: <https://github.com/jusana/pyemllib/>
- *Documentation* <https://jusana.github.io/pyemllib/>


## Main features

- Deserializes EML files to python objects
- Serializes pure python objects to EML as XML string / files
- Checks validity of EML generated against xsd 
- Generates a markdown/html DataPaper from suitable EML files
- 


## Very simple usage


```python
from emllib import EMLizer

# instantiate EML object document
my_eml = EMLizer(package_id="ID", title="Mon titre", lang="fr", creator="Mon Createur", abstract="Mon abstract")

# print EML xml formatted string
print(my_eml.to_string())

# dump EML xml formatted to file
my_eml.to_file('path/to/file/eml.xml')

# Inspect validity
if my_eml.validate().bool:
    print("This EML file seems valid")
else:
    print("This EML file does not seem valid!")
    my_eml.validate().reason

```


## Recommended usage

The EMLizer helper class is just a wrapper to help quickly basic EML files.
Nevertheless in more complex or sophisticated situations, i recommend to use the dataclass API directly under `emllib.dataclass.eml220`



# Changelog

## 0.2.0

### Added

### Changed

* utils.validate() returns collections.namedtuple (bool, reason) instead of just bool

### Removed


---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).