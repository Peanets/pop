release: test
	python setup.py install
	
test:
	@cd pop/tests; py.test -vv