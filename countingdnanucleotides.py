#!/usr/bin/env python3

#Function counts the amount of A, C, T and G nucleotides appear
# in a given DNA sequence.
def count():
    dnasq = input("Please input DNA sequence: ")
    char1 = "A"
    char2 = "C"
    char3 = "G"
    char4 = "T"

    print("There are", dnasq.count(char1), "instances of the nucleotide A,", dnasq.count(char2), "of the nucleotide C,", dnasq.count(char3), "of the nucleotide G,", "and", dnasq.count(char4), "of the nucleotide T.")

count()
