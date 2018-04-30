"""Docstring: program code, used to solve problem for EPR 4.2 b)"""

from math import sqrt, log, e  #an example 
#from numpy import array       #another example for third party module
#import meinmodul              #example for your own module 
 
__author__ = "4424114: Marvin Glaser"  #put your data here
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "marvin.glaser91@gmail.com" 
  
def iterative_implementation(n): 
    """iterative implementation of given function""" 

    if n <= 1:
        return n
    else:
        return(iterative_implementation((n-1))
        + iterative_implementation((n-2)))
    
 
def main():
    """executes the main body of this program"""
    iterative_implementation(32)
    


if __name__ == '__main__':
    main()


