# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Add
- `--testing` option to load sample.txt/sample2.txt data when testing to prevent flooding the BCCDC site with requests
- option to print ascii histograms
- support for other provinces
- `--version` option

## [0.2.0] - 2020-09-01
### Added 

## [0.1.1] - 2020-08-30
### Fixed
- date parser to read both YYYY-MM-DD and MM/DD/YYYY formats (the BCCDC flip-flops between them)

## [0.1.0] - 2020-08-28
### Added
- `covid-update.py`, with optional arguments `-adrtw` and helpful command line hints via `-h`
- a README in Github-Flavored Markdown to document installation, API & licensing
- this CHANGELOG
- a couple sample data files, for testing new features.
