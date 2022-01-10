

'''
An example of a nested loop,
using chessboard colour
SH 2019-02-03
'''


###########################################

def setColours(j):
  '''
  Label the odd and even square colours
  '''
  if((j%2)==1):  # an odd line. First square black
    oddSquare="black"
    evenSquare="white"
  else:          # an even line. First square white
    oddSquare="white"
    evenSquare="black"
  return(oddSquare,evenSquare)


###########################################

def writeChessColour():
  '''
  Loop over all squares of a chessboard
  and write their coordinates
  '''
  nX=nY=8    # the number of squares in x and y
  for j in range(1,nY+1):   # loop over y, on the outer loop
    # is the first square in this line black or white?
    oddSquare,evenSquare=setColours(j)
    for i in range(1,nX+1): # loop over x, on the inner loop
      if((i%2)==1):   # odd square
        colour=oddSquare
      else:
        colour=evenSquare
      print(i,j,colour)
  

###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  # a chessboard has a fixed size, so I will not bother
  # reading the command line.
  writeChessColour()

