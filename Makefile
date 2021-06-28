clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

runserver:
	python manage.py runserver 0.0.0.0:8000

export_requirements:
	poetry export -f requirements.txt -o requirements.txt

export_requirements_dev:
	poetry export --dev -f requirements.txt -o requirements-dev.txt

black:
	black --target-version py38 --verbose --check --exclude=venv .

black_reformat:
	black --target-version py38 --verbose --exclude=venv .

create_admin:
	python manage.py shell -c "from django.contrib.auth.models import User; \
                               User.objects.filter(username='admin').exists() or \
                               User.objects.create_superuser('admin', 'admin@example.com', '123456')"

cov:
	pytest --cov