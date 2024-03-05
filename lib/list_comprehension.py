#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]  # Change 'sequence' to 'num_list'
    return evens

def make_exclamation(sentence_list):
    exclamations = [sentence + '!' for sentence in sentence_list]  # Change 'sentences' to 'sentence_list'
    return exclamations