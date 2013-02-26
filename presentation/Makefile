todoflask.pdf: todoflask.md
	pandoc todoflask.md -t beamer -Vtheme:default -Vcolortheme:beaver -Vfonttheme:structurebold -i --template=template.tex -o todoflask.pdf --latex-engine=xelatex

clean:
	rm -f todoflask.pdf

.PHONY: clean
