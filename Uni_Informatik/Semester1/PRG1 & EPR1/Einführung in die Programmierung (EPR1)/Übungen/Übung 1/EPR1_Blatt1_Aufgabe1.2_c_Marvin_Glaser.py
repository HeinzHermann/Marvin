__author__ = "4424114: Marvin Glaser"

# EPR1
# Exerciise 1, 1.2 (c)
# Input Summe

"""
strategy for problem:
use eval() funktion to enable defintion of four variables
with the given input method
"""

INPUT1, INPUT2, INPUT3, INPUT4 = eval(input("--> "))

LIST_USER_INPUT = [INPUT1, INPUT2, INPUT3, INPUT4]

"""
create list of inputs to enable use of sum() funktion
"""

print(sum(LIST_USER_INPUT))

