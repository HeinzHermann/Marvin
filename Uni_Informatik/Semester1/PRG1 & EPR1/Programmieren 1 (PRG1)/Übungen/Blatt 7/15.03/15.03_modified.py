"""This is a game called SIXTEEN IS DEAD"""

import random
import time
import math
import os

__author__ = "4424114: Marvin Glaser"  #put your data here
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
    print("Welcome to SIXTEEN IS DEAD!")
    print("____________________________\n"
        "")
    print("This is a fun game for {} players".format(players))
    rules = ("\n"
    "Every player rolls three dice during their turn.\n"
    ".\n"
    "In the end the dice throws are summed.\n"
    "The goal is to come as close to 16 as possible.\n"
    "But beware: If you hit 16 or above, you lose.\n"
    "There are special rules: \n"
    "If hitting 9, you must not throw again,\n"
    "if hitting 10, you have to throw again.\n"
    "If all players are below 16 after their part, the one with the\n"
    "smallest number loses.\n"
    "")
    print("Your options:\n"
    	"roll the dice: <Enter>\n"
        "new game: new\n"
        "Next player: n\n"
        "Rules: r\n"
        "Quit: exit")
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
        dice_list = []
        for strings in rolled_dice:
            dice_list.append(int(strings))
        rollable_dice = [1, 2, 3]
        while True:
            print("\n\nHey player {}, the result of your dice rolls is: ".format(i),
                  str(dice_list)[1:-1], "\nCurrently the sum of your dice"
                  "rolls is: ", sum(dice_list)
                  )
            users_choice = input("\nWhat would you like to do next?\n")
            if users_choice == '':
                player_sums.append(sum(dice_list))
                print("The final result of Player {} is:".format(i),
                      sum(dice_list), "\nWith the numbers:", str(dice_list)[1:-1]
                      )
                break
            elif users_choice == 'r':
                print("Here are the rules of the game.\n")
                print(rules)
            elif users_choice == 'exit':
                exit()
            elif users_choice == 'new':
                os.system('CLS')
            else:
                users_choice = users_choice.split(" ")
                for order in users_choice:
                    try:
                        if int(order) not in rollable_dice:
                            print("OH NOOO...apparently your input had an "
                                  "error.\nPlease reenter the numbers of the "
                                  "dice you would like to reroll.\n\n"
                                  )
                            break
                        else:
                            dice_list[(int(order) - 1)] = random.randrange(1,7)
                            rollable_dice.remove(int(order))
                    except:
                        print("OH NOOO...apparently your input had an "
                              "error.\nPlease reenter the numbers of the "
                              "dice you would like to reroll.\n\n"
                              )
                        break
            
            if rollable_dice == []:
                player_sums.append(sum(dice_list))
                print("The final result of Player {} is:".format(i),
                      sum(dice_list), "\nWith the numbers:", str(dice_list)[1:-1]
                      )
                break

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
        if player_sums[i-1] == min_throws:
            losers += str(i) + ', '
    losers = losers[0:-2]
    print("player{} {} you are the loser{}, haha! Your number {} is so tiny!".format(
        (len(losers) != 1) * 's', losers, (len(losers) != 1) * 's', min_throws))
    
def main():
    """This function starts the main function"""
    while True:        
        try:
            players = int(input("Give me the number of the players, please: "))
            if players >= 2:
                break
        except ValueError:
            print("It must be an integer")

    sixteen_is_dead(players)
    #print(roll_dice().split(','))
    #print(type(roll_dice()))
    
if __name__ == '__main__':
    #while True:
     main()
