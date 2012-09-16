t=.$1.tex_files
test -d $t || mkdir $t
cd $t
TEXINPUTS=:..:../headers:../headers/imm-format:../../slides/:../images:../../slides/images:../../slides/figures/generated: xelatex $1
cp `basename $1 tex`pdf ..
cd
