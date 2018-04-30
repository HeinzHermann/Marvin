"""Docstring: Modules defines class "Bike". New class has four attributes,
two of them beeing mileage and color. class also containes three methods.
Methods set/display the color of the bike and increse the mileage.
"""

import random
#  import random library for randomized inc_miles increase

__author__ = "4424114: Marvin Glaser"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni" 
__credits__ = "If you would like to thank somebody \
              i.e. an other student for her code or leave it out" 
__email__ = "marvin.glaser91@gmail.com" 
  
class bike(): 
    """New class "bike"
    new class contains four attributes and three methods
    """ 
    
    vehicle = "motorcycle"
    mileage = 0
    horsepower = 100
        
    def set_color(self, color):
        """this function creates/redifines the color attribute of a bike
        instance.
        """
        self.color = color
        
    def show_color(self):
        """this function prints the color attribute of the instance"""
        
        print("The color of your bike is: ", self.color)
 
    def inc_miles(self, kilometers):
        """this function adds a defined integer to the mileage attribute"""
        self.mileage += kilometers
        #  adds number of kilometers to the milage variable
        #  kilometers, since miles are a terrible unit

def test_drive(name_bike1, name_bike2, rounds):
    """the function takes the variable names of two instances of the bike class
    and a number of rounds. during every round a random number of kilometers
    is determined and added to the total mileage of the instance.
    the results of every round are printed in the console.
    """
    
    random.seed(2.0)
    #  random.seed method enables reproducable results
    counter = 0
    #  coutner used to track numbers and print correct round number
    while counter < rounds:
        distance_bike1 = random.randrange(100,500)
        distance_bike2 = random.randrange(100,500)
        #  randoms distance for every bike
                
        name_bike1.inc_miles(distance_bike1)
        name_bike2.inc_miles(distance_bike2)
        #  adds randomed distance to total mileage of instance 1 and 2
        counter += 1
        
        print("Test drive, Round", str(counter) + ":")
        print("During round", counter, "bike1 drove",
              distance_bike1, "km, \nwhile", "bike2 drove", distance_bike2,
              "km.\n")
        print("The total mileage of", "bike1 is now:", 
              name_bike1.mileage, "km.")
        print("The total mileage of", "bike2 is now:",
              name_bike2.mileage, "km.\n\n")
        #  prints results of respective round in console
        
def main():
    """Main body of the modul"""
    bike1 = bike()
    bike2 = bike()
    # definition of bike 1 and 2
    
    bike1.set_color("Sarcoline")
    bike2.set_color("Smaragdine")
    #  sets colors of bike 1 and 2
    #  the names are weird but those are actual colors
    
    print("Color scheme:")
    print("The color of bike1 is \"" + str(bike1.color) + "\".")
    print("The color of bike2 is \"" + str(bike2.color) + "\".\n\n\n")    
    #  prints the colors of the bikes in the console
    
    test_drive(bike1, bike2, 3)
    #  executes function test drive to add random numbers to instance mileages        

if __name__ == '__main__':
    main()

