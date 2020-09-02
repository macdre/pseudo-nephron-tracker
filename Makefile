# Makefile for local build management

SHELL = /usr/bin/bash
MY_VAR := $(shell pwd)

.PHONY: build-docker
build-docker:
	docker build -t web:latest .

.PHONY: build-vue
build-vue:
	cd ./client && npm run build

.PHONY: run
run:
	./scripts/run-local.sh $(MY_VAR)

.PHONY: follow
follow:
	docker logs -f flask-vue

.PHONY: test
test:
	@echo MY_VAR is $(MY_VAR)
