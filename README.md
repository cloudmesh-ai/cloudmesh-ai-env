# cloudmesh-ai-env

## cm-env

**cm-env** is a lightweight command‑line utility packaged under the ``src``
directory. It demonstrates how to provide an editable installation with
``pip install -e .`` and expose a console script.

### Installation (editable mode)

You can install the package in editable mode using **either** `pip` **or** `uv`.

#### Using pip (standard)

```bash
pip install -e .
```

#### Using uv (recommended for speed)

```bash
uv venv .venv          # create a virtual environment (only once)
source .venv/bin/activate   # or use `uv run` to avoid activation
uv pip install -e .    # install the package in editable mode
```

### Usage

The console script `cm-env` is installed as part of the editable installation.
It can be run directly from an activated virtual environment, or via `uv run`
which executes the command without needing to activate the venv.

```bash
cm-env <path> [--python <interpreter>]
```

* ``<path>`` – The directory to which the configuration should be applied. Use ``.`` for the current working directory.
* ``--python`` – (optional) Specify the Python interpreter version that the configuration should target. If omitted, the default is ``python3.15.2``.

The command creates (or overwrites) a ``config.txt`` file inside the target directory containing a short confirmation message.

### Example

```bash
cm-env .                        # Apply to the current directory (defaults to python3.15.2)
cm-env /tmp/example             # Apply to a specific directory (defaults to python3.15.2)
cm-env . --python python3.10    # Apply with a custom Python version
```

#### Running via `uv run`

If you prefer not to activate the virtual environment, you can execute the command directly with `uv`:

```bash
uv run cm-env .
```

### Development workflows

There are two common ways to work on this project locally:

1️⃣ **Direct `uv` usage** – manually create and activate the venv as shown above. This is straightforward and works on any system where `uv` is installed.

2️⃣ **`direnv` auto‑activation** – place a `.envrc` file at the repository root (included in this repo). When you `cd` into the project, `direnv` will automatically create the `uv` virtual environment (if missing) and load it, removing the need to remember to run `source .venv/bin/activate`.

   ```bash
   # Install direnv (macOS example)
   brew install direnv
   # Add the hook to your shell configuration (e.g., ~/.bashrc or ~/.zshrc)
   eval "$(direnv hook bash)"   # or "$(direnv hook zsh)" for Zsh
   # Allow the .envrc in this repository (run once)
   direnv allow
   ```

   After this, simply `cd` into the repository and the virtual environment will be active. You can then run the CLI as usual:

   ```bash
   cm-env .
   ```

   (or `uv run cm-env .` if you prefer not to rely on the activation).

The source code for this tool lives under ``src/cm_env``.

## License

This project is licensed under the **Apache License, Version 2.0**. See the `LICENSE` file for the full license text.
