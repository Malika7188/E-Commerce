# Malika Couture Makefile

.PHONY: help install dev test lint format clean migrate superuser demo-data docker-build docker-up docker-down

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}\' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements-dev.txt

dev: ## Start development server
	python manage.py runserver

test: ## Run tests
	pytest --cov=apps --cov-report=html --cov-report=term

test-fast: ## Run tests without coverage
	pytest -x --disable-warnings

lint: ## Run linting
	flake8 .
	black --check .
	isort --check-only .

format: ## Format code
	black .
	isort .

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/

migrate: ## Run database migrations
	python manage.py makemigrations
	python manage.py migrate

superuser: ## Create superuser
	python manage.py createsuperuser

demo-data: ## Load demo data
	python manage.py loaddata fixtures/initial_data.json
	python manage.py setup_demo_data

collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

# Docker commands
docker-build: ## Build Docker images
	docker-compose build

docker-up: ## Start Docker containers
	docker-compose up -d

docker-down: ## Stop Docker containers
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

docker-shell: ## Open shell in web container
	docker-compose exec web bash

docker-migrate: ## Run migrations in Docker
	docker-compose exec web python manage.py migrate

docker-demo-data: ## Load demo data in Docker
	docker-compose exec web python manage.py loaddata fixtures/initial_data.json
	docker-compose exec web python manage.py setup_demo_data

docker-test: ## Run tests in Docker
	docker-compose exec web pytest

# Production commands
prod-deploy: ## Deploy to production
	@echo "Deploying to production..."
	git push origin main
	# Add your deployment commands here

prod-migrate: ## Run production migrations
	python manage.py migrate --settings=malika_couture.settings.production

prod-collectstatic: ## Collect static files for production
	python manage.py collectstatic --noinput --settings=malika_couture.settings.production

# Backup commands
backup-db: ## Backup database
	python manage.py dbbackup

restore-db: ## Restore database
	python manage.py dbrestore

# Celery commands
celery-worker: ## Start Celery worker
	celery -A malika_couture worker -l info

celery-beat: ## Start Celery beat scheduler
	celery -A malika_couture beat -l info

celery-flower: ## Start Celery Flower monitoring
	celery -A malika_couture flower