DOXYGEN ?= `which doxygen`
SAMPLEDATA = "sample_data"
PHP = "$(SAMPLEDATA)/php"
PHPBUILD = "$(SAMPLEDATA)/_build/php"
PHPDOXYFILE = "$(PHP)/Doxyfile"

php: "$(PHP)/**/*.php"
	$(DOXYGEN) "$(PHPDOXYFILE)"

.PHONY: clean
clean:
	rm -fR $(PHPBUILD)

init:
	mkdir -P $(PHPBUILD)