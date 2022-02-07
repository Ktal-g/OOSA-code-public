
'''
An example of how to use the 
LVIS python scripts
'''

# import the HDF5 data handler class

from processLVIS import lvisGround   # we are importing the version with
                                     # the ground-finding algorithm
from pyproj import Proj, transform
import matplotlib.pyplot as plt
import argparse
import numpy as np


##########################################

def getCmdArgs():
  # function description for use within python
  '''
  Get commandline arguments
  '''
  # create an argparse object with a useful help comment
  p = argparse.ArgumentParser(description=("An illustration of a command line parser"))
  # read a string
  p.add_argument("--input",dest="inName",type=str,default='/geos/netdata/oosa/week4/lvis_antarctica/ILVIS1B_AQ2015_1014_R1605_070717.h5',help=("Input filename"))
  p.add_argument("--outRoot",dest="outRoot",type=str,default='waveforms',help=("Output filename root"))
  # parse the command line into an object
  cmdargs = p.parse_args()
  # return that object from this function
  return cmdargs


##########################################

class plotLVIS(lvisGround):
  '''A class, ineriting from lvisGround
     and add a plotting method'''

  def reprojectLVIS(self,outEPSG):
    '''A method to reproject the footprint coordinates'''
    # set projections
    inProj=Proj(init="epsg:4326")
    outProj=Proj(init="epsg:"+str(outEPSG))
    # reproject data
    self.x,self.y=transform(inProj, outProj, self.lon, self.lat)


  def reprojectBounds(self,outEPSG):
    '''A method to reproject the file bounds'''
    # set projections
    inProj=Proj(init="epsg:4326")
    outProj=Proj(init="epsg:"+str(outEPSG))
    # reproject data
    self.bounds[0,2],self.bounds[1,3]=transform(inProj, outProj, self.bounds[0,2], self.bounds[1,3])


  def plotWaves(self,outRoot="waveform",step=1):
    '''A method to plot all waveforms'''

    # loop over list of waveforms
    for i in range(0,self.nWaves,step):
      self.plotWave(i,outRoot=outRoot)


  def plotWave(self,i,outRoot="waveform"):
    ''''A method to plot a single waveform'''
    outName=outRoot+"."+str(i)+".png"
    plt.plot(self.waves[i],self.z[i])
    plt.xlabel("Waveform return")
    plt.ylabel("Elevation (m)")
    plt.savefig(outName)
    plt.close()
    print("Graph to",outName)


##########################################


if __name__=="__main__":
  '''Main block'''

  # read the command line
  cmd=getCmdArgs()
  filename=cmd.inName
  outRoot=cmd.outRoot

  # create instance of class with "onlyBounds" flag
  b=plotLVIS(filename,onlyBounds=True)

  # set a steo size (note that this will be in degrees)
  step=(b.bounds[2]-b.bounds[0])/6

  # below, (x0,y0) is the bottom left corner of our tile
  #   (x1,y1) is the top right corner of our tile

  # loop over spatial subsets
  for x0 in np.arange(b.bounds[0],b.bounds[2],step):  # loop over x tiles
    x1=x0+step   # the right side of the tile
    for y0 in np.arange(b.bounds[1],b.bounds[3],step):  # loop over y tiles
      y1=y0+step  # the top of the tile

      # print the bounds to screen as a sanity check
      print("Tile between",x0,y0,"to",x1,y1)

      # read in all data within our spatial subset
      lvis=plotLVIS(filename,minX=x0,minY=y0,maxX=x1,maxY=y1)

      # set elevation, though this is not used here, but would be if you
      lvis.setElevations()    # were making a DTM

      # reproject the data. This is also not used here, but would be if you
      lvis.reprojectLVIS(3031)    # were making a DTM

      # plot up some waveforms using your new method
      lvis.plotWaves(step=int(lvis.nWaves/100),outRoot=outRoot+".x."+str(x0)+".y."+str(y0))  # this will print 100 waveforms
                                                                                # updating the filename as it goes

