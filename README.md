[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/daskol/tskv/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/daskol/tskv.svg?style=social&style=flat-square)](https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D)

# tskv

*Tab-Separated Key-Value format*

## Description

1. Each line starts from prefix `tskv\t`.
2. Values are stored as key-value pairs that is separated with equal sign `=`.
3. Prefix and key-value pairs separated with tabs `\t`.

## Installation and Testing

One could install package in common way from PyPI with `pip`
```bash
    pip install tskv
```
In order to setup the newest version from source codes, one should clone repository first and than run installation script
```bash
    git clone git@github.com:daskol/tskv.git
    python tskv/setup.py
```
Than run tests as follows
```bash
    python -m unittest discover tskv/tests/
```

## Examles

In the begging it data representation format is used for running mappers in Hadoop Streaming regine.

See [examples/](examples/) for working example of utility that converts nginx's logs to tksv-formatted files.
