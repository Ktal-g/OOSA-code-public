
'''
Demonstrating of iterating over
a list of numbers, backwards
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

def reverseNumbers(n):
  # the loop, from n to 1 (replace 0 with -1 to loop to zero)
  for i in range(n,0,-1):   # the optional third number sets the step size
    print(i)


###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  cmdargs=getCmdArgs()
  # call the looping function
  reverseNumbers(cmdargs.n)

