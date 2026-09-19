# GitHub Actions Notes

## What is an action?

In GitHub Actions, an action is a reusable unit of work that can be executed inside a workflow. It may be a small script, a task, or a prebuilt solution created by GitHub or the community.

Example:

```yaml
- uses: actions/checkout@v4
```

Here, `actions/checkout` is an action that checks out your repository so the runner can access the project files.

---

## What does `uses:` mean?

`uses:` tells GitHub Actions to run an action instead of a local shell command.

```yaml
steps:
  - uses: actions/checkout@v4
```

This is different from:

```yaml
steps:
  - name: Run script
    run: echo Hello, world!
```

In the second example, `run` executes a shell command directly.

---

## Example workflow

```yaml
name: CI

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run a one-line script
        run: echo Hello, world!
```

### Meaning of each part

- `name`: workflow name
- `on`: when the workflow should run
- `jobs`: collection of tasks
- `runs-on`: machine type used to run the job
- `steps`: ordered list of instructions
- `uses`: reusable action
- `run`: shell command

---

## Where to find available actions?

### 1. GitHub Marketplace
Visit:

https://github.com/marketplace?type=actions

You can search for actions like:
- checkout
- setup-python
- cache
- docker
- deploy

### 2. GitHub Docs
Official documentation:

https://docs.github.com/actions

### 3. Search by action name
Common examples:
- `actions/checkout`
- `actions/setup-python`
- `actions/cache`
- `actions/upload-artifact`

---

## Common GitHub Actions examples

### Checkout repository
```yaml
- uses: actions/checkout@v4
```

### Setup Python
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
```

### Run Python code
```yaml
- run: python --version
```

### Cache dependencies
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

---

## Difference between `uses` and `run`

### `uses`
- runs a prebuilt action
- useful for reusable logic
- often used for setup and packaging tasks

### `run`
- runs a shell command directly
- suitable for simple commands like `echo`, `python`, `pytest`, `npm install`

---

## Typical Python CI workflow

```yaml
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

This workflow:
1. checks out the repo
2. installs Python
3. installs dependencies
4. runs tests

---

## Summary

- Actions are reusable tasks in GitHub workflows.
- `uses:` is how you invoke an action.
- `run:` is how you execute a shell command directly.
- You can discover actions from the GitHub Marketplace and official docs.
- For Python projects, common actions are `checkout` and `setup-python`.

---

## Quick takeaway

If you want to do something common in CI, there is usually already an action for it.

Examples:
- install Python
- checkout code
- cache dependencies
- upload test results
- deploy applications


