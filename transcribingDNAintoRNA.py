#!/usr/bin/env python3

def dnatorna():
    dna = input("Please input DNA sequence to be transcribed: ")
    return dna.replace("T", "U")

print("RNA:", dnatorna())
