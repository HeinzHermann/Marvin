"""Program for binary search of a number in a list of numbers
"""

__author__ = "4424114: Marvin Glaser"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "Thanks to Carmen for braiding my hair"
__email__ = "marvin.glaser91@gmail.com"


class calculations:
    """class that performes the binary searching"""

    def calc_main(self, object1, object2):
        """main funktion of the class, starts searching algorithm"""

        self.sorted_list = object1
        self.sorted_list.sort()
        self.search_number = object2
        self.round = 1
        print('\nduplicates of the same number were removed\n'
              'and the list was sorted to enable the usage\n'
              'of a binary algorithm\n')
        print('the modified input list can be seen below:')
        print(str(self.sorted_list) + '\n')

        #  hashed code was used for 10.1

        #self.condition = True
        #while self.condition:
        #    self.calculations()
        self.calculations()


    def calculations(self):
        """function that performs binary algorithm"""

        length_list = len(self.sorted_list)
        self.middle = (length_list - 1) // 2

        #  special case, desired number was not found in list
        if length_list == 0:
            print('we are sorry, but the number you wree looking for\n'
                  'was not found in the list that was provided\n\n'
                  'the search ended after {} rounds'.format((self.round - 1))
                  )
            #self.condition = False
            #return

        #  check if middle number is equal to searched number
        else:
            if self.search_number == self.sorted_list[self.middle]:
                print('\n\ncomparison no. ' + str(self.round) + ':')
                print('compared {} with {}'.format(self.search_number,
                                                   self.sorted_list[self.middle])
                      )
                print('the number was found!!\n')
                print('\nthe number was found after {} '
                      'rounds of binary search'.format(self.round)
                      )
                #self.condition = False
                #return

            #  check if searched number is greater then middle number
            elif self.search_number > self.sorted_list[self.middle]:
                print('\n\ncomparison no. ' + str(self.round) + ':')
                print('compared {} with {}'.format(self.search_number,
                                                   self.sorted_list[self.middle])
                      )
                print('{} > {}\ndiscarded all numbers of list, that are ' \
                      'smaller or equal to {}\n'.format(self.search_number,
                                          self.sorted_list[self.middle],
                                          self.sorted_list[self.middle]
                                          )
                      )

                #  remove false list elements from back to front
                #  avoids index error
                for deletion in range(self.middle, -1, -1):
                    self.sorted_list.pop(deletion)
                print('new list: ' + str(self.sorted_list))
                self.round += 1
                self.calculations()
                #return

            #  check if searched number is smaller then middle number
            else:
                print('\n\ncomparison no. ' + str(self.round) + ':')
                print('compared {} with list element {}'.format(
                      self.search_number, self.sorted_list[self.middle])
                      )
                print('{} < {}\ndiscarded all numbers of list, that are ' \
                      'greater or equal to {}\n'.format(self.search_number,
                                          self.sorted_list[self.middle],
                                          self.sorted_list[self.middle]
                                          )
                      )

                #  remove false list elements from back to front
                #  avoids index error
                for deletion in range((len(self.sorted_list) - 1),
                                      (self.middle - 1), -1):
                    self.sorted_list.pop(deletion)
                print('new list: ' + str(self.sorted_list))
                self.round += 1
                self.calculations()
                #return

        return



class interface():
    """interface class taht interacts with user"""

    def ui_main(self):
        """main function of interface class, runs other functions"""
        self.get_input()

        #  create object for binary search algorithm
        calculator = calculations()
        calculator.calc_main(self.number_list, self.to_search)


    def gatekeeper(self):
        """gatekeeper 1, checks if enteed list is correct"""

        #  check for all valid characters in input string
        for character in self.user_input:
            if character not in self.valid_numbers and \
                    character not in [' ', '-']:
                return False

        self.number_list = []
        integer_list = self.user_input.split(' ')

        #  remove empty strings from double blank spaces
        to_remove = []
        for index in range(len(integer_list) - 1, -1, -1):
            if integer_list[index] == '':
                to_remove.append(index)

        for index in to_remove:
            integer_list.pop(index)

        #  generate valid list for sorting and searching
        for element in integer_list:
            self.number_list.append(int(element))

        #  check if list has at least 20 unique numbers
        if len(set(self.number_list)) < 20:
            return False

        else:
            return True


    def gatekeeper2(self):
        """gatekeeper 2, checks for valid input of search number"""

        #  check for valid characters
        #  if first string character is '-', allow for negative numbers
        if self.user_input2[0] == '-':
            for character in self.user_input2[1:]:
                if character not in self.valid_numbers:
                    return False
        else:
            for character in self.user_input2:
                if character not in self.valid_numbers:
                    return False

        return True


    def get_input(self):
        """asks user for list of numbers and searched number"""

        print('\nhello dear user\nthis program simulates the binary sort '
              'algorithm\nplease enter at least 20 unique integer numbers in '
              'arbitrary order\nthe program will sort them and apply the '
              'binary sort algorithm\nto the resulting list\n'
              )

        self.valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        #  remains True until valid input list was given
        while True:
            self.user_input = input('\nplease enter your numbers in the '
                                    'format \'1 2 22 123\'\n(separate the'
                                    ' numbers with blank spaces\nduplicates of'
                                    ' the same number\nwill automatically be '
                                    'removed)\n'
                                    )
            if self.gatekeeper():
                break
            else:
                print('\nwe are sorry, apparently your input contained '
                      'characters other\n'
                      'then integral numbers and blank spaces or you entered '
                      '20 or less unique\nnumbers. Please repead the  input'
                      ' step\n\n'
                      )

        #  create list of 20 or more unique numbers
        number_set = set(self.number_list)
        self.number_list = list(number_set)

        #  remains True till valid searched number is given
        while True:
            self.user_input2 = input('\nplease enter the number you are '
                                     'looking for now\n(the number must be an '
                                     'integer)\n'
                                     )

            if self.gatekeeper2():
                break
            else:
                print('\nwe are sorry, but your input seems to contain '
                      'invalid characters\n'
                      'Please enter an integral number without blank spaces\n'
                      )

        self.to_search = int(self.user_input2)



def main():
    """main function, creates sorter object and starts program"""
    sorter = interface()
    sorter.ui_main()


if __name__ == '__main__':
    main()
