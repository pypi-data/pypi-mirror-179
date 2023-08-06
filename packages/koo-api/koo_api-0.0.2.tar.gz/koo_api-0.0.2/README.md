> Work in progress!

# Koo API

This is a basic api wrapper for [Koo](https://www.kooapp.com/).

# Use
## Install
```bash
pip install koo-api
```

## Usage

```python
from koo_api import KooAccount, KooAccountNotFoundException

user = KooAccount("felipeneto")
for post in user.get_koos():
    print(post.content)
```


# Development


This is the standard workflow:

1. Clone this repo.
Before anything:

```bash
pip install poetry
poetry install
```

2. Create a new branch, add your changes and tests.
```bash
git checkout my-new-feature
```

3. Run linting check and tests with: `poetry run tests`
4. If it is all ok format it with: `poetry run format`
4. Commit and open a pull request and request a review from one of the autors.


# TODO

- [] ??
- [] ??
- [] ??
- [] ??
