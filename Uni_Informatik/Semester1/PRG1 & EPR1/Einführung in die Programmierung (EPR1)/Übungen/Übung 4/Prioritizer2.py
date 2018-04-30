"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""


__author__ = "6539575: Marc-Robin Muth, 4424114: Marvin Glaser"  #put your data here
__credits__ = "To Kim, because she was always there...kind of"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mrmuth@outlook.com, marvin.glaser91@gmail.com"


def input_converter():
    """Docstring: Every subroutine and function has a docstring."""
    #  gatekeeper, richtige eingaben

    list_A = []
    list_B = []
    list_unspecific = []
    list_master = []
    
    user_input = ''
    #user_input = input('')
    #print(user_input)
    list_input = user_input.split(' ')
    #print(list_input)
    
    acceptable_commands = ['4r','A4','B4','3r','3h','A3','B3','2r','2h','A2',
                           'B2','1r','1h','A1','B1','Er','Eh','AE','BE','Kh',
                           'AK', 'BK'
                           ]
    
    print(list_input)
    if list_input == ['']:
        return([[],[],[]])
        #prüfen ob korrekt!!
    
    for order in list_input:
        if order not in acceptable_commands:
            return('ERROR')
    
    
    for order in list_input:
        #a = order[0]
        #b = order[1]
        if order[0] == 'A':
            try:
                too_add = (int(order[1])+1)
            except:
                if order[1] == 'K':
                    too_add = 0
                elif order[1] == 'E':
                    too_add = 1
            
            if too_add not in list_A:
                list_A.append(too_add)
                    
            

        elif order[0] == 'B':
            try:
                too_add = (int(order[1])+1)
            except:
                if order[1] == 'K':
                    too_add = 0
                elif order[1] == 'E':
                    too_add = 1
                    
            if too_add not in list_B:
                list_B.append(too_add)

        elif order[0] in 'KE1234':
            too_add = order
            if too_add not in list_unspecific:
                list_unspecific.append(too_add)
        
        else:
            return('ERROR')

    #print(list_A)
    #print(list_B)
    #print(list_unspecific)
    list_master.append(list_A)
    list_master.append(list_B)
    list_master.append(list_unspecific)
    #print(list_master)
    return(list_master)

def yourfunction_2():
    """Docstring for yourfunction_2(). """

    pass  #To be programed later.


def main():
    print(input_converter())

if __name__ == '__main__':
    main()
