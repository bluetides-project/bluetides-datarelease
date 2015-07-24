README.html : README.rst
	rst2html.py README.rst --stylesheet=cskeeters-rst2html-style.css  > README.html
