install:
	pip3 install -r requirements.txt
	./scriptDespliegue.sh

tests:
	python3 tests.py