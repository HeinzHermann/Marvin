"""Docstring: A very short sentence explaining the function. < 79 characters.

Additional information if required and more infos. Complete sentences please.
"""


#from numpy import array       #another example for third party module
#import meinmod0ul              #example for your own module

__author__ = "6539575: Marc-Robin Muth, 4424114: Marvin Glaser"  #put your data here
__credits__ = "To Kim, because she was always there...kind of"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mrmuth@outlook.com, marvin.glaser91@gmail.com"


def printer(info_a, info_b, floor_orders):
    """Docstring: Every subroutine and function has a docstring."""
    #  gatekeeper, richtige eingaben

    dic_printer = {'A5':'   ','B5':'   ','A4':'   ','B4':'   ','A3':'   ',
                   'B3':'   ','A2':'   ','B2':'   ','A1':'   ','B1':'   ',
                   'A0':'   ','B0':'   '
                   }

    order_variables_up = ['3h','2h','1h','Eh','Kh']
    order_variables_down = ['4r','3r','2r','1r','Er']

    for variables in order_variables_up:
        if variables in floor_orders:
            dic_printer[variables] = "[ up ]"
        else:
            dic_printer[variables] = "[    ]"
    
    for variables in order_variables_down:
        if variables in floor_orders:
            dic_printer[variables] = "[down]"
        else:
            dic_printer[variables] = "[    ]"
    
    location_A = "A" + str(info_a[1])
    location_A = location_A.replace('[','')
    location_A = location_A.replace(']','')
    dic_printer[location_A] = '[A]'
    
    location_B = "B" + str(info_b[1])
    location_B = location_B.replace('[','')
    location_B = location_B.replace(']','')
    dic_printer[location_B] = '[B]'
        

    print('Floor    Floor Order      Elevators ')
    print('')
    print('  4     ' + dic_printer['4r'] + '   ' + '    ' + '     |' + dic_printer['A5'] + '| |' + dic_printer['B5'] + '|')
    print('  3     ' + dic_printer['3r'] + ' ' + dic_printer['3h'] + '     |' + dic_printer['A4'] + '| |' + dic_printer['B4'] + '|')
    print('  2     ' + dic_printer['2r'] + ' ' + dic_printer['2h'] + '     |' + dic_printer['A3'] + '| |' + dic_printer['B3'] + '|')
    print('  1     ' + dic_printer['1r'] + ' ' + dic_printer['1h'] + '     |' + dic_printer['A2'] + '| |' + dic_printer['B2'] + '|')
    print('  E     ' + dic_printer['Er'] + ' ' + dic_printer['Eh'] + '     |' + dic_printer['A1'] + '| |' + dic_printer['B1'] + '|')
    print('  K     ' + '      ' + ' ' + dic_printer['2h'] + '     |' + dic_printer['A0'] + '| |' + dic_printer['B0'] + '|')



def main():
    printer([[],[2]], [[],[3]], ["3h", "4r", "Kh", "1h", "1r"])

if __name__ == '__main__':
    main()
