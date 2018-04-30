"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import random

#from numpy import array       #another example for third party module
#import meinmod0ul              #example for your own module

__author__ = "6539575: Marc-Robin Muth, 4424114: Marvin Glaser"  #put your data here
__credits__ = "To Kim, because she was always there...kind of"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mrmuth@outlook.com, marvin.glaser91@gmail.com"

def elevation_A(update_elevator_A):
    """Docstring: Every subroutine and function has a docstring."""
    #  gatekeeper, richtige eingaben

    direction = update_elevator_A[0]
    status = update_elevator_A[1]
    goal = update_elevator_A[2]
    list_order = update_elevator_A[3]
    list_output = []
    list_floor = ['K', 'E', '1', '2', '3', '4']

    if isinstance(direction, int):
        if direction > 0:
            direction -= 1
            list_output.append(direction)
            list_output.append(status)
            list_output.append(goal)
            list_output.append(list_order)
            return list_output

        else:
            return update_elevator_A

    for goals in list_order:
        if status == goals:
            direction = random.randrange(0, 3)
            list_order.remove(goals)

            list_output.append(direction)
            list_output.append(status)
            list_output.append(goal)
            list_output.append(list_order)

            return list_output

    if direction == 'up':
        status += 1
        list_output.append(direction)
        list_output.append(status)
        list_output.append(goal)
        list_output.append(list_order)

        return list_output

    elif direction == 'down':
        status -= 1
        list_output.append(direction)
        list_output.append(status)
        list_output.append(goal)
        list_output.append(list_order)

        return list_output


def main():
    elevation_A()

if __name__ == '__main__':
    main()
