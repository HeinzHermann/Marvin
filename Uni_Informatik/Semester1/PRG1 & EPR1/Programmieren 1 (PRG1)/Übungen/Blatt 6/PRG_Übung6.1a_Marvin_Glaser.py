"""the module creates a matrix of the size n x m (user defined)
the values of the cells are determined randomly and printed into the
console.
"""

import random


__author__ = "4424114: Marvin Glaser"  #put your data here
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "marvin.glaser91@gmail.com" 


def gate_keeper():
    """gate_keeper takes the user input, checks for false input and executes
    other functions for matrix creation
    """
    
    gate1 = True
    #  gate1 will repeat while loop till input is correct
    while gate1:
        user_row = input("Please enter an integral number that is greater"
                         "than 1,\nin order to choose the number of rows "
                         "in your matrix\n"
                         )
        
        try:
            if isinstance(user_row, float):
                print("\n\nSorry, but your input was invalid")
            else:
                user_row = int(user_row)
                if user_row < 2:
                    print("\n\nSorry, but your input was invalid")       
                else:
                    gate1 = False
        except:
            print("\n\nSorry, but your input was invalid")

    gate2 = True
    #  gate1 will repeat while loop till input is correct
    while gate2:
        user_column = input("Please enter an integral number that is greater"
                         "than 1,\nin order to choose the number of colums "
                         "in your matrix\n"
                         )
        
        try:
            if isinstance(user_column, float):
                print("\n\nSorry, but your input was invalid")
            else:
                user_column = int(user_column)
                if user_column < 2:
                    print("\n\nSorry, but your input was invalid")       
                else:
                    gate2 = False
        except:
            print("\n\nSorry, but your input was invalid")       
    
    print("Your maxtrix is displayed below:\n")
    matrix_printer(create_matrix(user_row, user_column))
    
            
def create_matrix(n, m): 
    """function creates matrix of user defines size""" 
    
    numbers_n = []
    numbers_m = []
    #  lists of variable length to construct dictionary key for matrix cells
    
    output = []
    
    for counter in range(n):
        numbers_n.append(counter)
    
    for counter2 in range(m):
        numbers_m.append(counter2)

    matrix = {}
    for row_number in numbers_n:
        for column_number in numbers_m:
            key = (row_number, column_number)
            #  if statement to ensure that at least 4 numbers
            #  of different magnitude are present in matrix
            if key == (0, 0):
                matrix[key] = random.randrange(0,9)
            elif key == (0, 1):
                matrix[key] = random.randrange(10, 99)
            elif key == (1, 0):
                matrix[key] = random.randrange(100,999)
            elif key == (1, 1):
                matrix[key] = random.randrange(1000, 9999)
            else:
                matrix[key] = random.randrange(0, 9999)
    
    output.append(n)
    output.append(m)
    output.append(matrix)
    
    """output contains three elements
    element [0] is number of rows
    element [1] is number of columns
    element [2] is dictionary with all cell nubmers as keys and random numbers
    as values
    """
    return output

def matrix_printer(matrix_info):
    """matrix_printer prints every row of the matrix in the console"""

    numbers_row = []
    numbers_column = []
    output_matrix = matrix_info[2]
    
    for row in range(matrix_info[0]):
        numbers_row.append(row)
    for column in range(matrix_info[1]):
        numbers_column.append(column)
    
    

    for row_number in numbers_row:
        output_row = []
        for column_number in numbers_column:
            key = (row_number, column_number)
            output_row.append(output_matrix[key])
            #  all values of maxtrix in current row are added to output row            
        output_row = str(output_row)
        output_row = output_row[1:-1].replace(",", "")
        #  output row is formated and final row is printed
        #  output_row is reset after this process (beginning of for in loop)
        print(output_row)
        

def main():
    """main part of the module. only executed, when modul is run and not
    imported
    """

    gate_keeper()

if __name__ == '__main__':
    main()

