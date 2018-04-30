__author__ = "4424114: Marvin Glaser"

# PRG1
# Exercise 2, 2.4

"""
strategy:
convert "Hobby Wert" to binary numbers and collect numbers in list
cycle though generated list and search for "1" values in binary list
output corresponding activities
"""

hobby_value = float(input("--> "))

def binarisator(input_number):
    binary_list = []
    
    # define function to convert decimal input to binary list
    # creat empty list, that can be filled with binaries    
        
    while input_number >= 1:
        binary_list.append(int(input_number % 2))
        input_number = (input_number // 2)
        # calculation to convert decimal to binary
        # reversal of list not necessarry, since .append() adds number to end of list
    return binary_list


def hobby_output(list_in_binary):
    # define function to output lowest value activity
        
    counter = 0
    list_output = []
    list_hobbies = ["Schwimmen", "Brettspiele", "Angeln", "Kochen", "Laufen",
                    "Fussball spielen", "Klavier spielen", "Naehen"]
    # useing a counter in following for loop to determine activity postion in list_hobbies
    # defined output list, that will be returned at the end of the function
    
    for position in list_in_binary:

        if position == 1:
            list_output.append(list_hobbies[counter])
            counter += 1
            # if checked element in binary list == 1, coressbonding activity is added
            # to output list and coutner is increased by 1
        
        else:
            counter += 1
            # if checked element of binary list != 1, counter is raised by 1
        
    return list_output

if hobby_value <= 255 and hobby_value >= 0:
    # check, if input is in the appropriate range of 0 to 265
    
    final_output = hobby_output(binarisator(hobby_value))
    
    if len(final_output) == 0:
        print("Keine Hobbies")
    
    else:
        for output in final_output:
            print(output)
else:
    print("Keine Hobbies")