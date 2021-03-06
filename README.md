# covid-update.py

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)


Print regional COVID case data from the BCCDC.

From the [BCCDC data notes](http://www.bccdc.ca/Health-Info-Site/Documents/BC_COVID-19_Disclaimer_Data_Notes.pdf):
>Case details and laboratory information are updated daily Monday through Friday at 4:30 pm.

## Installation

**covid-update.py** was made with Python 3.8.2, and is compatible with 3.7+. 

### 1. [Install python 3](https://installpython3.com/)

### 2. Install requests

```bash
python3 -m pip install -U requests
```

## Command Line Options

`-a`, `--all-regions`

Print data for all regions.

`-d N`, `--days N`

Print data for the past N days.

`-h`, `--help`

Print a help message covering these options.

`--no-hist`

Don't print the histogram.

`-r REGION`, `--region REGION`

Specify a region. Defaults to Vancouver Island. Valid regions are I (Interior), F (Fraser), C (Vancouver Coastal), V (Vancouver Island), N (Northern).

`-t`, `--today`

Print today's data only.

`--testing`

Read data from sample2.txt instead of BCCDC.

`--version`

Print **covid-update** version.

`-w N`, `--weeks N`

Print data for the past N weeks.

## TODO
- [ ] add support for other provinces
- [ ] restructure script for portability

See [`CHANGELOG.md`](/CHANGELOG.md).

## Contributing

If you want to contribute to this project, shoot me an email at tom.on.github@gmail.com — I'd love to hear about it.

#### A few guidelines:
* Whenever possible while testing new features, use `--testing` to avoid frequent server requests.
* Any optional arguments should be added via `argparse` and documented in the README and the script docstring.
* All changes shall adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 440](https://www.python.org/dev/peps/pep-0440/) specifications.
* Notable changes should be documented in `CHANGELOG.md`.

This project is released with the [Contributor Covenant's](https://www.contributor-covenant.org/) [Contributor Code of Conduct](/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License
**covid-update.py** is licensed under [The Hippocratic License 2.1](https://firstdonoharm.dev/).

Note that the python package is tagged with the MIT trove classifier until PyPI 
supports a trove classifier for the Hippocratic License
([https://github.com/pypa/warehouse/issues/7157](https://github.com/pypa/warehouse/issues/7157)).
