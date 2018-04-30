import random
def roll_cheating_dice(number, faces, seed):
    dice_min = 1
    dice_max = faces + 1
    #überprüfen falsche eingaben
    #seed nach float überprüfen
    if seed != None:
        random.seed(seed)
    list_player = []

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
