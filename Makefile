run:
	poetry run python -m musicAggregator

lint:
	poetry run black -q -l 120 .
	poetry run isort .
	poetry run pyflakes .
	poetry run flake8
