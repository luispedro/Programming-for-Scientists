input=slides
t=.$input.tex_files
test -d $t || mkdir $t
cd $t
TEXINPUTS=../:../../../lectures/slides/headers/:../../../lectures/slides/headers/cmu-beamer: pdflatex $input.tex
cp $input.pdf ..
cd
