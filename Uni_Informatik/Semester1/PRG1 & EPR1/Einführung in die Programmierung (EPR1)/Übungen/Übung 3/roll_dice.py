import random
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
