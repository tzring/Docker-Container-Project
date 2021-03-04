setup:
	python3 -m venv ~/.docker 

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test_app.py

validate-circleci:
	circleci config process .circleci/config.yml

run-circleci-local:
	circleci local execute

lint:
	hadolint Dockerfile 
	pylint --disable=R,C,W1203 app.py
	
format:
	black *.py

all: install lint test
