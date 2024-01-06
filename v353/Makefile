all: build/v353.pdf

# hier Python-Skripte:
build/plota.pdf: python/plota.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc python python/plota.py
build/plotb.pdf: python/plotb.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc python python/plotb.py
build/plotc.pdf: python/plotc.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc python python/plotc.py

# hier weitere Abhängigkeiten für build/v353.pdf deklarieren:
build/v353.pdf: build/plota.pdf build/plotb.pdf build/plotc.pdf

build/v353.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v353.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean

