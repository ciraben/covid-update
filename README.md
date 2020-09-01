# covid-update.py

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)


Print regional COVID case data from the BCCDC.

From the [BCCDC data notes](http://www.bccdc.ca/Health-Info-Site/Documents/BC_COVID-19_Disclaimer_Data_Notes.pdf):
>Case Details and Laboratory Information are updated daily Monday through Friday at 5:00 pm.

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

`-r REGION`, `--region REGION`

Specify a region. Defaults to Vancouver Island. Valid regions are I (Interior), F (Fraser), C (Vancouver Coastal), V (Vancouver Island), N (Northern).

`-t`, `--today`

Print today's data only.

`-w N`, `--weeks N`

Print data for the past N weeks.

## TODO
- [ ] add a --histogram option -g
- [ ] add support for other provinces
- [x] add a date format reader for both YYYY-MM-DD and MM/DD/YYYY
- [x] add an --all-regions option that prints for all regions -a
- [x] add a --today option that prints "X new case(s) today." -t
- [x] add a number of --weeks/--days ago option (default all) -w/-d N

See [`CHANGELOG.md`](/CHANGELOG.md).

## Contributing

If you want to contribute to this project, shoot me an email at tom.on.github@gmail.com, I'd love to hear about it!

#### A few guidelines:
* Whenever possible while testing new features, data should be loaded from local files rather than the BCCDC server itself to reduce traffic.
* Any optional arguments should be added via `argparse` and documented in the README and the script docstring.
* Changes should be documented in `CHANGELOG.md`.

This project is released with the [Contributor Covenant's](https://www.contributor-covenant.org/) [Contributor Code of Conduct](/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License
**covid-update.py** is licensed under [The Hippocratic License 2.1](https://firstdonoharm.dev/).

Note that the python package is tagged with the MIT trove classifier until PyPI 
supports a trove classifier for the Hippocratic License
([https://github.com/pypa/warehouse/issues/7157](https://github.com/pypa/warehouse/issues/7157)).
