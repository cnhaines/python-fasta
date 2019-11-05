import sys

def read_fasta(filename):
    """Reads fasta file from disk and returns the sequence"""
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line: # to remove idenitfier information
            seq = seq + line
    f.close()
    return seq

if len(sys.argv) < 2:
	print("Need to provide filename as argument")
	exit(1)

print(read_fasta(sys.argv[1]))

