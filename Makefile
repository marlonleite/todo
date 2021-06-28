clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

export_requirements:
	poetry export -f requirements.txt -o requirements.txt

export_requirements_dev:
	poetry export --dev -f requirements.txt -o requirements-dev.txt