"""Docstring: Modules defines class "Bike". New class has four attributes,
two of them beeing mileage and color. class also containes three methods.
Methods set/display the color of the bike and increse the mileage.
"""


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
    
    

def main():
    """Main body of the modul"""
    bike1 = bike()
    print("Bike number 1 is a", str(bike1.vehicle) + ".")
    print("The bike has driven a total of", bike1.mileage, "Kilometers.")
    print("The motor of the bike has", bike1.horsepower, "hp.")

if __name__ == '__main__':
    main()

