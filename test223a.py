#! python3
# -*- coding: utf-8 -*-
# test223a.py - confirmation of Zipf's Law, using brown corpus in nltk

import nltk
import math
import matplotlib.pyplot as plt
from nltk.corpus import brown

def zipf(text):
    '''text - a list of words
    '''
    tokens = [w.lower() 
            for w in text 
            if w.isalpha()
            ]
    fdist = nltk.FreqDist(tokens)
    f = sorted([math.log(v) for v in fdist.values()], reverse=True)
    r = list(range(1, len(f) + 1))

    if len(f) == len(r):
        plt.plot(r, f)
        plt.xlabel('Rank')
        plt.ylabel('Frequency')

        plt.title(r'''Zipf's Law''') 

        plt.show()
    else:
        print("The rank does not match the frequency.")
    
if __name__ == '__main__':
    zipf(brown.words(categories='news'))