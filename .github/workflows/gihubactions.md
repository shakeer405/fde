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

## Creating your own GitHub Action

You can build your own action and reuse it in any repository.

There are 3 common types:

1. JavaScript action
2. Docker action
3. Composite action

The easiest for beginners is a composite action.

---

### 1. Create a repository for the action

Create a new GitHub repository, for example:

```text
my-org/custom-python-setup
```

Inside it, create a file named `action.yml`.

Example:

```yaml
name: 'Custom Python Setup'
description: 'Sets up Python and installs dependencies'
inputs:
  python-version:
    description: 'Python version to use'
    required: true
    default: '3.11'
  requirements-file:
    description: 'Requirements file path'
    required: false
    default: 'requirements.txt'
runs:
  using: 'composite'
  steps:
    - uses: actions/setup-python@v5
      with:
        python-version: ${{ inputs.python-version }}

    - shell: bash
      run: |
        python -m pip install --upgrade pip
        pip install -r ${{ inputs.requirements-file }}
```

This action:
- accepts input values
- installs Python
- installs project dependencies

---

### 2. Add the action code

For a composite action, you usually only need the `action.yml` file.

Example folder structure:

```text
custom-python-setup/
  action.yml
```

---

### 3. Commit and push the repository

```bash
git init
git add .
git commit -m "Initial custom action"
git branch -M main
git remote add origin https://github.com/<your-org>/<your-repo>.git
git push -u origin main
```

---

## Using the custom action in another repository

In another repository, create or edit a workflow file:

```yaml
name: CI

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

      - name: Setup Python and install deps
        uses: your-org/custom-python-setup@v1
        with:
          python-version: '3.11'
          requirements-file: 'requirements.txt'

      - name: Run tests
        run: pytest
```

This means:
- the workflow calls your custom action
- the action runs in a reusable way
- all repositories can use the same setup logic

---

## Important syntax for using a custom action

```yaml
- uses: owner/repository@ref
```

Examples:

```yaml
- uses: my-org/custom-python-setup@v1
- uses: my-org/custom-python-setup@main
- uses: my-org/custom-python-setup@<commit-sha>
```

Best practice:
- use a tag like `v1` or a commit SHA for stability

---

## Publishing to GitHub Marketplace

If you want others to find and use your action publicly, you can publish it to the GitHub Marketplace.

Steps:
1. Create a public repository
2. Add a valid `action.yml`
3. Add a README
4. Add release tags like `v1`
5. Publish to Marketplace if needed

---

## JavaScript action example

If you want logic in Node.js instead of shell commands:

```yaml
name: 'Hello World'
description: 'Prints hello world'
runs:
  using: 'node20'
  main: 'index.js'
```

Then create `index.js`:

```javascript
console.log('Hello from custom GitHub Action!')
```

This is useful when you need a more advanced action with logic and branching.

---

## Docker action example

```yaml
name: 'My Docker Action'
description: 'Runs in a Docker container'
runs:
  using: 'docker'
  image: 'Dockerfile'
```

This is used when you need a custom environment or dependencies that are easier to manage in a container.

---

## Best practices for own actions

- Keep the action simple and single-purpose
- Use clear input names
- Add documentation in README
- Use version tags like `v1`
- Test the action in a sample repo before sharing it
- Keep action logic portable and repeatable

---

## Quick takeaway

To create your own GitHub Action:

1. create a repo
2. add `action.yml`
3. commit and push it
4. call it from another repository with `uses: owner/repo@tag`

This is the standard way to reuse CI logic across projects.

---

## Quick takeaway

If you want to do something common in CI, there is usually already an action for it.

Examples:
- install Python
- checkout code
- cache dependencies
- upload test results
- deploy applications


