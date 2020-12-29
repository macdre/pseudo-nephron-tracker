# Makefile for local build management

SHELL = /usr/bin/bash
CURR_DIR := $(shell pwd)

.PHONY: build-docker
build-docker:
	docker build -t web:latest .

.PHONY: build-vue
build-vue:
	cd ./client && npm run build

.PHONY: run
run:
	./scripts/run-local.sh $(CURR_DIR)

.PHONY: follow
follow:
	docker logs -f flask-vue

.PHONY: e2e-test
e2e-test:
	cd ./client/test && source ./test_creds.sh && pytest tests.py