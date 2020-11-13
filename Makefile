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