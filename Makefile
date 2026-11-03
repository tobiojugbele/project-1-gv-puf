install:
	pip install --upgrade pip && pip install -r requirements.txt

etl:
	@python3 etl.py

run:
	@python3 run_analysis.py

regression:
	@python3 regression_analysis.py

build_excel:
	@python3 build_excel_model.py

html:
	@python3 -c "import os; open('trend_decomposition.html', 'w').write('<html><body><h1>Trend Decomposition Audit Entry Log</h1></body></html>')"

test:
	@pytest test_pipeline.py -v

clean:
	rm -rf __pycache__ .pytest_cache data/processed/*.csv data/*.db *.html *.xlsx
