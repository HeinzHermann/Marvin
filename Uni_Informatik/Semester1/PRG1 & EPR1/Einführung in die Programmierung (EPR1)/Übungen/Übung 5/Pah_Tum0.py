"""This module symulates elevator A moving up/down,
stoping at the correct floors and removing finished
orders from its own "to do" list
"""

import random
import os
import tkinter as tk

__author__ = "6539575: Marc-Robin Muth, 4424114: Marvin Glaser"  #put your data here
__credits__ = "To Kim, because she was always there...kind of"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mrmuth@outlook.com, marvin.glaser91@gmail.com"

class board_game():
    """"""
    def __init__(self):
        self.board = {}

    def field(self):
        self.list_width = ['1', '2', '3', '4', '5', '6', '7']
        self.list_height = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.list_field = []

        for element in self.list_height:
            for element2 in self.list_width:
                self.list_field.append(element + element2)

        for key in self.list_field:
            self.board[key] = ' '

    def blocked(self):
        list_blocked = []
        self.number_blocks = random.randrange(5, 14, 2)
        for number in range(self.number_blocks):
            while True:
                to_blocked = random.randrange(0, 49)
                if to_blocked not in list_blocked:
                    list_blocked.append(to_blocked)
                    break
        for number in list_blocked:
            self.board[self.list_field[number]] = 'X'

    def set_square(self, square, command):
        self.board[square] = command

    def get_square(self, square):
        return(self.board[square])

    def iterator(self, player_colour):
            list_score = []
            counter = 0
            for height in self.list_height:
                if counter >= 3:
                    list_score.append(counter)
                counter = 0
                for width in self.list_width:
                    if self.board[height + width] == player_colour:
                        counter += 1
                    else:
                        if counter >= 3:
                            list_score.append(counter)
                        counter = 0
            if counter >= 3:
                list_score.append(counter)
            counter = 0
            for width in self.list_width:
                if counter >= 3:
                    list_score.append(counter)
                counter = 0
                for height in self.list_height:
                    if self.board[height + width] == player_colour:
                        counter += 1
                    else:
                        if counter >= 3:
                            list_score.append(counter)
                        counter = 0
            if counter >= 3:
                list_score.append(counter)

            return list_score

    def score_calculator(self, list_score):
        score = 0
        for element in list_score:
            if element == 3:
                score += 3
            elif element == 4:
                score += 10
            elif element == 5:
                score += 25
            elif element == 6:
                score += 56
            elif element == 7:
                score += 119
        return(score)

    def clear(self):
        os.system('cls')

    def printer(self):
        print('      1        2        3        4        5        6        7')
        for row in self.list_height:
            print('  ' + ' ________' * 7)
            print('  ' + '|        ' * 7 + '|')
            print(row, '|   {}   '.format(self.board[row + '1']), '|   {}   '.format(self.board[row + '2']),
                  '|   {}   '.format(self.board[row + '3']), '|   {}   '.format(self.board[row + '4']),
                  '|   {}   '.format(self.board[row + '5']), '|   {}   '.format(self.board[row + '6']),
                  '|   {}   '.format(self.board[row + '7']) + ' |')
            print('  ' + '|________' * 7 + '|')



    def pah_tum(self):
        self.field()
        self.blocked()
        self.clear()
        self.printer()

        self.undo_list = []
        number_turns = 49 - self.number_blocks
        for turns in range(number_turns):
            while True:
                if turns % 2 == 0:
                    colour = 'white'
                else:
                    colour = 'black'
                #  prints einfügen
                #  clear console
                square = input('\nPlease enter the tile you would like'
                               'to add a {} stone to\n'.format(colour)
                               )
                #  gatekeeper
                if square == 'undo':
                    turns -= 2
                    self.set_square(self.undo_list[-1], ' ')
                    self.undo_list.remove(self.undo_list[-1])
                    self.clear()
                    self.printer()
                    break
                elif square in self.list_field:
                    if self.board[square] == ' ':
                        if colour == 'white':
                            colour = 'W'
                        else:
                            colour = 'B'
                        self.set_square(square, colour)
                        self.undo_list.append(square)
                        self.clear()
                        self.printer()
                        break
                    else:
                        self.clear()
                        self.printer()
                        print('\nThe tile you have chosen is already occupied.\n'
                              'Please chose a differnt one.')
                else:
                        self.clear()
                        self.printer()
                        print('\nWe are sorry, but your input was invalid.\n'
                              'Please enter a valid combiniation of rows'
                              'and columns.')
        #  call iterator
        results_white = self.score_calculator(self.iterator('W'))
        results_black = self.score_calculator(self.iterator('B'))

        if results_white > results_black:
            print('The white player won the game with {} points!'.format(results_white))
        elif results_white < results_black:
            print('The black player won the game with {} points!'.format(results_black))
        else:
            print('Both players won the game!\n'
                  'Your scores are equal ({} points).'.format(results_white))

    def tk_pah_tum(self):
        root = tk.Tk()
        self.field()
        self.blocked()
        self.clear()
        self.printer()

        self.undo_list = []
        number_turns = 49 - self.number_blocks
        for turns in range(number_turns):
            while True:
                if turns % 2 == 0:
                    colour = 'white'
                else:
                    colour = 'black'
                #  prints einfügen
                #  clear console
                square = input('\nPlease enter the tile you would like'
                               'to add a {} stone to\n'.format(colour)
                               )
                #  gatekeeper
                if square == 'undo':
                    turns -= 2
                    self.set_square(self.undo_list[-1], ' ')
                    self.undo_list.remove(self.undo_list[-1])
                    self.clear()
                    self.printer()
                    break
                elif square in self.list_field:
                    if self.board[square] == ' ':
                        if colour == 'white':
                            colour = 'W'
                        else:
                            colour = 'B'
                        self.set_square(square, colour)
                        self.undo_list.append(square)
                        self.clear()
                        self.printer()
                        break
                    else:
                        self.clear()
                        self.printer()
                        print('\nThe tile you have chosen is already occupied.\n'
                              'Please chose a differnt one.')
                else:
                        self.clear()
                        self.printer()
                        print('\nWe are sorry, but your input was invalid.\n'
                              'Please enter a valid combiniation of rows'
                              'and columns.')
        #  call iterator
        results_white = self.score_calculator(self.iterator('W'))
        results_black = self.score_calculator(self.iterator('B'))

        if results_white > results_black:
            print('The white player won the game with {} points!'.format(results_white))
        elif results_white < results_black:
            print('The black player won the game with {} points!'.format(results_black))
        else:
            print('Both players won the game!\n'
                  'Your scores are equal ({} points).'.format(results_white))



def main():
    #random.seed(1.0)
    game = board_game()
    #game.field()
    #game.blocked()
    #for i in game.list_height:
     #   for j in game.list_width:
      #      if game.board[i + j] == 'X':
       #         pass
        #    else:
         #       if i in 'ACEG':
          #          game.board[i + j] = "W"
           #     else:
            #        game.board[i + j] = 'B'
    #results_white = game.score_calculator(game.iterator('W'))
    #results_black = game.score_calculator(game.iterator('B'))
    #game.printer()
    #print(results_white, results_black)
    game.pah_tum()

    while True:
        pass


if __name__ == '__main__':
    main()
