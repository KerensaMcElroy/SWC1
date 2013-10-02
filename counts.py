import sys
sequence=sys.argv[1].upper()
dna_dict={}
bases=set(sequence)
for base in bases:
    dna_dict[base]=sequence.count(base)
    
print dna_dict
total=len(sequence)
gc=dna_dict['G']+dna_dict['C']

print float(gc)/total

