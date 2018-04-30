"""Docstring: program code, used to solve problem for EPR 4.2 a)"""

from math import sqrt, log, e  #an example 
#from numpy import array       #another example for third party module
#import meinmodul              #example for your own module 
 
__author__ = "4424114: Marvin Glaser"  #put your data here
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "marvin.glaser91@gmail.com" 
  
def ack(n, m): 
    """implementation of Ackermann function"""
    if n == 0:
        return((m + 1))
    elif (m == 0) and (n != 0):
        return(ack((n - 1), 1))
    else:
        return(ack((n - 1), ack(n, (m - 1))))

def main():
    """executes the main body of this program"""
    ack(3,5)

if __name__ == '__main__':
    main()
