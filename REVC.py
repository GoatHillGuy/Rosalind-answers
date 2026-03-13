#!/usr/bin/env python3

# Reverse the compliment of a strand of DNA
def revcomp(dna):
    copy = []
    
    for i in dna:
        if i == 'A':
            copy.append('T')
        elif i == 'T':
            copy.append('A')
        elif i == 'G':
            copy.append('C')
        elif i == 'C':
            copy.append('G')
        else:
            print("Invalid string entered.")
            return
    
    copy = (''.join(copy))[::-1]
    print(copy)

revcomp(input("Enter DNA string: "))

