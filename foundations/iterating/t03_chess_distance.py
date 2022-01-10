

'''
An example of calculation within
a nested loop, using a chessboard
SH 2019-02-03
'''

###########################################
from math import sqrt


###########################################

def writeDistanced():
  '''
  Loop over all squares of a chessboard
  and write their coordinates
  '''
  nX=nY=8    # the number of squares in x and y
  for j in range(1,nY+1):   # loop over y on origin square
    for i in range(1,nX+1): # loop over x on origin square
      # we have the origin square, (i,j). We want to compare this to
      # all other squares, so we need another set of nested loops
      for j2 in range(1,nY+1):   # loop over y on target square
        for i2 in range(1,nX+1): # loop over x on target square
          # if the same square, skip calculation
          if((i2==i)&(j2==j)):
            continue
          # calculate distance
          distance=sqrt((i2-i)**2+(j2-j)**2)
          print(i,j,"to",i2,j2,"distance",distance)


###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  # a chessboard has a fixed size, so I will not bother
  # reading the command line.
  writeDistanced()

