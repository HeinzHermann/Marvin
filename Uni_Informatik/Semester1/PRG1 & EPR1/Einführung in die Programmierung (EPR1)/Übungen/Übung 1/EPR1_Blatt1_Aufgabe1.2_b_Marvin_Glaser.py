__author__ = "4424114: Marvin Glaser"

# EPR1
# Exerciise 1, 1.2 (b)
# Reihe


def log_2_series(iterations):
    """
    definition of a new function
    
    done to enable fast modification of number of iterations
    this eliminates the need to change the code directly
    """
    
    counter = 1
    total = 0

    while counter <= iterations:
        """
        while loop used to enable iteration
        
        variable "counter" used as "k" for the given equation
        and to count the number of loops till termination
        
        variable "iterations" dictates the number of iterations
        """
        
        total = total + ( ((-1) ** (counter + 1)) / counter)
        counter += 1
    
    print(total)


# execution of the code with 3, 9 and 15 iterations respectively

log_2_series(3)
log_2_series(9)
log_2_series(15)
