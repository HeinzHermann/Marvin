"""This program was written for the course EPR1, exercise 3
The following code contains the roll_dice, the
roll_cheating dice, a conversion and the sixteen_is_dead
function.
"""

import random
import time
import msvcrt


__author__ = "4424114: Marvin Glaser, 6539575: Marc-Robin Muth"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out"
__email__ = "marvin.glaser91@gmail.com, mrmuth@outlook.com"


def converter(list_string):
    """converts list as string type to list and returns list"""
    list_converted = []
    for i in list_string[1::3]:
        list_converted.append(int(i))

    return list_converted


def roll_dice(number, faces, seed):
    """function rolls die without cheating and returns result
    number variable regulates the number of rolled dice
    faces variable regulates number of die faces
    seed is a float used to make random numbers reproducible
    """
    dice_min = 1
    dice_max = faces

    #  series of if loops to check for correct input type of variables
    if type(number) != type(1):
        print("ERROR!!!\n\"number\" value for roll_dice is not an integer!")
    if type(faces) != type(1):
        print("ERROR!!!\n\"faces\" value for roll_dice is not an integer!")
    if type(seed) != type(1.0):
        if seed != None:
            print("ERROR!!!\n\"seed\" value for roll_dice is not a flaoting number!")

    if seed != None:
        random.seed(seed)

    #  create empty list that can be filled with player numbers
    #  list will be returned at end of function
    list_player = []

    #  introduction of counter to regulate number of dice rolls
    counter = 0
    while counter < number:
        list_player.append(random.randint(dice_min, dice_max))
        counter += 1

    return(str(list_player))


def roll_cheating_dice(number, faces, seed):
    """functions rolls cheating die, with increased chance to roll 3
    number variable regulates the number of rolled dice
    faces variable regulates number of die faces
    seed is a float used to make random numbers reproducible
    """

    dice_min = 1
    #  additional face introduced to increase chance to roll 3
    dice_max = faces + 1


    #  series of if loops to check for correct input type of variables
    if type(number) != type(1):
        print("ERROR!!!\n\"number\" value for roll_dice is not an integer!")
    if type(faces) != type(1):
        print("ERROR!!!\n\"faces\" value for roll_dice is not an integer!")
    if type(seed) != type(1.0):
        if seed != None:
            print("ERROR!!!\n\"seed\" value for roll_dice is not a flaoting number!")

    if seed != None:
        random.seed(seed)

    #  create empty list that can be filled with player numbers
    #  list will be returned at end of function
    list_player = []

    #  introduction of counter to regulate number of dice rolls
    counter = 0
    while counter < number:
        temporary = random.randint(dice_min, dice_max)
        #print(temporary)
        if temporary == 7:
            list_player.append(3)
        else:
            list_player.append(temporary)
        counter += 1

    return(str(list_player))


