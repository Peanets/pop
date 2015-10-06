release: test
	python setup.py install
	
test:
	@cd pop/tests; py.test -vv

clean:
	@rm -rf pop.egg-info; rm -rf build; rm -rf dist; rm -rf .cache