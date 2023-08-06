# Git croissant

French Git CLI to respect the Toubon Law in France.

## Installation

```bash
pipx install git-croissant
```

## Usage

Git commands and their options and arguments are translated into French.

For now the coverage is far from being exhaustive, and there is no documentation so please read the source code.

Some examples:

```bash
abruti clone --profondeur 3 https://github.com/x/y.git
abruti tire
abruti pousse
```

## Development

Install [Poetry](https://python-poetry.org/) then:

```bash
poetry install
poetry shell

abruti ...
```
