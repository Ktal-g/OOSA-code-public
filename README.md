# Public code for the OOSA course.

There is a separate directory for each week's work. As we progress, suggested answers will be uploaded.

## Foundations

The **foundations** folder contains some warm up exercises to transition on to the course. There are two folders within:

* basic\_features
* iterating

The basic\_features folder contains a set of scripts introducing the basic Python features (data types, loops, plotting etc.). Other than **06_objects.py**, which will be covered in week 2, these should already be familar to you and are included here for revision.

The **iterating** directory contains some exercises to practice using loops and work up to moving around a raster dataset.


## Week 1

Week 1 covers:

***Aspects***
* Github version control and code repository
* Computer basics 
* Revision of loops and file I/O

***Algorithm***
* Introduction to algorithm design: Finding minima and sorting


### fileIO

Contains two scripts to demonstrate reading from a text file and writing to a text file. The ***data*** folder contains the data for the file reading example.


### data

Contains a text file with some sample data to practice reading with the fileIO code.


### sort

Contains an example solution for a simple sort. Note that there are multiple sort solutions, such as bubble sort, and then many more complex and efficient algorithms.



## Week 2

Week 2 covers

***Aspects***
* Using the command line to make programmable programs
* Objects and classes

***Algorithm***
* Binary search: Loop and recursion


### main

Contains an example of the main block in order to ease importing code in to other programs


### docu\_strings

Contains examples of document strings.
Week 2 covers

***Aspects***
* Using the command line to make programmable programs
* Objects and classes

***Algorithm***
* Binary search: Loop and recursion

### command\_line

Contains two example python files, which can be used to alter the behaviour of a program at run time. This allows you to create a single python program and then reuse it with different input files, options etc.

    commandExample.py: Minimum workable example of a command line
    commandLineIllus.py: Illustrates the common command 


### objects

Includes a script with a simple example of an object; a grouping of data and functions.


### data

Contains some text data files for use in this week's exercises.


### binary\_search

Contains the answer for week 2's algorithm.

    binarySearches.py: contains suggested answers for binary search by loop and recursion
    finishedQuartiles.py: uses the above to find quartiles in a sorted dataset
    searchObject.py: begins an object for sorting data
    makeData.py: makes data for testing algorithms
    randomWages.py: generates random wage data for testing algorithms


## Week 3

Week 3 covers

***Aspects***
* Geospatial packages: pyproj and gdal
* A note on function input/output
* Function fitting
* A mention of pandas
* Geospatial data formats; HDF5

***Algorithm***
* Douglas-Peucker line generalization


### reproject

Shows an example of using the dgal package to reproject raster or vector data.


### function\_fit

Shows an example of fitting a function to data.


### pointer\_reference

Demonstrates the difference between variables that point to an array and copying a whole array.

### pandas

Shows an example of reading data into a pandas object.


### hdf

Shows an example of reading HDF data in to RAM, in this case using LVIS data.


### line\_distance

A function to find the orthogonal distance between a line and a point, to be used in the Douglas-Peucker line generalization algorithm.


### dp-line-general

An example solution for Douglas-Peucker line-generalisation. This one uses recursion and imports a script from a different folder usingf PYTHONPATH.


### data

Contains data to be used in week 3's exercises.


