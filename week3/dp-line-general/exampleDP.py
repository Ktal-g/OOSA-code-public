

'''
An example of one potential
solution for Douglas-Peucker
line generalisation
SH 2019-02-01
'''

import argparse
import numpy as np

# to allow it to import week 3's work, add the week 3 folder to your PYTHONPATH
import sys
sys.path.append("../../week3/reproject")   # NOTE, make sure this points to a directory with vectorExample.py
from vectorExample import reprojectData
 
sys.path.append('../line_distance')
from perpendicular_distance import perp_dist   # James' line distance


#####################################

def readCommands():
  '''
  Read the command line
  '''
  p = argparse.ArgumentParser(description=("A Douglas-Peucker line generalisation"))
  p.add_argument("--input",dest="inName",type=str,default='../data/squirrel_ordered.txt',help=("Input filename"))
  p.add_argument("--tolerance",dest ="tol",type=float, default=10.0, help=("Tolerance of generalisation\nDefault = 10"))
  p.add_argument("--epsg",dest ="epsg",type=int, default=27700, help=("EPSG to do analysis in\nDefault = 27700"))
  cmdargs = p.parse_args()
  return(cmdargs)


#####################################

def generaliseDP(iS,iE,x,y,tol,nodeIndices):  # note that I have renamed the start and end indices
  '''
  The line generalisation function
  '''

  # check that there are sufficient points here. Once they are adjacent, stop
  if((iE-iS)<2):
   return

  # calcuate distance from the line for all points
  distances=perp_dist(x[iS],x[iE],x,y[iS],y[iE],y)

  # we only want to test distances within our region of interest, so set values outside to 0
  distances[0:iS]=0.0            
  distances[iE:len(x)]=0.0

  # find maximum distance from line and test against our tolerance
  maxDist=np.max(distances)
  if(maxDist>tol):  # if beyond tolerance, identify a node point
    nodeInd=np.argmax(distances)   # this finds the index of the maximum value
    print(iS,iE,nodeInd)           # print out the bounds to help us debug
    # record new node point in a list of all points
    nodeIndices.append(nodeInd)
    # repeat for the array to the left of the split
    generaliseDP(iS,nodeInd,x,y,tol,nodeIndices)
    # repeat for the array to the right of the split
    generaliseDP(nodeInd,iE,x,y,tol,nodeIndices)


#####################################

def writeResults(x,y,inds):
  '''
  Write out the results
  Alternatively you could 
  plot them using week 2's code
  '''
  for i in inds:
    print(i,x[i],y[i])


#####################################

if __name__ == "__main__":
  '''
  Main block
  '''
  cmdargs=readCommands()
  # read data in to numpy arrays. Here i have pre-sorted the data
  lon,lat=np.loadtxt(cmdargs.inName,unpack=True,usecols=(0,1),dtype=float,comments='#',delimiter=' ')

  # reproject
  x,y=reprojectData(lon,lat,cmdargs.epsg)

  # first and last point are our first break points
  startInd=0
  endInd=len(x)-1

  # create a list to hold the results. Put first two breakpoints in
  nodeIndices=[startInd,endInd]

  # call generaliser
  generaliseDP(startInd,endInd,x,y,cmdargs.tol,nodeIndices)

  # sort the indices, as they will be in a funny order
  sortedIndices=np.sort(nodeIndices)

  # write out results
  writeResults(x,y,sortedIndices)

