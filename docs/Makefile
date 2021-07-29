# Makefile for Sphinx documentation
# You can set these variables from the command line.

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
VENV = .env/bin/activate
PORT = 8001
BUILDDIR = build
SOURCEDIR = source

# Internal variables.
ALLSPHINXOPTS   = -n -d build/doctrees $(SPHINXOPTS) "$(SOURCEDIR)"

# list the targets that we don't want confused with files in the directory
.PHONY: help clean html dirhtml htmlhelp changes linkcheck doctest

# "help" is first so that "make" without an argument acts like "make help".
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  install   to setup a venv with the docs requirements installed"
	@echo "  html      to make standalone HTML files"
	@echo "  run       to build the docs, watch for changes, and serve them at http://0.0.0.0:8001"
	@echo "  dirhtml   to make HTML files named index.html in directories"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"
	@echo "  doctest   to run all doctests embedded in the documentation (if enabled)"
	@echo "  spelling  to check for typos in documentation"


html:
	. $(VENV); $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) build/html
	@echo
	@echo "Build finished. The HTML pages are in build/html."

install:
	@echo "... setting up virtualenv"
	python3 -m venv .env
	. $(VENV); pip install -r requirements.txt

	@echo "\n" \
	      "-------------------------------------------------------------------------------------------------- \n" \
		    "* watch, build and serve the documentation: make run \n" \
		    "* check spelling: make spelling \n" \
		    "\n" \
				"enchant must be installed in order for pyenchant (and therefore spelling checks) to work. See \n" \
				"http://docs.django-cms.org/en/latest/contributing/documentation.html#install-the-spelling-software \n" \
	      "-------------------------------------------------------------------------------------------------- \n" \

clean:
	-rm -r $(BUILDDIR)/*

dirhtml:
	. $(VENV); $(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) build/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in build/dirhtml."

htmlhelp:
	. $(VENV); $(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) build/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in build/htmlhelp."

changes:
	. $(VENV); $(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) build/changes
	@echo
	@echo "The overview file is in build/changes."

linkcheck:
	. $(VENV); $(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) build/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in build/linkcheck/output.txt."

doctest:
	. $(VENV); $(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) build/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in build/doctest/output.txt."

spelling:
	. $(VENV); $(SPHINXBUILD) -b spelling $(ALLSPHINXOPTS) build/spelling
	@echo
	@echo "Check finished. Incorrect words can be found in " \
		"build/spelling/output.txt."

run:
	. $(VENV); sphinx-autobuild $(ALLSPHINXOPTS) build/html --host 0.0.0.0 --port $(PORT)

