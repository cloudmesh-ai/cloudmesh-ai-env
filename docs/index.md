# Cloudmesh AI Environment

Welcome to the **Cloudmesh AI Environment** repository.

This documentation provides an overview of the project, how to set up the development environment, and basic usage instructions.

## Getting Started

To get started with this project, clone the repository and set up a development environment. You can choose between the classic `pip` workflow or the faster `uv` workflow. Optionally, enable `direnv` for automatic environment activation.

```bash
git clone https://github.com/cloudmesh-ai/cloudmesh-ai-env.git
cd cloudmesh-ai-env
```

### Pip workflow (default)

```bash
make install   # installs the package in editable mode using pip
```

### UV workflow

```bash
make uv-install   # creates a uv virtual environment and installs the package
```

### Direnv auto‑activation (optional)

```bash
brew install direnv   # macOS example; see direnv docs for other platforms
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc   # or ~/.zshrc for Zsh
direnv allow
```

After the environment is set up, you can run the CLI:

```bash
cm-env .               # from an activated venv
uv run cm-env .        # without activating
```

## Documentation

The documentation is built with **MkDocs** using the Material theme and the Cloudmesh AI custom theme. You can preview the documentation locally:

```bash
make view
```

And build the static site:

```bash
make doc
```

### Further Reading

- [User Manual](user_manual.md) – detailed guide covering installation, CLI usage, options, and development workflows.

## Contributing

Contributions are welcome! Please see the `CONTRIBUTING.md` (to be added) for guidelines.

---

*This page was generated automatically. Feel free to edit and expand as needed.*
