setup:
	python3 -m venv ~/.myrepo

install:
	echo "Installing requirements..."
	pip install -r requirements.txt

test:
	echo "running tests..."
	python -m pytest -vv --cov=myrepolib tests/test_myrepo.py
	python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C myrepolib cli web

all: 
	install lint test
