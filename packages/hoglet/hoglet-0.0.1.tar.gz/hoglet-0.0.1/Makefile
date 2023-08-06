.DEFAULT_GOAL   := all

.PHONY: autoflake
autoflake: ## remove unused imports and variables
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r .

.PHONY: black
black: ## format all files
	black .

.PHONY: build
build: ## build dist
	python -m build

.PHONY: clean
clean: ## clean working folders
	@rm -r .mypy_cache | True
	@rm -r .pytest_cache | True
	@rm -r build | True
	@rm -r dist | True
	@rm -r hoglet.egg-info | True
	@rm .coverage | True

.PHONY: install
install: ## install package
	python -m pip install --upgrade pip
	python -m pip install ".[dev]"

.PHONY: isort
isort: ## sort imports
	python -m isort .

.PHONY: install
uninstall: ## uninstall package
	python -m pip uninstall hoglet -y

.PHONY: unittest
unittest: ## run unit tests
	python -m pytest -n 3 --cov-report term-missing --cov hoglet -m "not debug" ./tests/test_unit

.PHONY: integrationtest
integrationtest: ## run integration tests
	python -m pytest -n 3 --cov-report term-missing --cov hoglet -m "not debug" ./tests/test_integration

.PHONY: mypy
mypy: ## run mypy
	python -m mypy .

.PHONY: all
all:
	make clean
	make autoflake
	make isort
	make black
	make unittest
	make integrationtest
	make mypy
	make build

.PHONY: help
help: ## show all commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'