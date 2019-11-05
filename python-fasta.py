#!/usr/bin/env python
# coding: utf-8

# In[1]:


# read and parse and use for reverse_complement function
# three quotes serve as the documentation
# conditionally add sequence information but lose the identified lines
def read_fasta(filename):
    """
    Read a FASTA format sequence from the named file
    """
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line: # to remove idenitfier information
            seq = seq + line
    f.close()
    return seq
print(read_fasta('ae.fa'))


# In[ ]:




