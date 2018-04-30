"""This is a game called SIXTEEN IS DEAD"""

import random
import time
import math
import os

__author__ = "4424114: Marvin Glaser"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "marvin.glaser91@gmail.com" 


def roll_dice(number=3, faces=6, seed=None):
    """This function rolls a dice."""
    try:
        random.seed(seed)
        assert faces >= 1
        assert number >= 0
    except TypeError:
        print("Seed must be float")
    except AssertionError:
        print("Faces and number must be non-negative")
    dice_string = ''
    try:
        for i in range(number):
            dice_string += str(random.randint(1, faces)) + ','
    except TypeError:
        print("Number, faces must be integral.")
    return dice_string[0:-1]



def roll_cheating_dice():
    """This function rolls a dice with a higher possibility of getting the number three."""
    probabilities = [1/7, 1/7, 2/7, 1/7, 1/7, 1/7]
    for p in probabilities:
        assert p >= 0, "Probabilities must be non-negative."
    assert math.isclose(sum(probabilities), 1), "Probabilities must be normed"
    random_number = random.uniform(0, 1)
    for i in range(1, len(probabilities) + 1):
        if sum(probabilities[0:i]) >= random_number:
            break
    return str(i)


def sixteen_is_dead(players):
    """This is the main function of the game sixteen is dead."""
    os.system('CLS')
    print("Welcome to \"Studentenpasch\"")
    print("____________________________\n"
        "")
    print("This is a fun game for {} players".format(players))
    rules = ("\n"
    "Every player has three turns and rolls three dice.\n"
    "In each of their turns players may reroll up to three dice.\n"
    "Players may choose not to reroll one or more dice. These dice\n"
    "  must not be rerolled in the upcoming turns.\n"
    "The next player may start to roll, once the current player has\n"
    "  either rerolled three times or the current player chooses not\n"
    "  to reroll.\n"
    "The game ends once all players are finished rerolling.\n"
    "Once the game is finished, the players will compare their respecitve\n"
    "  scores. The player(s) with the lowest score lose(es).\n"
    "A players score is calculated by comparing the values of\n"
    "  their dice with the table shown below and summing up their\n"
    "  respective score values.\n\n"
    "Score table:\n"
    "6 = 60 Points\n5 = 5 Points\n4 = 4 Points\n3 = 3 Points\n2 = 2 Points\n"
    "1 = 100 Points"
    )
    print("Your options:\n"
          "choose not to roll any dice: <Enter> (next players turn)\n"
          "enter the number of the die(dice) you would like to keep\n"
          "  - the numbers of the dice are 1, 2 and 3 (presented to you\n"
          "      from left to right)\n"
          "  - enter the numbers of the dice you would like to kee\n"
          "  - separate the numbers of the dice with a blank space\n"
          "      (commata, dots or other symbols will not be accepted\n"
          "      by the program\n"
          "New game:     type \"new\"\n"
          "Rules:        type \"r\"\n"
          "Quit:         type \"exit\""
          )
    #prematurely_lost = False
    player_sums = []
    #try:
    for i in range(1, players+1):
            #if prematurely_lost:
            #    break
            #print("Player {}, your turn!".format(i))
            #summed_throws = 0
            #while summed_throws < 16:
            #    if summed_throws != 10:
            #        print("Player {}, you already summed up to {}".format(
            #            i, summed_throws))
            #while True:
        rolled_dice = roll_dice().split(',')
        #  generates a list with three randomly determined dice rolls
        dice_list = []
        for strings in rolled_dice:
            #  converts strings of rolled_dice to integers
            dice_list.append(int(strings))
        rollable_dice = [1, 2, 3]
        counter = 1
        #  counter used to track player turns
        while True:
            point_list = []
            for dice in dice_list:
                #  checks player score at the beginning of every turn
                if dice == 1:
                    point_list.append(100)
                elif dice == 6:
                    point_list.append(50)
                else:
                    point_list.append(dice)
                
            if counter >= 3:
                #  ends player round, when three turns are performed
                #  and prints player score for feedback
                player_sums.append(sum(point_list))
                print("\nPlayer {}, your turn is over.".format(i), "\nYou "
                          "reachted a total of", sum(point_list), "points")
                break
            
            #  prints information for the player
            print("\n\nHey player {}, the result of your dice rolls is: ".format(i),
                  str(dice_list)[1:-1], "\nYour current score is", sum(point_list),
                  "\nYou can still have", (3 - counter), "turn(s) and can roll",
                  "dice", str(rollable_dice)[1:-1]
                  )
            
            condition = True
            while condition:
                #  checks if user input is valid or if new input is needed
                condition = False
                users_choice = input("\nWhat would you like to do next?\n")
                if users_choice not in ['', 'r', 'exit', 'new']:
                    #  checks for commands outside of game turns
                    users_choice = users_choice.split(" ")
                    #  creates list from player input
                    for order in users_choice:
                        #  checks if elements of list are convertable to
                        #  integers and if they are proper commands
                        try:
                            if int(order) not in rollable_dice:
                                print("OH NOOO...apparently your input had an "
                                      "error.\nPlease reenter the numbers of the "
                                      "dice you would like to reroll.\n"
                                      )
                                condition = True
                                break
                        
                        except:
                            print("OH NOOO...apparently your input had an "
                                  "error.\nPlease reenter the numbers of the "
                                  "dice you would like to reroll.\n"
                                  )
                            condition = True
                            break
                
           
            if users_choice == '':
                #  player wants to keep all dice --> prints results and next player
                player_sums.append(sum(point_list))
                print("The final score of Player {} is:".format(i),
                      sum(point_list)
                      )
                break
            elif users_choice == 'r':
                #  prints game rules
                print("Here are the rules of the game.\n")
                print(rules)
            elif users_choice == 'exit':
                #  finishes game in console
                exit()
            elif users_choice == 'new':
                #  clears current console and starts a new game
                #  (while loop) in __main__
                os.system('CLS')
                return
            else:
                for to_remove in [1, 2, 3]:
                    #  checks which dice the user wants to protect from reroll
                    #  removes "safe dice" from rollable list and randoms
                    #  new values for other dice
                    if (str(to_remove) not in users_choice
                        and to_remove in rollable_dice
                        ):
                        rollable_dice.remove(to_remove)
                        for to_roll in rollable_dice:
                            dice_list[(to_roll - 1)] = random.randrange(1,7)
            counter += 1

                #else:
                #    print("Invalid input: Please try again.")
                #if users_choice == 'n':
                #    player_sums.append(summed_throws)
                #    break
                #if summed_throws >= 16:
                #    print("Player {}, you lost. Haha".format(i))
                #    break
                #    prematurely_lost = True
                #    break
                #if summed_throws == 9:
                #    print("You hit 9, next players turn")
                #    player_sums.append(summed_throws)
                #    break
                #if summed_throws == 10:
                #    print(
                #        "You hit 10. I will throw the dice in 3 seconds automatically.")
                #    time.sleep(3)
                #    continue
    #except TypeError:
    #   print("Players must be integer.")
    #   return

    min_throws = min(player_sums)
    losers = ''
    for i in range(1, players+1):
        #  adds losers to loser string
        if player_sums[i-1] == min_throws:
            losers += str(i) + ', '
    losers = losers[0:-2]
    #  prints all losers
    print("\n\n\nplayer{} {} you are the loser{}, haha! Your number {} is "
          "so tiny!\n\n".format((len(losers) != 1) * 's', losers, (len(losers)
          != 1) * 's', min_throws)
          )
    
def main():
    """This function starts the main function"""
    while True: 
        #  gatekeeper, asks for input till player number valid
        try:
            players = int(input("Please enter an integral number of players"
                            "that is greater then one\n"
                            "Please note: If a floating numbers is used as"
                            "an input, it will be rounded down\n"))

            if players >= 2:
                break
            else:
                print("number of players must be greater or equal to 2\n")
        except ValueError:
            print("The input must be an integer\n")
                    
    sixteen_is_dead(players)

    
if __name__ == '__main__':
    while True:
        main()
