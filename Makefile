.PHONY: clean install virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

install:
	virtualenv --prompt '|> boxmetrics <| ' env
	env/bin/pip install -r requirements.txt
	env/bin/python setup.py install
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo "Usage: "
	@echo "boxmetrics -h"
	@echo "boxmetrics info -h"
	@echo "boxmetrics info system -h"
	@echo 

virtualenv:
	virtualenv --prompt '|> boxmetrics <| ' env
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=boxmetrics \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t boxmetrics:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
