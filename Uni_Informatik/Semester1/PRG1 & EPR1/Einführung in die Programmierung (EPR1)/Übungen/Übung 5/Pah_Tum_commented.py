"""this program simulates the game pah tum, bot in console and in tkinter.
one class contains all used functions, both for the console and tkinter.
in main function user can branch of to console or tkinter environment.
dictionary contains all 7x7 tiles of the game with respective tile states.
"""

#  random. used to randomly distribute blocked tiles on board
import random
#  os. used to clear console before each print for better user experience
import os
import tkinter as tk

__author__ = "6539575: Marc-Robin Muth, 4424114: Marvin Glaser"  #put your data here
__credits__ = "To Kim, because she was always there...kind of"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "mrmuth@outlook.com, marvin.glaser91@gmail.com"

class board_game():
    """class simulates all aspects of the game pah tum.
    contains all operations necessary to play in console or tkinter
    """
    def __init__(self):
        """defines dictionar that will keep track of states of all tiles"""
        self.board = {}

    def field(self):
        """function used to define a key and an initial state per game tile"""
        
        #  lists used to generate keys for each game tile (added to self.board)
        self.list_width = ['1', '2', '3', '4', '5', '6', '7']
        self.list_height = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.list_field = []

        # for loops iterate through entire playing field
        for element in self.list_height:
            for element2 in self.list_width:
                self.list_field.append(element + element2)

        #  iterates thogh all generated keys and adds them to dictionary
        for key in self.list_field:
            self.board[key] = ' '

    def blocked(self, user_input):
        """handles random blocking of game tiles"""
        
        #  list of blocked tiles to prevent 'double blocking' of one tile
        list_blocked = []
        self.number_blocks = int(user_input)
        
        #  randoms unique tile for each tile that has to be blocked
        for number in range(self.number_blocks):
            while True:
                to_blocked = random.randrange(0, 49)
                if to_blocked not in list_blocked:
                    list_blocked.append(to_blocked)
                    break
                
        #  blocks all chosen tiles in dictionary
        for number in list_blocked:
            self.board[self.list_field[number]] = 'X'

    def set_square(self, square, command):
        """setter function to change state of tile with key 'square' to
        'command'
        """
        self.board[square] = command

    def iterator(self, player_colour):
        """function used to check all rows and columns for lines of same
        color stones (used for score calculation). player_colour is either
        'white' ('w' in dictionary) or 'black ('b' in dictionary) and
        determines searched color.
        """
        list_score = []
        #  counter used to track how many same color stones are in sequence
        counter = 0
        #  for loops iterate through rows of field and check for scores
        for height in self.list_height:
            #  checks counter after every itaration (end of row)
            if counter >= 3:
                list_score.append(counter)
            counter = 0
            for width in self.list_width:
                #  counter +1 if tile has searched color
                if self.board[height + width] == player_colour:
                    counter += 1
                else:
                    #  if tile is not of the searched color, add sequences that
                    #  have a point score > 0 to list_score for evaluation
                    if counter >= 3:
                        list_score.append(counter)
                    # reset counter, because new stone sequence beginns
                    counter = 0
        #  after itaration is finished, check if final counter is > 3
        #  needed to add stone sequences that run till end of row/column
        if counter >= 3:
            list_score.append(counter)
        counter = 0
        #  for loops iterate through rows of field and check for scores
        for width in self.list_width:
            #  checks counter after every itaration (end of column)
            if counter >= 3:
                list_score.append(counter)
            counter = 0
            for height in self.list_height:
                #  counter +1 if tile has searched color
                if self.board[height + width] == player_colour:
                    counter += 1
                else:
                    #  if tile is not of the searched color, add sequences that
                    #  have a point score > 0 to list_score for evaluation
                    if counter >= 3:
                        list_score.append(counter)
                    # reset counter, because new stone sequence beginns
                    counter = 0
        #  after itaration is finished, check if final counter is > 3
        #  needed to add stone sequences that run till end of row/column
        if counter >= 3:
            list_score.append(counter)

        return list_score

    def score_calculator(self, list_score):
        """function takes score list, genarated by iterator() and calculates
        the score"""
        score = 0
        #  itarates throgh list of stone sequences > 3 and adds points to score
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
        """clears console window"""
        os.system('cls')

    def printer(self):
        """prints game board in console that changes based on tile states in
        self.board (dictionary with all tile states)"""
        
        #  prints column 'names' to help illustrate tile nomenclature
        print('      1        2        3        4        5        6        7')
        #  iterates through rows and generates user friendly tile UI
        #  for intuitive understanding of game state
        for row in self.list_height:
            print('  ' + ' ________' * 7)
            print('  ' + '|        ' * 7 + '|')
            print(row, '|   {}   '.format(self.board[row + '1']),
                  '|   {}   '.format(self.board[row + '2']),
                  '|   {}   '.format(self.board[row + '3']),
                  '|   {}   '.format(self.board[row + '4']),
                  '|   {}   '.format(self.board[row + '5']),
                  '|   {}   '.format(self.board[row + '6']),
                  '|   {}   '.format(self.board[row + '7']) + ' |'
                  )
            print('  ' + '|________' * 7 + '|')



    def pah_tum(self):
        """main function that simulates pah tum in console"""
        
        #  clear console before initial game status is printed
        self.clear()
        #  print initial game status
        self.printer()
        #  list of all turns, used to track previous turns for undo command
        self.undo_list = []
        
        #  calculates number of turns the game has before finishing
        number_turns = 49 - self.number_blocks
        #  enables user input while game is running
        for turns in range(number_turns):
            #  while loop in case user enters invalid command
            while True:
                # decides if white or black palyer is playing right now
                if turns % 2 == 0:
                    colour = 'white'
                else:
                    colour = 'black'
                
                #  input of user to set respective stone on tile
                print('Hello, this is Pah Tum.\n'
                      'You can put your stone on one of the tiles by typing\n'
                      'the \'name\' of the field [row + column]\n'
                      'Example: \'A1\', \'C5\', \'F6\', etc.\n'
                      'To undo one of your turns simply type \'undo\''
                      )
                square = input('\n{} players turn.\n'
                               'Please enter the tile you would like'
                               ' to add a stone to\n'.format(colour)
                               )
                
                #  gatekeeper to check for valid input
                if square == 'undo':
                    #  calls for undo function and sets turns -2
                    #  since +1 at beginning of turn
                    turns -= 2
                    self.set_square(self.undo_list[-1], ' ')
                    self.undo_list.remove(self.undo_list[-1])
                    self.clear()
                    self.printer()
                    break
                elif square in self.list_field:
                    #  if input was correct, check if tile is already occupied
                    if self.board[square] == ' ':
                        #  valid input for empty field
                        if colour == 'white':
                            colour = 'W'
                        else:
                            colour = 'B'
                        #  change color in dictionary
                        self.set_square(square, colour)
                        #  add valid command to list of pased turns
                        self.undo_list.append(square)
                        #  clear console and print new board in console
                        self.clear()
                        self.printer()
                        break
                    else:
                        #  valid input but occupied field, repead user input
                        #  and print new field for aestehtics
                        self.clear()
                        self.printer()
                        print('\nThe tile you have chosen is already occupied.\n'
                              'Please chose a differnt one.')
                else:
                    #  invalid input, clear console, reprint field and ask
                    #  for new input
                    self.clear()
                    self.printer()
                    print('\nWe are sorry, but your input was invalid.\n'
                          'Please enter a valid combiniation of rows'
                          'and columns.')
        
        #  once game is finished, calculate score for each player
        results_white = self.score_calculator(self.iterator('W'))
        results_black = self.score_calculator(self.iterator('B'))

        #  compare score of each player and declare winner
        if results_white > results_black:
            print('The white player won the game with {} points!'.format(results_white))
        elif results_white < results_black:
            print('The black player won the game with {} points!'.format(results_black))
        else:
            print('Both players won the game!\n'
                  'Your scores are equal ({} points).'.format(results_white)
                  )
    
    def bot(self):
        counter = 1
        counter2 = 0
        bot_number = 0

        for height in range(7):
            for width in range(7):
    
                if self.board[self.list_height[height] + self.list_width[width]] == 'B':
                    while True:
                        if width + counter < 7:
                            if self.board[self.list_height[height] + self.list_width[width + counter]] == ' ':
                                self.board[self.list_height[height] + self.list_width[width + counter]] = 'B'
                                return
                        elif width - counter >= 0:
                            if self.board[self.list_height[height] + self.list_width[width + counter]] == ' ':
                                self.board[self.list_height[height] + self.list_width[width + counter]] = 'B'
                                return
                            else:
                                counter += 1
                        else:
                            counter = 1
                            break
    
                    while True:
                        if height + counter < 7:
                            if self.board[self.list_height[height + counter] + self.list_width[width]] == ' ':
                                self.board[self.list_height[height + counter] + self.list_width[width]] = 'B'
                                return
                        elif height - counter >= 0:
                            if self.board[self.list_height[height - counter] + self.list_width[width]] == ' ':
                                self.board[self.list_height[height - counter] + self.list_width[width]] = 'B'
                                return
                            else:
                                counter += 1
                        else:
                            counter = 1
                            break
    
    
        for height in range(7):
            if counter2 > bot_number:
                bot_number = counter2
                bot_square = (self.list_height[height] + self.list_width[width])
            counter2 = 0
            for width in range(7):
                if self.board[self.list_height[height] + self.list_width[width]] == ' ':
                    counter2 += 1
                else:
                    if counter2 > bot_number:
                        bot_number = counter2
                        middle = counter2 // 2
                        bot_square = (self.list_height[height] + self.list_width[width - middle])
                    counter2 = 0
    
        for width in range(7):
            if counter2 > bot_number:
                bot_number = counter2
                bot_square = (self.list_height[height] + self.list_width[width])
            counter2 = 0
            for height in range(7):
                if self.board[self.list_height[height] + self.list_width[width]] == ' ':
                    counter2 += 1
                else:
                    if counter2 > bot_number:
                        bot_number = counter2
                        middle = counter2 // 2
                        bot_square = (self.list_height[height - middle] + self.list_width[width])
                    counter2 = 0
    
            if counter2 > bot_number:
                bot_number = (counter2)
                bot_square = (self.list_height[height] + self.list_width[width])
            counter2 = 0
    
        self.board[bot_square] = 'B'
        
    def pah_tum_bot(self):
        """main function that simulates pah tum in console"""
        
        #  clear console before initial game status is printed
        self.clear()
        #  print initial game status
        self.printer()
        #  list of all turns, used to track previous turns for undo command
        self.undo_list = []
        
        #  calculates number of turns the game has before finishing
        number_turns = 49 - self.number_blocks
        #  enables user input while game is running
        for turns in range(number_turns):
            #  while loop in case user enters invalid command
            while True:
                # decides if white or black palyer is playing right now
                if turns % 2 == 0:
                    colour = 'white'
                    print('number of turns', turns)
                    print('Hello, this is Pah Tum.\n'
                          'You can put your stone on one of the tiles by typing\n'
                          'the \'name\' of the field [row + column]\n'
                          'Example: \'A1\', \'C5\', \'F6\', etc.\n'
                          'To undo one of your turns simply type \'undo\''
                          )
                    square = input('\n{} players turn.\n'
                                   'Please enter the tile you would like'
                                   ' to add a stone to\n'.format(colour)
                                   )
                
                    #  gatekeeper to check for valid input
                    if square == 'undo':
                        #  calls for undo function and sets turns -2
                        #  since +1 at beginning of turn
                        turns -= 2
                        self.set_square(self.undo_list[-1], ' ')
                        self.undo_list.remove(self.undo_list[-1])
                        self.clear()
                        self.printer()
                        break
                    elif square in self.list_field:
                        #  if input was correct, check if tile is already occupied
                        if self.board[square] == ' ':
                            #  valid input for empty field
                            colour = 'W'
                            #  change color in dictionary
                            self.set_square(square, colour)
                            #  add valid command to list of pased turns
                            self.undo_list.append(square)
                            #  clear console and print new board in console
                            self.clear()
                            self.printer()
                            break
                        else:
                            #  valid input but occupied field, repead user input
                            #  and print new field for aestehtics
                            self.clear()
                            self.printer()
                            print('\nThe tile you have chosen is already occupied.\n'
                                  'Please chose a differnt one.')
                    else:
                        #  invalid input, clear console, reprint field and ask
                        #  for new input
                        self.clear()
                        self.printer()
                        print('\nWe are sorry, but your input was invalid.\n'
                              'Please enter a valid combiniation of rows'
                              'and columns.')
        
                else:
                    self.bot()
                    self.clear()
                    self.printer()
                    print('bot turn', turns)
                    break
                    
                        
        #  once game is finished, calculate score for each player
        results_white = self.score_calculator(self.iterator('W'))
        results_black = self.score_calculator(self.iterator('B'))

        #  compare score of each player and declare winner
        if results_white > results_black:
            print('The white player won the game with {} points!'.format(results_white))
        elif results_white < results_black:
            print('The black player won the game with {} points!'.format(results_black))
        else:
            print('Both players won the game!\n'
                  'Your scores are equal ({} points).'.format(results_white)
                  )



    def final_calc(self):
        """calculates results for both players and changes text output in
        tkinter label"""
        #  calculates scores of both players
        results_white = self.score_calculator(self.iterator('W'))
        results_black = self.score_calculator(self.iterator('B'))

        #  compares scores and changes text of output label
        if results_white > results_black:
            self.winner.set('The white player won the game with {} points!'.format(results_white))
        elif results_white < results_black:
            self.winner.set('The black player won the game with {} points!'.format(results_black))
        else:
            self.winner.set('Both players won the game!\nYour scores are equal ({} points).'.format(results_white))

    def undo(self):
        """undo function for tkinter implementation
        undoes both changes to tkinter buttons of board tiles and dictionary
        """
        
        #  if first turn (no changes can be undone), button does nothing
        if self.undo_list == []:
            pass
        else:
            #  change color of button back to neutral color
            self.dic_butt[self.undo_list[-1]].config(bg = 'gold3', state = tk.NORMAL)
            tupel_carrier = self.undo_list[-1]
            #  undo changes in tile dictionary
            self.board[self.list_height[tupel_carrier[0]],str(tupel_carrier[1] + 1)] = ' '
            #  remove last turn from 'passed turnes' list
            self.undo_list.remove(self.undo_list[-1])
            #  turn counter back one turn
            self.counter -= 1

    def click(self, row, column):
        """function executed on click of a button
        changes button to player color and disables button
        adds action to list of passed turns
        calls for score calculation if game is finished
        """
        
        #  determines player color for this turn
        if self.counter % 2 == 0:
            colour = 'white'
            self.board[self.list_height[row] + str(column + 1)] = 'W'
        else:
            colour = 'black'
            self.board[self.list_height[row] + str(column + 1)] = 'B'

        #  changges button color and disables button
        self.dic_butt[row, column].config(bg = colour)
        self.dic_butt[row, column].config(state = tk.DISABLED)
        #  increases turn by 1
        self.counter += 1
        #  adds turn to list of passed turns
        self.undo_list.append((row, column))
        #  if game is finished, calculate game results
        if self.counter == 49 - self.number_blocks:
            self.final_calc()

    def butt_block(self, row, column):
        """checks if entered tile is blocked and adjusts buttons
        if tile is blocked, changes button color and disables button
        """
        if self.board[self.list_height[row] + str(column + 1)] == 'X':
            self.dic_butt[row, column].config(bg = 'light slate gray')
            self.dic_butt[row, column].config(state = tk.DISABLED)

    def tk_pah_tum(self):
        """main function that runs pah tum in tkinter environment
        handles buttons and lables"""
        root = tk.Tk()
        root.title('Pah Tum')
        #  counts number of turns till game is finished
        self.counter = 0

        #  creates new dictionary that stores all possible (one per tile)
        #  haha, dic(k)butt
        self.dic_butt = {}
        #  iterates though all possible fields and creates one button per tile
        for row in range(7):
            for column in range(7):
                self.dic_butt[row, column] = tk.Button(root, height = 5, width = 10,
                                                       bg = 'gold3',
                                                       command = lambda row = row,
                                                       column = column : self.click(row, column)
                                                       )
                self.dic_butt[row, column].grid(row = row, column = column)
        
        #  generates textvariable that changes lable next to playing field
        self.winner = tk.StringVar()
        self.winner.set('To put your stone on a tile, just click on it.\n'
                        'You can only put stones on the golden tiles.\n'
                        'Click the \'Undo\' button, to undo the last turn.'
                        )
        
        #  generates lable that displays basic instructions and outputs
        #  game results
        winner = tk.Label(root, textvariable = self.winner, width = 40, font = ('times', 16))
        winner.grid(row = 2, rowspan = 2, column = 9)

        #  generates static lables that help to identify tile nomenclature
        #  technically not needed but nice aesthetic and easier to understand
        tk.Label(root, text = '1').grid(row = 7, column = 0)
        tk.Label(root, text = '2').grid(row = 7, column = 1)
        tk.Label(root, text = '3').grid(row = 7, column = 2)
        tk.Label(root, text = '4').grid(row = 7, column = 3)
        tk.Label(root, text = '5').grid(row = 7, column = 4)
        tk.Label(root, text = '6').grid(row = 7, column = 5)
        tk.Label(root, text = '7').grid(row = 7, column = 6)

        tk.Label(root, text = 'A').grid(row = 0, column = 7)
        tk.Label(root, text = 'B').grid(row = 1, column = 7)
        tk.Label(root, text = 'C').grid(row = 2, column = 7)
        tk.Label(root, text = 'D').grid(row = 3, column = 7)
        tk.Label(root, text = 'E').grid(row = 4, column = 7)
        tk.Label(root, text = 'F').grid(row = 5, column = 7)
        tk.Label(root, text = 'G').grid(row = 6, column = 7)

        #  creates undo button
        undo_button = tk.Button(root, text = 'UNDO', bg = 'beige',
                                width = 20, height = 5, command = self.undo)
        undo_button.grid(row = 4, column = 9)

        #  blocks number of fields at the beginning of the game
        for row in range(7):
            for column in range(7):
                self.butt_block(row, column)
        
        #  list that tracks performed turns (needed for undo function)
        self.undo_list = []

        root.mainloop()




