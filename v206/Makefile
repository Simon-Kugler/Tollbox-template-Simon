all: build/v206.pdf

# hier Python-Skripte:
build/plota.pdf: python/plota.py ../matplotlibrc ../header-matplotlib.tex messdaten/Messdaten.txt| build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc \
	python python/plota.py
build/Verdampfungswärme.pdf: python/Verdampfungswärme.py ../matplotlibrc ../header-matplotlib.tex messdaten/Messdaten.txt| build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc \
	python python/Verdampfungswärme.py

# hier weitere Abhängigkeiten für build/v206.pdf deklarieren:
PLOTS := build/plota.pdf build/Verdampfungswärme.pdf
build/v206.pdf: $(PLOTS)

build/v206.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v206.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
