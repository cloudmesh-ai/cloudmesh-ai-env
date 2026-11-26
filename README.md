# cloudmesh-ai-env

## cm-env

**cm-env** is a lightweight command‑line utility packaged under the ``src``
directory. It demonstrates how to provide an editable installation with
``pip install -e .`` and expose a console script.

### Installation (editable mode)

```bash
pip install -e .
```

### Usage

```bash
cm-env <path> [--python <interpreter>]
```

* ``<path>`` – The directory to which the configuration should be applied. Use
  ``.`` for the current working directory.
* ``--python`` – (optional) Specify the Python interpreter version that the
  configuration should target. If omitted, the default is ``python3.15.2``.

The command creates (or overwrites) a ``config.txt`` file inside the target
directory containing a short confirmation message.

### Example

```bash
cm-env .                        # Apply to the current directory (defaults to python3.15.2)
cm-env /tmp/example             # Apply to a specific directory (defaults to python3.15.2)
cm-env . --python python3.10    # Apply with a custom Python version
```

After running the command you will find a ``config.txt`` file in the target
directory with content similar to:

```
Configuration applied to /absolute/path/to/target
```

The source code for this tool lives under ``src/cm_env``.

## License

This project is licensed under the **Apache License, Version 2.0**. See the
`LICENSE` file for the full license text.
