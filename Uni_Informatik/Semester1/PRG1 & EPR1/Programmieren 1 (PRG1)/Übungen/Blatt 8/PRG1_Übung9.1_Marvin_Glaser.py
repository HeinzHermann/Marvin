"""module realizes and visualizes bubble sort algorithm in tkinter"""

import tkinter as tk
import time
from tkinter import messagebox

__author__ = "4424114: Marvin Glaser"
__credits__ = "no credits were given that day..."
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "marvin.glaser91@gmail.com"


class ui():
    """class used to implement bubble sort in tkinter/perform algorithm"""

    def gatekeeper(self, data):
        """checks user input for invalid input and returns feedback"""
        
        temp_split = data.split(' ')
        self.to_sort = []
        
        #  checks list form user input for non numeric elements
        for element in temp_split:
            if not element.isnumeric():
                
                #  opens messagebox with user feedback
                messagebox.showerror('That does not seem to be correct...',
                                     'We are very sorry, but your input was invalid\n'
                                     'Please enter a string of integers and separate\n'
                                     'each one with a <blank>'
                                     )
                return False
        
        #  prevents sorting of list with single elements
        if len(temp_split) == 1:
            messagebox.showerror('That does not seem to be correct...',
                                 'Well...your input only contained one element\n'
                                 'We dont think there is much to sort for the\n'
                                 'algorithm ;)\n'
                                 'Please enter a new set of integers!')
            return False
        
        #  creates integer list from user input
        for element in temp_split:
            self.to_sort.append(int(element))
        
        #  user feedback for valid input
        self.info.set('Great, your input was valid!\n'
                      'Now wait for the algorithm to do\nits magic!'
                      )
        return True


    
    def clicker(self):
        """gets entry input, wipes labels from previous runs"""
        
        #  wipes labels from earlyer runs
        self.show1.set(' ')
        self.show2a.set(' ')
        self.show2b.set(' ')
        self.show2c.set(' ')
        self.show3.set(' ')
        self.root.update()
        
        #  checks user input and starts bubblesort if input valid
        user_input = self.number_entry.get()
        if self.gatekeeper(user_input):
            self.bubblesort(self.to_sort)


    def pause(self):
        """pause button, not functional"""
        
         #self.pauser = False
         #if self.pauser:
         #    return
         #self.root.after(1, self.pause)


    def resume(self):
        """resume button, not functional"""
        #self.pauser = True


    def add_info(self):
        """gives user additional information about program in messagewindow"""
        
        messagebox.showinfo('Ruels', 'This window is desinged to sort numbers\n'
                            'for you!\nYou can enter a string of numbers\n'
                            '(The numbers must be integers) and the algorithm\n'
                            'called Bubble Sort will automatically order them\n'
                            'for you. Just enter some numbers, lean back and\n'
                            ' enjoy the machine doring all the work ;) \n\n'
                            '(IMPORTANT: The numbers must be separated by\n'
                            'exactly one <Space> (blank) each.)'
                            )

        
    def ui_manager(self, data, step, counter):
        """manages visualization till numbers are sorted"""
        
        #  manages comparison between two user numbers
        var_2b = str(data[step]) + ' < ' + str(data[step + 1])
        self.show2b.set(var_2b)
        
        #  check what elements need to be displayed on left side of comparison
        if (step - 1) == -1:
            var_2a = '[ '
            self.show2a.set(var_2a)
            
        elif (step - 2) == -1:
            var_2a = '[ ' + str(data[0])
            self.show2a.set(var_2a)
        
        else:
            var_2a = '[...,' + str(data[step - 2]) + ', ' + str(data[step - 1])
            self.show2a.set(var_2a)
        
        
        
        #  check what elements need to be displayed on right side of comparison
        if (step + 2) == len(data):
            var_2c = ' ]'
            self.show2c.set(var_2c)
        
        elif (step + 3) == len(data):
            var_2c = str(data[-1]) + ', ]'
            self.show2c.set(var_2c)
        
        elif (step + 4) == len(data):
            var_2c = str(data[-2]) + ', ' + str(data[-1]) + ', ]'
            self.show2c.set(var_2c)
        
        else:
            var_2c = str(data[step + 2]) + ', ' + str(data[step + 3]) + ',...]'
            self.show2c.set(var_2c)
            


    def ui_manager2(self, data, step):
        """handles visualization of number change animation, if postions of
        two nubmers are swaped
        """
        
        #  handles visualization of comparision between two numbers
        self.show2b.set(str(data[step]) + ' < ' + str(data[step + 1]))
        self.root.update()
        time.sleep(0.15)


        #  handles visualization of first step of swap animation
        var_show1 = str(data[step]) +  '   ' +  (' ' * len(str(data[step + 1])))
        var_show2 = ' ' * len(str(data[step])) + ' < ' + ' ' * len(str(data[step + 1]))
        var_show3 = (' ' * len(str(data[step]))) + '   ' + str(data[step + 1])
        self.show1.set(var_show1)
        self.show2b.set(var_show2)
        self.show3.set(var_show3)
        self.root.update()
        time.sleep(0.15)
        
        
        #  handles visualization of second step of swap animation
        var_show1 = data[step]
        var_show2 = ' < '
        var_show3 = data[step + 1]
        self.show1.set(var_show1)
        self.show2b.set(var_show2)
        self.show3.set(var_show3)
        self.root.update()
        time.sleep(0.15)
        

        #  handles visualization of third step of swap animation        
        var_show1 = (len(str(data[step + 1])) * ' ') + '   ' + str(data[step])
        var_show2 = ' ' * len(str(data[step])) + ' < ' + ' ' * len(str(data[step + 1]))
        var_show3 = str(data[step + 1]) + '   ' +  (' ' * len(str(data[step + 1])))
        self.show1.set(var_show1)
        self.show2b.set(var_show2)
        self.show3.set(var_show3)
        self.root.update()
        time.sleep(0.15)


        #  handles visualization of new state of swaped numbers
        self.show1.set(' ')
        self.show2b.set(str(data[step + 1]) + ' < ' + str(data[step]))
        self.show3.set(' ')
        self.root.update()
        time.sleep(0.15)
        


    def bubblesort(self, data):
        """bubble sort algorithm
        sorts numbers from user input and calls for visualization managers
        """
        
        #  coutner used to track how many numbers of user input are stable
        #  (sorted to end of list)
        counter = 0
        self.pauser = False
        
        #  loops till all nubmers are stable
        while counter < len(data):
            end_counter = 0
            
            #  iterate through all nubers - stable numbers
            for step in range((len(data) - counter)):
                
                #  if end of unstable numbers is reached, start new iteration
                if step == (len(data) - (counter + 1)):
                    if end_counter == 0:
                        counter = len(data)
                    else:
                        counter += 1
                
                #  call for user ai to update list status
                else:
                    self.ui_manager(data, step, counter)
                    self.root.update()
                    time.sleep(0.5)
                    
                    #  if swap of 2 numbers, call for ui manager2
                    if data[step] > data[step + 1]:
                        temp_var1 = data[step]
                        temp_var2 = data[step + 1]
                        self.ui_manager2(data, step)
                        data[step] = temp_var2
                        data[step + 1] = temp_var1
                        end_counter += 1
        
        #  show user final result
        self.show1.set('final result!')
        self.show2a.set(' ')
        self.show2b.set(' ')
        self.show2c.set(' ')
        self.show3.set(data)
        self.root.update()
        
        self.info.set('The algorithm is done!\n'
                      'You can continue to play, by\n'
                      'entering a new, unsorted set of numbers'
                     )

    def ui_main(self):
        """main function of ui class
        defines all buttons, labels and the entry of bubble sort program
        """
        self.root = tk.Tk()
        self.root.title('Bubble Sort - Algorithm')

        #  creates label to user
        label_entry = tk.Label(self.root, text = 'Hello User', height = 1, width = 10)
        label_entry.grid(row = 0, column = 0, columnspan = 2, sticky = 'W')
        
        #  creates entry for user input
        self.number_entry = tk.Entry(self.root, text = 'Hello')
        self.number_entry.grid(row = 1, column = 0, columnspan = 2)
        
        #  button associated with entry
        button_entry = tk.Button(self.root, text = 'Sort!',
                                 command = self.clicker
                                 )
        button_entry.grid(row = 1, column = 2, sticky = 'W')
        
        #  infor label, updates druing the game
        self.info = tk.StringVar()
        self.info.set('Hello dear user\n'
                      'Alease enter a number of integers\n'
                      'you would like the algorithm so sort')
        label_info = tk.Label(self.root, textvariable = self.info, width = 40)
        label_info.grid(row = 0, column = 3, rowspan = 2, columnspan = 4)
        
        # creates variables to update swap and sort animations
        self.show1 = tk.StringVar()
        self.show1.set(' ')
        self.show2a = tk.StringVar()
        self.show2a.set(' ')
        self.show2b = tk.StringVar()
        self.show2b.set(' ')
        self.show2c = tk.StringVar()
        self.show2c.set(' ')
        self.show3 = tk.StringVar()
        self.show3.set(' ')
        
        #  creates labels for swap and sort animation
        self.label_show1 = tk.Label(self.root, textvariable = self.show1)
        self.label_show1.grid(row = 3, column = 0, rowspan = 1, columnspan = 6, sticky = 'S')
        self.label_show2a = tk.Label(self.root, textvariable = self.show2a)
        self.label_show2a.grid(row = 4, column = 0, rowspan = 1, columnspan = 3, sticky = 'E')
        self.label_show2b = tk.Label(self.root, textvariable = self.show2b)
        self.label_show2b.grid(row = 4, column = 3, rowspan = 1, columnspan = 1, sticky = 'NESW')
        self.label_show2c = tk.Label(self.root, textvariable = self.show2c)
        self.label_show2c.grid(row = 4, column = 4, rowspan = 1, columnspan = 3, sticky = 'W')
        self.label_show3 = tk.Label(self.root, textvariable = self.show3)
        self.label_show3.grid(row = 5, column = 0, rowspan = 1, columnspan = 6, sticky = 'N')
        
        #  creates pause, resume and info buttons
        button_pause = tk.Button(self.root, text = 'Pause', command = self.pause, width = 8)
        button_pause.grid(row = 6, column = 0, sticky = 'W')
        button_resume = tk.Button(self.root, text = 'Resume', command = self.resume, width = 8)
        button_resume.grid(row = 6, column = 1, sticky = 'W')
        button_info = tk.Button(self.root, text = 'more info', command = self.add_info, width = 8)
        button_info.grid(row = 6, column = 5, sticky = 'W')
        
        self.root.mainloop()    
        
                
def main():
    """main loop of the program
    executed, if __name__ == '__main__
    '"""
    
    user_interface = ui()
    user_interface.ui_main()


if __name__ == '__main__':
    main()
