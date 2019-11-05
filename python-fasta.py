import sys

def read_fasta(filename):
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line: # to remove idenitfier information
            seq = seq + line
    f.close()
    return seq
print(read_fasta(sys.argv[1]))

