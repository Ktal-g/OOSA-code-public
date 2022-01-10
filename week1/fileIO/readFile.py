
"""
Example of reading a csv file as a numpy array
"""

import numpy as np



def readFile(filename):
  x,y=np.loadtxt(filename,usecols=(0,1), unpack=True, dtype=float,comments='#',delimiter=',')
  return(x,y)

################################
# the main block

if __name__ == '__main__':
  filename="../data/Wiggle1.txt"
  # read data
  x,y=readFile(filename)

