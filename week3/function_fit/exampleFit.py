

'''
Finds a line of best fit
to scatter data
'''


import numpy as np
import matplotlib.pyplot as plt


##################################

class dataFit(object):
  '''
  Class to hold our
  data and methods
  '''

  def __init__(self,filename):
    '''Read data from file and store'''
    self.wage,self.age=np.loadtxt(filename,delimiter=',',usecols=(0,1),unpack=True,dtype=float,comments="#")


  def fitLine(self):
    '''Fit a straight line through data and determine statistics'''
    # straight line coefficients
    self.m,self.c=np.polyfit(self.age,self.wage,1)
    # correlation coefficicent
    self.correl=np.corrcoef(self.age,self.wage)[0][-1]
    print("Correlation is",self.correl)
    # other error metrics are available

    # scipy.linregress() is another good package for straight lines


  def plotLine(self,outName):
    '''Plot our line of best fit'''

    # make the line
    minX=np.min(self.age)
    maxX=np.max(self.age)
    x=np.arange(minX,maxX,1)
    y=x*self.m+self.c

    # plot the two
    plt.plot(self.age,self.wage,'.')
    plt.plot(x,y)
    plt.xlabel('Age (years)')
    plt.ylabel('Wage (pounds sterling)')
    plt.savefig(outName) # write the graph to a file
    plt.close()           # close the file
    plt.clf()             # clear everything so we can start a new plot
    print("Graph drawn to",outName)


##################################

if __name__=="__main__":
  '''The main block'''

  # read data in to object
  filename="../data/wages.csv"
  dataObj=dataFit(filename)

  # fit line
  dataObj.fitLine()

  # plot it
  outName="linePlot.png"
  dataObj.plotLine(outName)

