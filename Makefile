install:
	pip install --upgrade pip && pip install -r requirements.txt

etl:
	@python3 etl.py

test:
	@pytest test_pipeline.py -v

clean:
	rm -rf __pycache__ .pytest_cache data/processed/*.csv data/*.db
