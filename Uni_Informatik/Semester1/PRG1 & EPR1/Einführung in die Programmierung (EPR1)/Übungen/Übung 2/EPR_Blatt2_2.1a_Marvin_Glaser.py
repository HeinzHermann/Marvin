__author__ = "4424114: Marvin Glaser"

# EPR1
# Exercise 2, 2.1 a)

sentence = input("--> ")

sentence = sentence.casefold()
# convert uppercase to lowercase letters and some special characters to ascii format
list_sentence = list(sentence)
# create list of characters of sentence
list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                 "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                 ]

pangramm_status = True

for letter_alphabet in list_alphabet:
    if letter_alphabet not in list_sentence:
        pangramm_status = False
        break
# if a letter of the defined alphabet list is missing in the sentence,
# pangramm status is set to false
if pangramm_status == False:
    print("Leider kein Pangramm.")
else:
    print("Juhu, ein Pangramm.")
# output of pangramm status
