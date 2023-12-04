all: build/v101.pdf

# hier Python-Skripte:
# build/plota.pdf: python/plota.py ../matplotlibrc ../header-matplotlib.tex | build
# 	# so that matplotlib can find the tex header when running
# 	# LaTeX in the tmp directory
# 	# and set the matplotlibrc
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python python/plota.py

#build/plotI_D.pdf: python/plotI_D.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python python/plotI_D.py

#hier weitere Abhängigkeiten für build/v101.pdf deklarieren:
#build/v101.pdf: build/plotI_D.pdf
# build/plota.pdf

build/v101.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v101.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
