all: build/v103.pdf

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

# build/plotd.pdf: plotd.py ../matplotlibrc ../header-matplotlib.tex | build
# 	# so that matplotlib can find the tex header when running
# 	# LaTeX in the tmp directory
# 	# and set the matplotlibrc
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc python python/plotd.py

# build/plote.pdf: plote.py ../matplotlibrc ../header-matplotlib.tex | build
# 	# so that matplotlib can find the tex header when running
# 	# LaTeX in the tmp directory
# 	# and set the matplotlibrc
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc python python/plote.py

# build/plotf.pdf: plotf.py ../matplotlibrc ../header-matplotlib.tex | build
# 	# so that matplotlib can find the tex header when running
# 	# LaTeX in the tmp directory
# 	# and set the matplotlibrc
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=$(CURDIR)/../matplotlibrc python python/plotf.py

# hier weitere Abhängigkeiten für build/v103.pdf deklarieren:
build/v103.pdf: build/plota.pdf build/plotb.pdf build/plotc.pdf 
#build/plotd.pdf build/plote.pdf build/plotf.pdf

build/v103.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v103.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