def sixteen_is_dead(players):
    """main program of the code, starts the game 16 is dead
    player variable regulates the maximum number of players.
    """

    #  three variables used to define game rules
    number_rule = 1
    faces_rule = 6
    seed_rule = None

    #  player itroduction to all possible commands
    print("Hello Players, you are about to enter a world of pure fun!! \n"
        "16 IS DEAD!!! \n\nTo roll your dice, please press the \"Enter\" key \n"
        "To end your turn and let the next player play, please press the \"n\" key \n"
        "To...not play fair...please press the \"c\" key\n"
        "To start the game over from the beginneing, please press the \"r\" key \n"
        "To end the game and display the losers of this round, please press the \"e\" key \n\n"
        "Good luck and may the dice be with you!\n\n"
        )

    #  list_master variable to concentrate roll results of all players
    list_master = []

    #  introduction of looper variable to track end of game/player number
    looper = 0
    while looper < players:

        #  introduction of list_player to safe dice rolls of every player
        list_player = []

        condition = True
        condition2 = True
        
        while condition:
            #  if condtion2 avoid double print for (^,´,`)
            if condition2:
                if sum(list_player) > 15:
                    #  one player lost, game ends and results are shown
                    looper = players
                    list_master.append(list_player)
                    break
                elif sum(list_player) == 10:
                    #  forces additional roll of same player
                    print("The sum of your rolls is 10!\n"
                          "Please wait for three seconds.\nWe are about"
                          "to roll your die again!\n\n")
                    time.sleep(3)
                    #  13 = unicode for enter key
                    key = 13
                elif sum(list_player) == 9:
                    #  forces turn of next player
                    print("The sum of your roll is 9!\n"
                          "Sorry, but your turn is finished")
                    key = ord("n")
                else:
                    #  display of sum + getch() of key input
                    print("Hey, Player", (looper + 1), " is playing right now. \n"
                          "The sum of your previous rolls is: \n\n-->", sum(list_player),
                          "<-- \n\nWhat would you like to do next? \nPlease press a key\n"
                          )
                    key = ord(msvcrt.getch())
            else:
                key = ord(msvcrt.getch())

            condition2 = True
            
            #  executes player commands
            if key == 13:
                roll = roll_dice(number_rule, faces_rule, seed_rule)
                roll = converter(roll)
                for i in roll:
                    list_player.append(i)
            elif key == ord("c"):
                roll = roll_cheating_dice(number_rule, faces_rule, seed_rule)
                roll = converter(roll)
                for i in roll:
                    list_player.append(i)
            elif key == ord("n"):
                list_master.append(list_player)
                condition = False
                looper += 1
            elif key == ord("e"):
                condition = False
                looper = players
                list_master.append(list_player)
            elif key == ord("ê"):
                condition = False
                looper = players
                list_master.append(list_player)
            elif key == ord("é"):
                condition = False
                looper = players
                list_master.append(list_player)
            elif key == ord("è"):
                condition = False
                looper = players
                list_master.append(list_player)
            elif key == ord('r'):
                condition = False
                looper = 0
                list_master = []
            elif key == ord("^"):
                condition2 = False
            elif key == ord("´"):
                condition2 = False
            elif key == ord("`"):
                condition2 = False


            else:
                print('The input you just gave us, did not work (;_;) \n'
                      'Please enter one of the allowed keys,\n\"Enter\" (roll dice) \n'
                      '\"c\" (not play fair) \n\"n\" (next player)\n\"r\" (restart the game)'
                      '\n\"e\" (exit the game)\n'
                      )

    print("The game is finished!! \n\nThese are your results:")

    #  counter2 used to display correct player number with sum of rolls
    counter2 = 1
    for i in list_master:
        # change i to better variable
        print("Sum of dice rolls of Player ", counter2, ":", sum(i))
        counter2 += 1

    #  counter3 used to display correct player number
    counter3 = 1
    list_losers = [15]
    list_loser_numbers = []

    for i in list_master:
        if sum(i) > 15:
            list_losers = i
            list_loser_numbers = []
            list_loser_numbers.append(counter3)
            break
        elif sum(i) < sum(list_losers):
            list_losers = i
            list_loser_numbers = []
            list_loser_numbers.append(counter3)
            counter3 += 1
        elif sum(i) == sum(list_losers):
            list_loser_numbers.append(counter3)
            counter3 += 1

    #  slice player numbers in case of multible losers
    loser_numbers_sliced = str(list_loser_numbers)
    loser_numbers_sliced = loser_numbers_sliced[1:-1]
    if len(list_loser_numbers) > 1:
        print("Players", loser_numbers_sliced,
              "lost the game with the number", sum(list_losers))
    else:
        print("Player", loser_numbers_sliced,
              "lost the game with the number", sum(list_losers))


def main():
    """Main body of program, executes game and ends program"""


    sixteen_is_dead(5)

    #  continue program in case of self closing command terminal
    while True:
        print("\n\nPress any key to end the program")
        key2 = msvcrt.getch()
        if True:
            break

if __name__ == '__main__':
    main()

