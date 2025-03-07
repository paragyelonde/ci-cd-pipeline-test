# CI/CD Calculator Project Documentation
## Overview
The CI/CD Calculator project demonstrates a simple Python-based calculator application with an integrated Continuous Integration (CI) and Continuous Deployment (CD) pipeline using GitHub Actions. The project automates testing using `pytest` and sets up automated workflows for building and testing the code with each change made.

### Core Features:
- **Basic Arithmetic Operations:**
  - Addition
  - Subtraction
  - Multiplication
  - Division (including error handling for division by zero)

- **Testing:**
  - Automated unit tests with `pytest` to ensure the calculator functions correctly.

- **CI/CD Pipelines:**
  - GitHub Actions workflows to automatically run tests and deploy the project with every code change.

## Project Structure
```
ci_cd_calculator/
├── calculator.py            # Core Calculator Implementation
├── test_calculator.py       # Unit Tests using pytest
├── requirements.txt         # Dependencies (pytest)
└── .github/
    └── workflows/
        ├── main.yml         # CI Pipeline: Runs tests on push and PR
        └── test.yml         # CD Pipeline: Runs tests on push to main
```

### Calculator Code (`calculator.py`)
The core calculator functionality is implemented in `calculator.py`. The module includes basic arithmetic operations:

```python
# calculator.py

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

### Testing with Pytest (`test_calculator.py`)
The unit tests for the calculator operations are defined in `test_calculator.py`, using `pytest` for automated testing. This file ensures that all arithmetic operations are functioning correctly.

```python
# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(0, 1) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 2) == -2

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        divide(1, 0)
```

### Dependencies (`requirements.txt`)
To install the necessary dependencies for running the tests and setting up the environment, the `requirements.txt` file lists `pytest` as the required package.

```
pytest==6.2.5
```

## CI/CD with GitHub Actions

### GitHub Actions Workflow for CI (`main.yml`)
The `main.yml` workflow file is configured to run automatically whenever code is pushed to the main branch or a pull request is made. It installs dependencies and runs tests using `pytest`.

```yaml
# .github/workflows/main.yml

name: Python CI Pipeline

on:
  push:
    branches:
      - main  # Trigger on push to 'main' branch
  pull_request:
    branches:
      - main  # Trigger on pull request to 'main' branch

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests with pytest
        run: |
          pytest --maxfail=1 --disable-warnings -q
```

### GitHub Actions Workflow for CD (`test.yml`)
The `test.yml` file runs tests on the main branch after every push, ensuring that the application remains in a deployable state.

```yaml
# .github/workflows/test.yml

name: Test Python App

on:
  push:
    branches:
      - main  # Trigger on push to 'main' branch

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests with pytest
        run: |
          pytest --maxfail=1 --disable-warnings -q
```

### Manual Trigger with Parameters
You can manually trigger the CI workflow and pass parameters (e.g., which version of Python to use or whether to run tests). This is useful for controlling the flow and testing with different configurations.

#### Example Manual Trigger Workflow (`main.yml`):
```yaml
# .github/workflows/main.yml

name: Python CI Pipeline

on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      run_tests:
        description: 'Run the tests'
        required: true
        default: 'yes'
      python_version:
        description: 'Python version to use'
        required: false
        default: '3.9'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ github.event.inputs.python_version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests with pytest
        if: ${{ github.event.inputs.run_tests == 'yes' }}
        run: |
          pytest --maxfail=1 --disable-warnings -q
```

### How to Trigger the Workflow Manually
1. Go to your GitHub repository.
2. Navigate to the **Actions** tab.
3. Select the **Python CI Pipeline** workflow.
4. Click on the **Run workflow** button.
5. Enter the parameters (e.g., `run_tests` and `python_version`) and click **Run workflow**.

## Conclusion
The CI/CD Calculator Project demonstrates a simple Python application with integrated CI/CD pipelines using GitHub Actions. This project automates the process of:
- Running tests with `pytest` on each change to ensure the calculator works as expected.
- Manually triggering workflows with configurable parameters to control the testing and CI/CD process.

The use of GitHub Actions makes the project robust and easily extensible for continuous deployment. Future improvements could include adding more features to the calculator or expanding the CD pipeline to deploy the application to a hosting service.