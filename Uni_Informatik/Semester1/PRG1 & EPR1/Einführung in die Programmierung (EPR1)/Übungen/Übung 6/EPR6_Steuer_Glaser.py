__author__ = "6164434: Julius Steuer, 4424114: Marvin Glaser"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "juliussteuer87@gmail.com, marvin.glaser91@gmail.com"

import os   # to join paths and change working directory
import json # json module, create json files


class EvalFile:
    """ class to read a unicode file and calculate some statistics"""

    def read_file(self):
        """ class method to read a file """

        # create file path, from program path
        self.path_in = os.path.join(os.path.dirname(__file__),
                                    "files",
                                    self.file_in)

        # try to open file in utf-8, utf-16, utf-32, else raise error and exit
        try:
            with open(self.path_in, "r", encoding="utf-8") as infile:
                self.file_string = infile.read()
        except:

            try:
                with open(self.path_in, "r", encoding="utf-16") as infile:
                    self.file_string = infile.read()
            except:

                try:
                    with open(self.path_in, "r", encoding="utf-32") as infile:
                        self.file_string = infile.read()
                except:
                    error_message = """ 
                                Improper encoding: Use utf-8, utf-16 or utf-32
                                Change encoding and then restart the program !
                             """
                    print(error_message)
                    exit()


    def write_json_file(self):
        """ class method to write statistical data into a JSON file"""

        self.path_out = os.path.join(os.path.dirname(__file__),"json")

        # check if directory 'json' exists in working current directory,
        # else create such directory
        if not os.path.exists(self.path_out):
            os.makedirs(self.path_out)

        # create new filename
        #print(self.file_in)
        dot_idx = self.file_in.find(".")
        #print(dot_idx)
        self.file_out = self.file_in[:dot_idx] + ".json"
        #print(self.file_out)

        path_reset = os.path.dirname(__file__)

        # change dir to "json" dir to create writeable user file
        os.chdir(self.path_out)

        with open(self.file_out, 'w') as in_file:
            json.dump(self.statistics, in_file)
            in_file.close()

        with open(self.file_out, 'r') as r_file:
            print(json.load(r_file))

        # reset dir file to program file
        os.chdir(path_reset)

    def evaluate_file(self):
        """ class method, draws statistics from input file
        1) number of impacts (without blanks)
        2) number of characters (without blanks)
        3) number of words
        4) average word length
        5) word frequency
        6) character frequency
        saves statistical data in a dictionary
        """

        # list of signs with single impacts
        single_impacts = ["", "–", "-", "<", ">"]

        # list of signs with double impacts
        double_impacts = ["!", "§", "$", "%", "&", "/", "(", ")",
                          "=", "?", "*", "'", "\"", ";", ":", "_",
                          ">", "°"
                          ]

        # list of signs with triple impacts
        triple_impacts = ["²", "³", "[", "]", "{", "}", "\\", "~",
                          "µ", "€"
                          ]

        # 1) number of impacts (with blanks)

        # iterates through input file and counts number of impacts
        count = 0
        for element in self.file_string:

            if element in triple_impacts:
                count += 3
            elif element.isupper() or element in double_impacts:
                count += 2
            else:
                count += 1

        self.statistics["impact_total"] = count
        print("impact_total", self.statistics["impact_total"])

        # 2) number of signs (without blanks)

        # counts number of characters and signs without blank spaces
        str_without_blanks = self.file_string.replace(" ", "")

        self.statistics["chars_total"] = len(str_without_blanks)
        print("chars_total", self.statistics["chars_total"])

        # 3) number of words

        str_cleared = self.file_string

        # strip file of unnecessary signs (for later count of word length)
        for char in double_impacts:
            str_cleared = str_cleared.replace(char, "")
        for char in triple_impacts:
            str_cleared = str_cleared.replace(char, "")
        for char in [",", ".", "–"]:
            str_cleared = str_cleared.replace(char, "")

        word_list = str_cleared.replace("\n", " ").split(" ")

        # defining all indices that would yield invalid words
        to_remove = []
        for idx in range(0, len(word_list)):
            if word_list[idx] in single_impacts:
                to_remove.append(idx)

        # reverse index list to remove invalid elements from back of list
        #  to  front (prevents .pop of valid words, due to index changes)
        to_remove.reverse()

        for idx in to_remove:
            word_list.pop(idx)

        self.statistics["words_total"] = len(word_list)
        print("words_total", self.statistics["words_total"])

        # 4) average word length

        # determine and add length of every word to counter
        count = 0
        for word in word_list:
            count += len(word)

        #  write average word length in dictionary
        self.statistics["average_word_length"] = count / len(word_list)
        print("average_word_length", self.statistics["average_word_length"])

        # 5) word frequency

        # create set of word list, to create object that holds every word
        # in input file, exactly one time
        words_in_text = set(word_list)
        word_frequency = {}

        # creating dictionary with distinct words as keys
        for word in words_in_text:
            word_frequency[word] = 0
        # counting frequency of single words in word_list
        for word in word_list:
            word_frequency[word] += 1
        # dividing each word count by total number of words
        for word in words_in_text:
            word_frequency[word] = word_frequency[word] / \
                                   self.statistics["words_total"]

        self.statistics["word_frequency"] = word_frequency
        print("word_frequency", self.statistics["word_frequency"])

        # 6) char frequency

        chars_in_text = set(self.file_string)
        char_frequency = {}

        # creating dictionary with distinct chars as keys
        for char in chars_in_text:
            char_frequency[char] = 0
        # iterating over original file string
        for char in self.file_string:
            char_frequency[char] += 1
        # dividing each value by total number of chars
        for char in chars_in_text:
            char_frequency[char] = char_frequency[char] / len(self.file_string)

        self.statistics["char_frequency"] = char_frequency
        print("char_frequency", self.statistics["char_frequency"], '\n')

    def write_json_file(self):
        """ class method, writes statistical data into a JSON file"""

        # creates path of directory for json files
        self.path_out = os.path.join(os.path.dirname(__file__), "json")

        # check if directory 'json' exists in current working directory,
        # else create directory
        if not os.path.exists(self.path_out):
            os.makedirs(self.path_out)

        # create new filename
        dot_idx = self.file_in.find(".")
        self.file_out = self.file_in[:dot_idx] + ".json"

        path_reset = os.path.dirname(__file__)

        # change working directory to "json" directory
        os.chdir(self.path_out)

        with open(self.file_out, 'w') as in_file:
            json.dump(self.statistics, in_file)
            in_file.close()

        with open(self.file_out, 'r') as r_file:
            print('opened json file:', json.load(r_file))

        # reset working directory to directory of program file
        os.chdir(path_reset)


    def __init__(self, filename):
        """ constructor """

        self.file_string = ""
        self.file_in = filename
        self.statistics = {"words_total" : 0,
                           "chars_total" : 0,
                           "average_word_length" : 0,
                           "impact_total" : 0,
                           "word_frequency" : {},
                           "char_frequency" : {}
                           }



        self.read_file()
        self.evaluate_file()
        self.write_json_file()


if __name__ == "__main__":
    EvalFile("Morgen_Kinder.txt")