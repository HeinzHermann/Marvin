__author__ = "4424114: Marvin Glaser"

# EPR1
# Exercise 2, 2.1 b)

input_number = input("--> ")

def rules(number):
    list_number = list(str(number))
    # convert number to string in order to create list
    condition1 = False
    if (number % 3) == 0:
        condition1 = True
    else:
        if "3" in list_number:
            condition1 = True
    # check if condtion 1 is true
    condition2 = False
    if (number % 7) == 0:
        condition2 = True
    else:
        if "7" in list_number:
            condition2 = True
    # check if condtion 2 is true
    if (condition1 == True) and (condition2 == True):
        return("fizzbuzz")
    elif condition1 == True:
        return("fizz")
    elif condition2 == True:
        return("buzz")
    else:
        return(number)
    # check if either both, one or neither of the condtions are true

try:
    input_number = int(input_number)
    # check for input beeing letters or float, since strings of letters or decimal
    # numbers cause ValueError with int() function
    if input_number >= 1 and input_number <= 999:
        print(rules(input_number))
        # if range for number is met, execute function
    else:
        print("ERROR")
except:
    print("ERROR")