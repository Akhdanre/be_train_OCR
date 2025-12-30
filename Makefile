# Makefile for be_train_OCR

.PHONY: help run test lint clean

help:
	@echo "Available targets:"
	@echo "  run     - Run the Flask app (development mode)"
	@echo "  test    - Run pytest for all tests"
	@echo "  lint    - Run flake8 for linting (if installed)"
	@echo "  clean   - Remove Python cache and pyc files"

run:
	FLASK_APP=main.py flask run

test:
	pytest

lint:
	flake8 . || echo 'flake8 not installed. Skipping lint.'

clean:
	rm -rf __pycache__ */__pycache__ *.pyc *.pyo .pytest_cache
