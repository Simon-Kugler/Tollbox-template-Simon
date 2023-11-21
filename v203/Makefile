all: build/v203.pdf

# hier Python-Skripte:
build/plota.pdf: python/plota.py ../matplotlibrc ../header-matplotlib.tex Messdaten1_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc
	python plota.py
build/plotb.pdf: plota.py ../matplotlibrc ../header-matplotlib.tex Messdaten2_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc 
	python plotb.py
build/plotc.pdf: plotc.py ../matplotlibrc ../header-matplotlib.tex Messdaten1_203.txt Messdaten1.1_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc 
	python plotc.py
build/plotd.pdf: plotd.py ../matplotlibrc ../header-matplotlib.tex Messdaten2_203.txt | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc 
	python plotd.py
build/plote.pdf: plote.py ../matplotlibrc ../header-matplotlib.tex  | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc 
	python plote.py
build/plotf.pdf: plotf.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	#TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc 
	python plotf.py




# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/v203.pdf: build/plota.pdf build/plotb.pdf build/plotc.pdf build/plotd.pdf build/plote.pdf build/plotf.pdf

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
