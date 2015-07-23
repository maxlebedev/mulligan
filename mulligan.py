from __future__ import division
import math
import sys

def fct(n):
	return math.factorial(n)
def c(n,d):
	return fct(n)/(fct(d)*fct(n-d))

def mullTo(x,h=0):#mulligan to a x-of but keep any h card hand
	cumSum = 1;
	d = 7;
	while (d >= h):
		cumSum = cumSum * c(60-x,d)/c(60,d)
		d = d-1
	return 1-cumSum;

print(mullTo(*map(int,sys.argv[1:])))
