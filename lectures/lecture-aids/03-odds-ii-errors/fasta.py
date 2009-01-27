def count_fasta_seqs(filename):
    '''
    N = count_fasta_seqs(fname)

    Count the number of sequences in FASTA file.
    '''
    nseqs = 0
    for line in file(filename):
        if line.startswith('>'):
            nseqs += 1
    return nseqs

try:
    N = count_fasta_seqs('this-file-does-not-exist'):
except Exception:
    print 'generic exception'
    

try:
    N = count_fasta_seqs('this-file-does-not-exist'):
except IOError:
    print 'IOError'
except Exception:
    print 'generic exception'

