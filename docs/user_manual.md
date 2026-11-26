# User Manual for **cm‑env**

Welcome to the **cm‑env** user manual. This guide walks you through the
installation, configuration, and everyday usage of the command‑line utility.

---

## 1. Overview

`cm‑env` is a tiny tool that applies a simple configuration to a target
directory. In this placeholder implementation the configuration consists of a
`config.txt` file containing a confirmation message and the Python interpreter
version you specify via the `--python` flag.

The package lives under `src/cm_env` and is exposed as a console script called
`cm‑env`.

---

## 2. Installation

You have two options for installing the project in **editable** mode:

### 2.1 Using pip (standard)

```bash
pip install -e .
```

### 2.2 Using uv (fast)

`uv` is a modern, single‑binary tool that resolves dependencies and creates a
virtual environment in a fraction of the time required by pip.

```bash
uv venv .venv          # create a virtual environment (only once)
source .venv/bin/activate   # or just use `uv run` to skip activation
uv pip install -e .    # install the package in editable mode
```

> **Tip:** The repository also ships a convenient Makefile target:
> ```bash
> make uv-install
> ```

---

## 3. Quick‑Start Guide

Once the package is installed, you can apply the configuration to any
directory:

```bash
cm‑env <path>
```

*`<path>`* is the directory you want to configure. Use `.` for the current
working directory.

The command will create (or overwrite) a `config.txt` file inside the target
directory. The file contains something similar to:

```
Configuration applied to /absolute/path/to/target
Python version: python3.15.2
```

---

## 4. Command‑line Options

| Option | Description |
|--------|-------------|
| ``<path>`` (positional) | Target directory. ``.`` = cwd. |
| ``--python <interpreter>`` | Python interpreter version to record. Defaults to ``python3.15.2``. |

Example with a custom interpreter:

```bash
cm‑env . --python python3.10
```

---

## 5. Running without activating the virtual environment

If you prefer not to `source .venv/bin/activate`, you can invoke the command
directly via `uv`:

```bash
uv run cm‑env .
```

---

## 6. Development Workflow

Two common ways to work on the project locally:

### 6.1 Direct `uv` usage

```bash
uv venv .venv          # create the env (once)
source .venv/bin/activate
uv pip install -e .    # install in editable mode
cm‑env .               # run the CLI
```

### 6.2 `direnv` auto‑activation (recommended for frequent context switches)

The repository includes a `.envrc` file that automatically creates the uv
virtual environment and activates it when you `cd` into the project.

```bash
# Install direnv (macOS example)
brew install direnv

# Hook direnv into your shell (add to ~/.bashrc or ~/.zshrc)
eval "$(direnv hook bash)"   # or "$(direnv hook zsh)" for Zsh

# Allow the .envrc file the first time you enter the repo
direnv allow
```

Now simply `cd` into the repository and the environment will be ready – you can
run `cm‑env` immediately.

---

## 7. Troubleshooting

* **`uv` not found** – Install it from https://github.com/astral‑sh/uv.
* **`direnv` not activating** – Ensure the hook is added to your shell
  configuration and that you have run `direnv allow` inside the repository.
* **Virtual‑environment conflicts** – Delete `.venv` and `.direnv` (or run
  `make uv-clean`) and recreate with `make uv-install`.

---

## 8. License

This project is licensed under the Apache License, Version 2.0. See the
`LICENSE` file for the full text.
