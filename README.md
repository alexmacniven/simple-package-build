# Simple Package with Build
This template bootstraps a python package using **pyproject.toml** and **build**.

## Setup
1. Clone your repository
2. Create a virtualenv
    ```bash
    python -m venv venv --prompt package && source venv/bin/activate
    ```
3. Install base dependencies
    ```bash
    python -m pip install --upgrade pip && python -m pip install -r requirements.txt
    ```

## Testing
Testing is powered by [pytest](https://pypi.org/project/pytest/)

Prior to running tests, ensure your package installed;
```bash
python -m pip install -e .
```

You can then run your tests;
```bash
python -m pytest
```

## Building
Building is powered by [build](https://pypi.org/project/build/)

You can build your package with;
```bash
python -m build
```