pdfs := $(patsubst %.tex,%.pdf,$(wildcard *.tex))
all: $(pdfs)

.PHONY: all

%.pdf: %.tex
	./do-hw.sh $<
