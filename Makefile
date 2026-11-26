######################################################################
# Cloudmesh AI Environment Makefile
######################################################################

# Variables
PYTHON       := python
PIP          := $(PYTHON) -m pip
PACKAGE_NAME := $(shell basename $(CURDIR))
TWINE        := $(PYTHON) -m twine
VERSION_FILE := VERSION
GIT          := git
PYENVVERSION := $(shell pyenv version-name)

# Repository information (override if needed)
GITHUB_REPO   := cloudmesh-ai/cloudmesh-ai-env

.PHONY: help doc view clean install

help:
	@echo "Makefile for Cloudmesh AI Environment"
	@echo ""
	@echo "  install    - Install in editable mode for local development"
	@echo "  doc        - Build documentation using MkDocs"
	@echo "  view       - Preview documentation locally"
	@echo "  clean      - Remove generated documentation artifacts"
	@echo ""

install:
	$(PIP) install -e .

# UV-based development workflow
uv-venv:
	uv venv .venv --clear

uv-install: uv-venv
	uv pip install -e .

uv-run:
	uv run cm-env $(ARGS)

uv-clean:
	rm -rf .venv .direnv
# Documentation dependencies (requirements-docs.txt and the local theme)
DOC_DEPS = requirements-docs.txt ../cloudmesh-ai-theme

docs-deps:
	@echo "🔧 Installing documentation dependencies"
	$(PYTHON) -m ensurepip --upgrade || true
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r $(word 1,$(DOC_DEPS))
	$(PIP) install -e $(word 2,$(DOC_DEPS))

doc: docs-deps
	@echo "✅ Docs dependencies installed – building site"
	mkdocs build

view: docs-deps
	@echo "✅ Docs dependencies installed – starting live server"
	lsof -ti:8000 | xargs kill -9 || true
	mkdocs serve --livereload

clean:
	@echo "Cleaning generated documentation artifacts"
	rm -rf site
