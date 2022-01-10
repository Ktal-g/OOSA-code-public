
'''
Example of writing a file
'''

# import the reader
from readFile import readFile
from math import sqrt


#########################################

def writeFile(newName,x,y):
  '''File writing function'''
  f=open(newName,'w')
  for i in range(0,x.shape[0]):
    line=str(x[i])+" "+str(y[i])+"\n"
    f.write(line)
  f.close()
  print("Written to",newName)


#########################################

if __name__ == '__main__':
  '''Main'''
  filename="../data/Wiggle1.txt"
  # read data
  x,y=readFile(filename)
  # do some maths to the file
  y=y*sqrt(2)
  # write the results
  newName='aNewFile.txt'
  writeFile(newName,x,y)

