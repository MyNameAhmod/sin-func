#!/usr/bin/env python

# system include files
#
import sys
import os
import numpy as np
import math

# excute a sin function with the variable given from the command line 
#
def sin_func(argv, N, freq, fsample, amp):

     # create a list to hold value
     #
     array =  [] 
     
     # run sin to calculate the 
     #
     for x in range(0,fsample*N):
     
          # asign the value to array
          #
          val = amp*math.sin(2 * math.pi * freq* (x/fsample))
          
          # add the value of the sine funtion to a list
          #
          array.append((val))
          
     # end of for loop
          
     # can a np.array that turn all daa type into short integer 
     #
     num  = np.array(array, dtype = np.short)

     # convert num to binary text
     # 
     bytes_num = bytearray(num)

     # open the file where we will be writting the text
     #
     b = open(argv[1], "wb")

     # write the binary form of the data to the 
     #
     b.write(bytes_num)

     # close the file
     #
     b.close()
    

# end of function
                       
# check the number of argument given in the command line
#
def check(argv):

     # check the amount of argument
     #
     if len(sys.argv) != 6:

          # open the file
          #
          with open("help.txt") as help_file:
               print(help_file.read())
               exit()
          # end of with open
     # end of if statement
# end of function
                       
# main: this is the main function of this Python
#
# int main(int argc, char** argv)
#
def main(argv):

     # check the number of argv
     #
     check(argv) 

     # define variable use in program
     #
     N = int(argv[2]) 
     freq = int(argv[3])
     fsample = int(argv[4])
     amp = int( argv[5])
  
     # for loop tha hold value with th different channel
     #
     sin_func(argv, N, freq, fsample, amp)
         
# end of main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end of file
