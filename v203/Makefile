all: build/v203.pdf
TEX := TEXINPUTS=$$(pwd)/..:
MPL := MATPLOTLIBRC=$(CURDIR)/../matplotlibrc
$(TEX) $(MPL)
# hier Python-Skripte:
plota.pdf: python/plota.py ../matplotlibrc ../header-matplotlib.tex Messdaten1_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	# $(TEX) $(MPL) python plota.py
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc \
	python plota.py
plotb.pdf: plota.py ../matplotlibrc ../header-matplotlib.tex Messdaten2_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc \
	python plotb.py
plotc.pdf: plotc.py ../matplotlibrc ../header-matplotlib.tex Messdaten1_203.txt Messdaten1.1_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc \
	python plotc.py
plotd.pdf: plotd.py ../matplotlibrc ../header-matplotlib.tex Messdaten2_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc \
	python plotd.py
plote.pdf: plote.py ../matplotlibrc ../header-matplotlib.tex  | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc \
	python plote.py
plotf.pdf: plotf.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc \
	python plotf.py




# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:

PLOTS := plota.pdf plotb.pdf plotc.pdf plotd.pdf plote.pdf plotf.pdf

build/v203.pdf: $(PLOTS)

build/v203.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v203.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
