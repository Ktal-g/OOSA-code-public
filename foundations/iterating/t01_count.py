
'''
Demonstrating of iterating over
a list of numbers
SH 2019-02-02
'''

###########################################
import argparse

###########################################

def getCmdArgs():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("Demonstrating of iterating over a list of numbers"))
  p.add_argument("--len", dest ="n", type=int, default=10, help=("Length of array"))
  cmdargs = p.parse_args()
  return cmdargs


###########################################

def writeNumbers(n):
  # the loop
  for i in range(1,n+1):   # a for loop loops from the first number to
    print(i)               # the second number-1.
                           # so to loop over 1-n inclusive, we must loop
                           # to n+1. This is to make array indexing easier
                           # more on this next

###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  cmdargs=getCmdArgs()
  # call the looping function
  writeNumbers(cmdargs.n)

