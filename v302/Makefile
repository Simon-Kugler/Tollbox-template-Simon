all: build/v302.pdf
TEX := TEXINPUTS=$$(pwd)/..:
MPL := MATPLOTLIBRC=$(CURDIR)=../matplotlibrc
$(TEX) $(MPL)
hier Python-Skripte:
build/fit.pdf: python/fit.py ../matplotlibrc ../header-matplotlib.tex  | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	$(TEX) $(MPL) python python/fit.py

PLOTS := python/fit.pdf
build/v302.pdf: $(PLOTS)

build/v302.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v302.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