def main():
    """main function that is executed if program is started"""
    random.seed(1.0)
    #  defines 'game' as an object of the board_game class
    game = board_game()
    
    print('This game is called Pah Tum and it is played on a'
          '7x7 tile board.\nAt the beginning of the game,'
          'an odd number of tiles between 5 and 13 is'
          'blocked.\n'
          )
    
    #  while loop till user enters valid input
    while True:
        input_blocks = input('Please enter the number of tiles you'
                             'would like to block:\n(The input must be an odd'
                             'integer between 5 and 13)\n'
                             )
        #  if input is valid, create dictionary for board tiles and block
        #  chosen number of tiles randomly
        if input_blocks in ['5', '7', '9', '11', '13']:
            game.field()
            game.blocked(input_blocks)
            break
        
        #  if input is even, not odd, give user feedback and ask for new input
        elif input_blocks in ['6', '8', '10', '12']:
            print('\nOops, it seems like you choose an even number between 5'
                  'and 13.\nUnfortunately the games rules dont allow that.'
                  )
        #  if input is compleatly invalid, ask for new input
        else:
            print('\nThis is unfortunate, but your input seems to be invalid.')

    #  while loop till user enters valid input
    while True:
        input_game = input('\nWould you like to play your game in the console'
                           '\nor open a separate window?\n'
                           'To open a separate window, just type: \'TK\'\n'
                           'Otherwiese, please type \'C\'.\n'
                           )
        if input_game == 'TK':
            game.tk_pah_tum()
            break
        elif input_game == 'C':
            game.pah_tum()
            break
        else:
            print('\nUnfortunately your input was invalid.\n'
                  'Please try again\n')

    while True:
        pass


if __name__ == '__main__':
    main()
