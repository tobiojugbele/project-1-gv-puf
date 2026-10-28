install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	@python3 test_environment.py

run:
	@python3 etl.py
