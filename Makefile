.DEFAULT_GOAL := help

.PHONY: help
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: env
env: ## Activate environment
	@echo source ./venv/bin/activate

.PHONY: init
init: ## Initiate project and database
	( \
			. ./venv/bin/activate; \
			r8 sql init --origin http://localhost:8000; \
			r8 sql file config.sql; \
	)

.PHONY: run
run: ## Start project on port 8000
	( \
			. ./venv/bin/activate; \
			r8 run; \
	)
	