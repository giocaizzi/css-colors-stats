# css-colors-stats
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/css-colors-stats) ![PyPI - Version](https://img.shields.io/pypi/v/css-colors-stats)
[![Deployment](https://github.com/giocaizzi/css-colors-stats/actions/workflows/deployment.yml/badge.svg)](https://github.com/giocaizzi/css-colors-stats/actions/workflows/deployment.yml)

Quickly **extract and count colors from CSS files** using a *python CLI tool*.

Export result to:
- `json`
- `html`

Available color formats:
- `hex`
- `rgb`
- `rgba`
- `hsl`
- `hsla`

## Installation

Clone this repo and install it with *pip*.

```shell
pip install css-colors-stats
```

## Usage

```shell
css-colors-stats [-h] [--html] filepath
```

*Positional arguments*:
- `filepath`    the path to the CSS file.

*Options*:
- `--html`:             generate an HTML file with the color counts
- `-h`, `--help `:      show help message and exit
