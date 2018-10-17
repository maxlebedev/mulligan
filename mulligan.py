#!/usr/bin/python
from __future__ import division
import math
import sys

def fct(n):
    return math.factorial(n)

def c(n,d):
    return fct(n)/(fct(d)*fct(n-d))

def mull_to(pop, min_hand_size=0, deck_size=60, hand_size=7):
    """ pop represents the number of desired cards in the deck, one of which constitutes a keep
        min_hand_size is the minimum hand size (min_hand_size=4 means keep any 4 card hand)
        deck_size is the number of cards in the deck at the start
        hand_size is the number of cards to draw initially
    """
    chance_of_failure = 1;
    while (hand_size >= min_hand_size):
            chance_of_failue *= c(deck_size - pop, hand_size)/c(deck_size, hand_size)
            hand_size -= 1
    return 1 - chance_of_failure

if __name__ == "__main__":
    print(mull_to(*map(int,sys.argv[1:])))
