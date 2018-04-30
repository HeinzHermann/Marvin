__author__ = "4424114: Marvin Glaser"

# EPR1
# Exercise 2, 2.2
# Professor Ungerecht

user_data = input("--> ")

user_grade = user_data[:3]
user_sex = user_data[4:5]
user_height = user_data[6:9]
# slice input into relevant variables
# keep str type for checks

def gatekeeper(grade, sex, height):
    correct_input = True

    try:
        grade = float(grade)
        list_all_grades = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0,
                           5.0
                           ]
        if grade not in list_all_grades:
            correct_input = False
        # check if grade is an allowed grade
    except:
        correct_input = False   
    # gatekeeper for user grade (correct numbers and types)
    if correct_input == True:
        try:
            int(sex)
            correct_input = False
            # check if the input of sex is a number
        except:
            sex = sex.casefold()
            list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                             "j", "k", "l", "m", "n", "o", "p", "q", "r",
                             "s", "t", "u", "v", "w", "x", "y", "z"
                             ]
            if sex not in list_alphabet:
                correct_input = False  
    # gatekeeper for user sex (check if used characters are in alphabet)
    if correct_input == True:
        for character in height:
            try:
                int(character)
                if (int(height) < 100) or (int(height) > 300):
                    correct_input = False
            except:
                correct_input = False
                break
    # gatekeeper for user height
    output_list = []

    if correct_input == True:
        output_list.append(correct_input)
        output_list.append(float(user_grade))
        output_list.append(user_sex)
        output_list.append(int(user_height))
        return(output_list)
        # if all variables in correct format, output list with True at [0] and variables
    else:
        output_list.append(correct_input)
        return(output_list)
        # if at least one variable in incorrect format, output list with False at [0]
    
def unfair_tool(returned_list):
    if returned_list[0] == False:
        return("ERROR")
        # check if variables are correct or false
    else:
        bonus = 0
        if returned_list[2] == "w":
            bonus += 0.4
        # determine bonus for sex
        if returned_list[3] > 180:
            bonus -= ((returned_list[3] - 180) * 0.05)
        # determine penalty for height 
        if bonus > 0:
            bonus_multiplier = bonus // 0.3
        elif bonus < 0:
            bonus_multiplier = (bonus // -0.3) * (-1)
        # determine if in total a penalty or a bonus
        else:
            return(returned_list[1])
        # return orinal grade if no bonus or penalty
        list_all_grades2 = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0,
                           4.3, 4.7, 5.0
                           ]

        counter = 0
        for position in list_all_grades2:
            if position != returned_list[1]:
                counter += 1
            else:
                break
        # determine position of original grade in list of all grades
        postion_final_grade = int(counter - bonus_multiplier)
        # determine new postion (new grade with bonus/penalty) in list of all grades
        # and convert to integer, for list access
        if postion_final_grade < 0:
            postion_final_grade = 0
        elif postion_final_grade >= 10:
            postion_final_grade = 12
        # account for special cases. like grades < 1.0 and > 4.0
        return(list_all_grades2[postion_final_grade])

print(unfair_tool(gatekeeper(user_grade, user_sex, user_height)))