install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r testPyPI -u $(user) -p $(password)

lint:
	poetry run flake8 yelper/

bump:
	poetry version patch

test:
	poetry run python -m pytest -vv --ff

test-cov:
	poetry run python -m pytest -q --cov=yelper tests/

coverage.xml:
	poetry run python -m pytest --cov=yelper tests/ --cov-report=xml

.PHONY:
	build install publish lint bump	test test-cov
