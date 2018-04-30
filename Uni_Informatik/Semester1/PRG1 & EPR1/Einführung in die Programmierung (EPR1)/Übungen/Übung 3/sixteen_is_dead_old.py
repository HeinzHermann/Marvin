import random
import time

def converter(list_string):
    list_test = []
    for i in list_string[1::3]:
        list_test.append(int(i))

    return list_test

def roll_dice(number, faces, seed):
    dice_min = 1
    dice_max = faces
    #überprüfen falsche eingaben
    #seed nach float überprüfen
    if seed != None:
        random.seed(seed)

    list_player = []

    counter = 0
    while counter < number:
        list_player.append(random.randint(dice_min, dice_max))
        counter += 1

    return(str(list_player))


def sixteen_is_dead(players):
    number_rule = 1
    faces_rule = 6
    seed_rule = None
   #  three variables used to define game rules

    print("Hello Players, you are about to enter a world of pure fun!! \n"
        "16 IS DEAD!!! \n\nTo roll your dice, please press the \"Enter\" key \n"
        "To end your turn and let the next player play, please press the \"n\" key \n"
        "To start the game over from the beginneing, please press the \"r\" key \n"
        "To end the game and display the losers of this round, please press the \"e\" key \n\n"
        "Good luck and may the dice be with you!\n\n"
        )
    list_master = []

    looper = 0


    #while looper für jeden Spieler
    while looper < players:
        list_player = []
        #keyprombs einarbeiten

        condition = True

        while condition:


            if sum(list_player) > 15:
                #  Game over interface hinzufügen
                #break durch return ersetzen?
                looper = players
                list_master.append(list_player)
                break

            elif sum(list_player) == 10:
                #3sekunden wartezeit einbauen
                print("The sum of your rolls is a 10!\n"
                      "Please wait for three seconds.\nWe are about"
                      "to roll your die again!\n\n")
                time.sleep(3)
                key = ''
                #auf enter aufpassen
            elif sum(list_player) == 9:
                key = 'n'
                #auf n aufpassen
            else:
                print("Hey, Player", (looper + 1), " is playing right now. \n"
                      "The sum of your previous rolls is: \n\n-->", sum(list_player),
                      "<-- \n\nWhat would you like to do next? \nPlease press a key\n"
                      )
                key = input()


            if key == '':
                #if schleife überarbeiten
                roll = roll_dice(number_rule, faces_rule, seed_rule)
                roll = converter(roll)
                for i in roll:
                    list_player.append(i)


            elif key == 'n':
                list_master.append(list_player)
                condition = False
                looper += 1


            elif key == 'e':
                #e für end
                #remove output
                condition = False
                looper = players
                list_master.append(list_player)

            elif key == 'r':
                #r für restart
                condition = False
                looper = 0
                list_master = []

            else:
                print('The input you just gave us, did not work (;_;) \n'
                      'Please enter one of the allowed keys,\n \"Enter\" (roll dice) \n'
                      '\"n\" (next player)\n \"r\" (restart the game)\n or \"e\" (exit the game)'
                      )
                #  gui genauer definieren

    print("The game is finished!! \n\nThese are your results:")

    counter2 = 1
    for i in list_master:
        # change i to better variable
        print("Sum of dice rolls of Player ", counter2, ":", sum(i))
        counter2 += 1

    counter3 = 1
    list_losers = [15]
    list_loser_numbers = []

    for i in list_master:
        #print(i)
        #print(list_losers)
        #print("i is type", type(i), i)
        #print("list is type", type(list_losers), list_losers)
        # change i to beter
        if sum(i) > 15:
            #print(i, " > 15")
            list_losers = i
            list_loser_numbers = []
            list_loser_numbers.append(counter3)
            break

        elif sum(i) < sum(list_losers):
            #print(i, "<", sum(list_losers))
            list_losers = i
            list_loser_numbers = []
            list_loser_numbers.append(counter3)
            counter3 += 1
            #print("list_losers", list_losers)
            #print("list_losers_numbers", list_loser_numbers)

        elif sum(i) == sum(list_losers):
            #print(i, "==", sum(list_losers))
            list_loser_numbers.append(counter3)
            counter3 += 1
            #print("list_losers", list_losers)
            #print("list_losers_numbers", list_loser_numbers)

    loser_numbers_sliced = str(list_loser_numbers)
    loser_numbers_sliced = loser_numbers_sliced[1:-1]
    #print(type(list_loser_numbers))
    #print(type(loser_numbers_sliced))
    if len(list_loser_numbers) > 1:
        print("Players", loser_numbers_sliced,
              "lost the game with the number", sum(list_losers))
    else:
        print("Player", loser_numbers_sliced,
              "lost the game with the number", sum(list_losers))

sixteen_is_dead(5)
