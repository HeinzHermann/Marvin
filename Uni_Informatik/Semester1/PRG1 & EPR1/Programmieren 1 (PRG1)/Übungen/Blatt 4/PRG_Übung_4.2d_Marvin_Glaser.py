"""program code, used to solve problem for EPR 4.2 d)"""

from math import sqrt, log, e  #an example 
#from numpy import array       #another example for third party module
#import meinmodul              #example for your own module 
 
__author__ = "4424114: Marvin Glaser"  #put your data here
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "marvin.glaser91@gmail.com" 


def string_to_number(user_input): 
    """function converts written number to int numbers in string type""" 
    if type(user_input) != type(""):
        return("ERROR")
        
    number_list = []
    number_list2 = ""
    user_input = user_input.split(",")
    counter = 0
    for number in user_input:
        if number == "null":
            number_list.append(0)
        elif number == "eins":
            number_list.append(1)
        elif number == "zwei":
            number_list.append(2)
        elif number == "drei":
            number_list.append(3)
        elif number == "vier":
            number_list.append(4)
        elif number == "fünf":
            number_list.append(5)
        elif number == "sechs":
            number_list.append(6)
        elif number == "sieben":
            number_list.append(7)
        elif number == "acht":
            number_list.append(8)
        elif number == "neun":
            number_list.append(9)
        else:
            return("ERROR")
            
        if counter == 3:
            break
        counter += 1
    
    for number2 in number_list:
        number_list2 += str(number2)

    return(number_list2)

def main():
    """executes the main body of this program"""
    user_numbers = input("--> ")
    false = 0
    #  variable that determines the cancellation of the number dekrementation
    
    converted_number = string_to_number(user_numbers)
    #  function used to convert user input to string of an integer
    
    #  if statement used to distinguish between number and error output
    if converted_number != "ERROR":
        converted_number = int(converted_number)
    else:
        print("ERROR")
    
        
    condition = True
    #  variable condtion used to continually loop while till termination
    while condition:
        if converted_number > (false + 2):
            converted_number -= 1
            #  dekrementation condition for converted_number
        elif converted_number == (false + 2):
            condition = False
            #  termination condition for while loop
            print("True")
        else:
            condition = False
            #  termination condition for while loop
            print("Out of range")


if __name__ == '__main__':
    main()


