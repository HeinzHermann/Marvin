"""Docstring: Modules defines class "Bike". New class has four attributes,
two of them beeing mileage and color. class also containes three methods.
Methods set/display the color of the bike and increse the mileage.
"""

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


class Ebike(bike):
    """New class "Ebike"
    This class contains all attributes and function of the "bike" class and two
    additional functions
    """
    def __init__(self, curr_capacity, consumption):
        self.curr_capacity = curr_capacity
        self.consumption = consumption
    
    def show_reach(self):
        reach = self.curr_capacity / self.consumption
        print("The maximum reach of this vehicle are", reach, "km.")


def main():
    """Main body of the modul"""
    ebike1 = Ebike(100, 4)
    ebike2 = Ebike(300, 20)
    print("ebike1:")
    ebike1.show_reach()
    print("\nebike2")
    ebike2.show_reach()
    
    help(Ebike)
    
if __name__ == '__main__':
    main()

