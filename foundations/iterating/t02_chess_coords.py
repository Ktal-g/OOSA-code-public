

'''
An example of a nested loop,
using chessboard coordinates
SH 2019-02-03
'''


###########################################

def writeChessCoords():
  '''
  Loop over all squares of a chessboard
  and write their coordinates
  '''
  nX=nY=8    # the number of squares in x and y
  for j in range(1,nY+1):   # loop over y, on the outer loop
    for i in range(1,nX+1): # loop over x, on the inner loop
      print(i,j)
  

###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  # a chessboard has a fixed size, so I will not bother
  # reading the command line.
  writeChessCoords()

