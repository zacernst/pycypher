PYTHON = 3.12

clean_build: clean all

all: build docs tests 

venv:
	echo "Installing Python and virtual environment..." && uv venv --python=$(PYTHON) venv

veryclean: clean
	uv cache clean

deps: venv requirements.txt
	( \
		echo "Installing dependencies..." && \
		. ./venv/bin/activate && \
		uv pip install -r requirements.txt \
	)

requirements.txt: requirements.in
	( \
		echo "Compiling requirements.txt..." && \
		. ./venv/bin/activate && \
		uv pip compile --output-file=requirements.txt requirements.in \
	)

install: build
	( \
		echo "Installing package as editable project..." && \
		. ./venv/bin/activate && \
		uv pip install --upgrade -e . \
	)

tests: install 
	( \
		echo "Running tests..." && \
		. ./venv/bin/activate && \
		pytest -vv tests/ \
	)

clean:
	( \
		rm -rfv ./venv && \
		rm -rfv ./sphinx_docs/_build/html/* \
		rm -rfv ./sphinx_docs/_build/doctrees/* \
		rm -rfv ./docs/* \
		rm -fv ./requirements.txt \
		rm -rfv ./dist/* \
	)

build: deps
	( \
		echo "Formatting code and building package..." && \
		. ./venv/bin/activate && \
		isort . && \
		ruff format . && \
		hatch build -t wheel \
	)

docs: install
	( \
		echo "Building documentation..." && \
		. ./venv/bin/activate && \
		cd sphinx_docs && \
		make html && \
		make singlehtml && \
		cp -rfv _build/singlehtml/* ../docs/ \
	)

.PHONY: clean clean_build tests deps install build docs grammar