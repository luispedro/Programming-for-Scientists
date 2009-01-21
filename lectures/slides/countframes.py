import vim
cb = vim.current.buffer
Nframe = 0
for i,line in enumerate(cb):
    if line.startswith(r'\frame{') or line.startswith(r'\begin{frame}'):
        if line == '\\begin{frame}':
            cb[i] = '\\begin{frame} %% slide %s\n' % Nframe
        if line == '\\begin{frame}[fragile]':
            cb[i] = '\\begin{frame}[fragile] %% slide %s\n' % Nframe
        Nframe += 1


print Nframe
