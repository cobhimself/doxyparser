DOXYGEN ?= `which doxygen`
SAMPLEDATA = test/_sample_data
PHP = $(SAMPLEDATA)/php
PHPBUILD = $(SAMPLEDATA)/_build/php
PHPDOXYFILE = $(PHP)/Doxyfile

php: "$(PHP)/**/*.php"
	$(DOXYGEN) "$(PHPDOXYFILE)"

.PHONY: clean
clean:
	rm -fR $(PHPBUILD)

init:
	mkdir -p $(PHPBUILD)

install:
	pipenv install

# Get the tests' doxygen data from our sample data
test_data: init php

.PHONY: test
test:
	pytest test

.PHONY: cov
cov:
	pytest --cov=doxyparser

.PHONY: expect
expect:
	#python -m test.expectation_generator index test_generator
	python -m test.expectation_generator class_src_1_1_more_1_1_deep_class test_generator

.PHONY: config
config:
	python -m doxyparser.util.element_generator compound config
	python -m doxyparser.util.element_generator index config

.PHONY: elements
elements:
	python -m doxyparser.util.element_generator compound elements