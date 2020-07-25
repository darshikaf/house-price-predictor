DOCKER_IMAGE := darkf-build-testing:latest
TERM := docker run --rm -it -v $(shell pwd):/regression_model -w /regression_model -e PYTTHONPATH=. darshika/${DOCKER_IMAGE}
TESTENV	:= docker run --rm -v $(shell pwd):/regression_model -w /regression_model -e PYTTHONPATH=. darshika/${DOCKER_IMAGE}

clean:
	$(TESTENV) rm -rf __pycache__ regression_model/__pycache__ tests/__pycache__ .pytest_cache .coverage
	$(TESTENV) rm -rf __pycache__ regression_model/config/__pycache__ regression_model/processing/__pycache__ 
	$(TESTENV) rm -rf .mypy_cache/
	$(TESTENV) rm -rf .eggs *.egg-info dist/*

test: clean
	$(TESTENV) coverage run setup.py test --pytest-args="--junit-xml=tests/results.xml"
	# $(TESTENV) coverage report

test-specific: clean
	$(TESTENV) python setup.py test --pytest-args="-k $(TEST)|-s|-v"

test-verbose: clean
	$(TESTENV) python setup.py test --pytest-args="-s"

test-missing: clean
	$(TESTENV) python setup.py test --pytest-args="--cov-report=term-missing|--cov=regression_model"

bash:
	$(TERM) bash

python:
	$(TERM) python

release:
	$(TERM) python setup.py sdist bdist_wheel; twine upload --repository testpypi dist/*

test-python-lint:
	$(TESTENV) black -l 79 --check .

test-python-types:
	$(TESTENV) mypy --ignore-missing-imports regression_model

.PHONY: test bash clean python