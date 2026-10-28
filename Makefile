.PHONY: install dev test reference
install:
	python3 -m venv .venv
	.venv/bin/python -m pip install -r requirements-lock.txt
dev:
	.venv/bin/python tools/dev.py
test:
	.venv/bin/python tools/verify.py
reference:
	.venv/bin/python tools/source-map.py
