#!/usr/bin/python
from __future__ import division
import math
import sys

def fct(n):
    return math.factorial(n)

def c(n,d):
    return fct(n)/(fct(d)*fct(n-d))

def mullTo(x,h=0, crds=60, d=7):
    """ x represents the number of desired cards in the deck, one of which constitutes a keep
        h is the minimum hand size (h=4 means keep any 4 card hand)
        crds is the number of cards in the deck at the start
        d is the number of cards to draw initially
    """
    cumSum = 1;
    while (d >= h):
            cumSum = cumSum * c(crds-x,d)/c(crds,d)
            d = d-1
    return 1-cumSum

print(mullTo(*map(int,sys.argv[1:])))
