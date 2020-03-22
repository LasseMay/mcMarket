.PHONY: dev setup

dev: 
	FLASK_APP=quarantino.py FLASK_ENV=development flask run

venv:
	pipenv --venv || pipenv install
	pipenv shell
