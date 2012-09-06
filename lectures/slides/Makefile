pdfs := $(patsubst %.tex,%.pdf,$(wildcard *.tex))
all: $(pdfs)

.PHONY: all

%.pdf: %.tex headers/slheader.tex
	./do-slides.sh $<
