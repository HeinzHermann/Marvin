"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""

import Prioritizer
import Elevator_A
import Elevator_B
import Printer

__author__ = "6539575: Marc-Robin Muth, 4424114: Marvin Glaser"
__credits__ = "To Kim, because she was always there...kind of"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mrmuth@outlook.com, marvin.glaser91@gmail.com"


def distribute():
    """Docstring: Every subroutine and function has a docstring."""
    #  gatekeeper, richtige eingaben

status_a = Elevator_A.elevation_A([0, 1, 1, []])
status_b = Elevator_B.elevation_B([0, 1, 1, []])
list_floor = ['K', 'E', '1', '2', '3', '4']


condition = True

while condition:

    list_order_a = status_a[3]
    list_order_b = status_b[3]

    condition2 = True
    user_lists = Prioritizer.input_converter()
    if user_lists != 'ERROR':
        condition2 = False
    

    for element in user_lists[0]:
        if status_a[1] != element:
            if element not in list_order_a:
                list_order_a.append(element)

    for element in user_lists[1]:
        if list_floor[status_b[1]] != element:
            if element not in list_order_b:
                list_order_b.append(element)

    if status_a[0] == 'up':
        for element2 in user_lists[2]:
            if element2[1] == 'h':
                try:
                    element_a = (int(element2[0])+1)
                except:
                    if element2[0] == 'K':
                        element_a = 0
                    elif element2[0] == 'E':
                        element_a = 1
                if element_a >= status_a[1]:
                    if element_a not in status_a[3]:
                        status_a[3].append(element_a)
    elif status_a[0] == 'down':
        for element2 in user_lists[2]:
            if element2[1] == 'r':
                try:
                    element_a = (int(element2[0])+1)
                except:
                    if element2[0] == 'K':
                        element_a = 0
                    elif element2[0] == 'E':
                        element_a = 1
                if element_a <= status_a[1]:
                    if element_a not in status_a[3]:
                        status_a[3].append(element_a)
    elif status_a[1] == status_a[2]:
        user_lists_3 = user_lists[2]
        try:
            element_user = (int(user_lists_3[0])+1)
        except:
            if user_lists_3[0] == 'K':
                element_user = 0
            elif user_lists_3[0] == 'E':
                element_user = 1
        status_a[3].append(element_user)
        status_a[2] = element_user
        #prüfung 1 element ungleich status!!!

    if status_a[1] < status_a[2]:
        status_a[0] = 'up'
        for element3 in user_lists[2]:
            if element3[1] == 'h':
                try:
                    element_a = (int(element3[0])+1)
                except:
                    if element3[0] == 'K':
                        element_a = 0
                    elif element3[0] == 'E':
                        element_a = 1
                if element_a > status_a[1]:
                    if element_a not in status_a[3]:
                        status_a[3].append(element_a)
    else:
        status_a[0] = 'down'
        for element3 in user_lists[2]:
            if element3[1] == 'r':
                try:
                    element_a = (int(element3[0])+1)
                except:
                    if element3[0] == 'K':
                        element_a = 0
                    elif element3[0] == 'E':
                        element_a = 1
                if element_a < status_a[1]:
                    if element_a not in status_a[3]:
                        status_a[3].append(element_a)

    if status_b[0] == 'up':
        for element2 in user_lists[2]:
            if element2[1] == 'h':
                try:
                    element_b = (int(element2[0])+1)
                except:
                    if element2[0] == 'K':
                        element_b = 0
                    elif element2[0] == 'E':
                        element_b = 1
                if element_b >= status_a[1]:
                    if element_b not in status_a[3]:
                        status_b[3].append(element_b)
    elif status_b[0] == 'down':
        for element2 in user_lists[2]:
            if element2[1] == 'r':
                try:
                    element_b = (int(element2[0])+1)
                except:
                    if element2[0] == 'K':
                        element_b = 0
                    elif element2[0] == 'E':
                        element_b = 1
                if element_b <= status_a[1]:
                    if element_b not in status_a[3]:
                        status_b[3].append(element_b)
    elif status_b[1] == status_b[2]:
            user_lists_3 = user_lists[2]
            try:
                element_user = (int(user_lists_3[0])+1)
            except:
                if user_lists_3[0] == 'K':
                    element_user = 0
                elif user_lists_3[0] == 'E':
                    element_user = 1
            status_b[3].append(element_user)
            status_b[2] = element_user

    if status_b[1] < status_b[2]:
        status_b[0] = 'up'
        for element4 in user_lists[2]:
            if element4[1] == 'h':
                try:
                    element_b = (int(element4[0])+1)
                except:
                    if element4[0] == 'K':
                        element_b = 0
                    elif element4[0] == 'E':
                        element_b = 1
                if element_b > status_b[1]:
                    if element_b not in status_b[3]:
                        status_b[3].append(element_b)
    else:
        status_b[0] = 'down'
        for element4 in user_lists[2]:
            if element4[1] == 'r':
                try:
                    element_b = (int(element4[0])+1)
                except:
                    if element4[0] == 'K':
                        element_b = 0
                    elif element4[0] == 'E':
                        element_b = 1
                if element_b < status_b[1]:
                    if element_b not in status_b[3]:
                        status_b[3].append(element_b)

    if status_a[1] < status_a[2]:
        for goal_a in status_a[3]:
            if goal_a > status_a[2]:
                status_a[2] = goal_a
    elif status_a[1] > status_a[2]:
        for goal_a in status_a[3]:
            if goal_a < status_a[2]:
                status_a[2] = goal_a

    if status_b[1] < status_b[2]:
        for goal_b in status_b[3]:
            if goal_b > status_b[2]:
                status_b[2] = goal_b
    elif status_b[1] > status_b[2]:
        for goal_b in status_b[3]:
            if goal_b < status_b[2]:
                status_b[2] = goal_b

    if status_a[0] == 0:
        if status_a[1] < status_a[2]:
            status_a[0] = 'up'
        elif status_a[1] > status_a[2]:
            status_a[0] = 'down'

    if status_b[0] == 0:
        if status_b[1] < status_b[2]:
            status_b[0] = 'up'
        elif status_b[1] > status_b[2]:
            status_b[0] = 'down'

    Printer.printer(status_a, status_b, user_lists[2])



def yourfunction_2():
    """Docstring for yourfunction_2(). """

    pass  #To be programed later.


def main():
    distribute()

if __name__ == '__main__':
    main()
