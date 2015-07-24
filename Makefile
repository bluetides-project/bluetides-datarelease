all: README.html README.pdf
README.pdf : README.rst summary.txt
	rst2latex.py README.rst > README.tex
	pdflatex README.tex
	pdflatex README.tex
	rm README.tex README.aux README.log README.out

README.html : README.rst summary.txt
	rst2html.py README.rst --stylesheet=cskeeters-rst2html-style.css  > README.html
summary.txt : summary.py
	python summary.py > $@
