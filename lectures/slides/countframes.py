import vim
import re
cb = vim.current.buffer
Nframe = 0
begin_pat = re.compile(r'\\begin{frame}(?:\[fragile\])?( % slide [0-9]+)?')

for i,line in enumerate(cb):
    if line.startswith(r'\frame{') or line.startswith(r'\begin{frame}'):
        if begin_pat.match(line):
            fragile = ('[fragile]' if line.find('fragile') > 0 else '')
            cb[i] = r'\begin{frame}%s %% slide %s' % (fragile,Nframe)
        Nframe += 1

print 'Number of frames:', Nframe
