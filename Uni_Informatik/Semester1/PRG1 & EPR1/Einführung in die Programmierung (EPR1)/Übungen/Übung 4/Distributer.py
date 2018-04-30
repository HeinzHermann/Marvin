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

status_a = [0, 1, 1, []]
status_b = [0, 1, 1, []]
list_floor = ['K', 'E', '1', '2', '3', '4']

print('Hello dear User, we present to you the elevation simulator :) \n'
      'Your orders need to be typed as two characters, separated by one blank \n'
      'You can either order from within the elevators or from the floors\n'
      'to order from within an elevator, type \"A\" or  \"B\" as your first\n'
      'character, followed by a number between 1 and 4 (for Floor 1 to 4),\n'
      '\"E\" (Erdgeschoss, ground level) or \"K\" (Keller, basement).\n'
      'To order an elevator form one of the floors, type K, E or 1 to 4 as\n'
      'your first character and \"h\" (hoch, up) or \"r\" (runter, down) as\n'
      'your second character\n'
      'Attention: \"K\" as a first character can only be combined with \"h\" \n'
      'and \"4\" as a first character can only be combined with \"r\". But \n'
      'otherwise you are free to choose any valid combination :)')

condition = True
while condition:

    status_a = Elevator_A.elevation_A(status_a)
    status_b = Elevator_B.elevation_B(status_b)

    list_order_a = status_a[3]
    list_order_b = status_b[3]

    #print('status_a0', status_a)
    #print('status_b0', status_b)

    condition2 = True
    while condition2:
        user_lists = Prioritizer.input_converter()
        if user_lists != 'ERROR':
            condition2 = False
        else:
            print('\nCarefull, your Input contained invalid orders!!\n'
                  'All possible valid orders are:\n\n'
                  'A4, B4, A3, B3, A2, B2, A1, B1, AK, BK, AE\n'
                  'BE, 3h, 2h, 1h, Eh, Kh, 4r, 3r, 2r, 1r, Er')

    printer_order_list = user_lists[2]
    printer_order_list = printer_order_list[:]
    #print(user_lists)
    

    for element in user_lists[0]:
        if status_a[1] != element:
            if element not in list_order_a:
                list_order_a.append(element)

    for element in user_lists[1]:
        if status_b[1] != element:
            if element not in list_order_b:
                list_order_b.append(element)


    if status_a[1] < status_a[2]:
        for goal_a in status_a[3]:
            if goal_a > status_a[2]:
                status_a[2] = goal_a
    elif status_a[1] > status_a[2]:
        for goal_a in status_a[3]:
            if goal_a < status_a[2]:
                status_a[2] = goal_a
    else:
        if status_a[3] != []:
            new_status = status_a[3]
            status_a[2] = new_status[0]


    if status_b[1] < status_b[2]:
        for goal_b in status_b[3]:
            if goal_b > status_b[2]:
                status_b[2] = goal_b
    elif status_b[1] > status_b[2]:
        for goal_b in status_b[3]:
            if goal_b < status_b[2]:
                status_b[2] = goal_b
    else:
        if status_b[3] != []:
            new_status = status_b[3]
            status_b[2] = new_status[0]

    #print('status_a1', status_a)
    #print('status_b1', status_b)

    if status_a[1] < status_a[2]:
        for element2 in user_lists[2]:
            if element2[1] == 'h':
                element_a = element2[0]
                try:
                    element_a = int(element_a) + 1
                except:
                    if element_a == 'K':
                        element_a = 0
                    elif element_a == 'E':
                        element_a = 1
                if element_a >= status_a[1]:
                    if element_a not in status_a[3]:
                        status_a[3].append(element_a)
    elif status_a[1] > status_a[2]:
        for element2 in user_lists[2]:
            if element2[1] == 'r':
                element_a = element2[0]
                try:
                    element_a = int(element_a) + 1
                except:
                    if element_a == 'K':
                        element_a = 0
                    elif element_a == 'E':
                        element_a = 1
                if element_a <= status_a[1]:
                    if element_a not in status_a[3]:
                        status_a[3].append(element_a)
    elif status_a[1] == status_a[2]:
        user_lists_3 = user_lists[2]
        if user_lists_3 != []:
            element_user = user_lists_3[0]
            try:
                element_user = int(element_user[0]) + 1
            except:
                if element_user == 'K':
                    element_user = 0
                elif element_user == 'E':
                    element_user = 1
            status_a[3].append(element_user)
            status_a[2] = element_user
            user_lists[2].remove(user_lists_3[0])
            #prüfung 1 element ungleich status!!!


    if status_b[1] < status_b[2]:
        for element2 in user_lists[2]:
            if element2[1] == 'h':
                element_b = element2[0]
                try:
                    element_b = int(element_b) + 1
                except:
                    if element_b == 'K':
                        element_b = 0
                    elif element_b == 'E':
                        element_b = 1
                if element_b >= status_a[1]:
                    if element_b not in status_a[3]:
                        status_b[3].append(element_b)
    elif status_b[1] > status_b[2]:
        for element2 in user_lists[2]:
            if element2[1] == 'r':
                element_b = element2[0]
                try:
                    element_b = int(element_b) + 1
                except:
                    if element_b == 'K':
                        element_b = 0
                    elif element_b == 'E':
                        element_b = 1
                if element_b <= status_a[1]:
                    if element_b not in status_a[3]:
                        status_b[3].append(element_b)
    elif status_b[1] == status_b[2]:
            user_lists_3 = user_lists[2]
            if user_lists_3 != []:
                element_user = user_lists_3[0]
                try:
                    element_user = (int(element_user[0]) + 1)
                except:
                    if element_user[0] == 'K':
                        element_user = 0
                    elif element_user[0] == 'E':
                        element_user = 1
                status_b[3].append(element_user)
                status_b[2] = element_user
                user_lists[2].remove(user_lists_3[0])


    if status_a[1] < status_a[2]:
        for goal_a in status_a[3]:
            if goal_a > status_a[2]:
                status_a[2] = goal_a
    elif status_a[1] > status_a[2]:
        for goal_a in status_a[3]:
            if goal_a < status_a[2]:
                status_a[2] = goal_a
    else:
        if status_a[3] != []:
            new_status = status_a[3]
            status_a[2] = new_status[0]


    if status_b[1] < status_b[2]:
        for goal_b in status_b[3]:
            if goal_b > status_b[2]:
                status_b[2] = goal_b
    elif status_b[1] > status_b[2]:
        for goal_b in status_b[3]:
            if goal_b < status_b[2]:
                status_b[2] = goal_b
    else:
        if status_b[3] != []:
            new_status = status_b[3]
            status_b[2] = new_status[0]


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


    #print('status_a2', status_a)
    #print('status_b2', status_b)
    Printer.printer(status_a, status_b, printer_order_list)



def main():
    distribute()

if __name__ == '__main__':
    main()
