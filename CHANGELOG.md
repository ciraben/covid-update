# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Add
- `--testing` option to load sample2.txt to prevent flooding the BCCDC site with requests when testing new features.
- option to print ascii histograms
- support for other provinces
- `--version` option
- `covid-update.py`, with optional arguments `-adrtw` and helpful command line hints via `-h`
- a README, LICENSE & CHANGELOG
- a couple sample data files, for testing new features.
### Fix
- date parser to read both YYYY-MM-DD and MM/DD/YYYY formats (the BCCDC flip-flops between them)
