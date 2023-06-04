
from random import choice
import winsound
from WordProcessor import Processor
import tkinter as tk
from tkinter import messagebox

class Game:

    #ui components
    seconds_left = 20
    label_timer = None
    main_window = None
    #define the completed word
    completed_word = ''
    selected_word = ''
    words_completed = 0
    #define an array of words
    __current_word = 0
    __index = 0
    __words = [[],[],[]]
    __word_processor = Processor()
    active_textbox = []

    def prepare_game(self):

        self.__word_processor.load_words()

        set_words_ready = 0
        while set_words_ready < 3:
            for i in range(0,3):

                if set_words_ready == 0: #first set will load easy words
                    self.__words[0].append(self.__word_processor.next_easy_word())

                if set_words_ready == 1: #second set will load medium words
                    self.__words[1].append(self.__word_processor.next_medium_word())
                
                if set_words_ready == 2: #third set will load hard words
                    self.__words[2].append(self.__word_processor.next_hard_word())
                
            set_words_ready += 1
    
    def next_word(self, window: tk.Tk):
        
        if self.__current_word < 3: #First three easy words
            self.selected_word = self.__words[0][self.__index]
        elif self.__current_word >= 3 and self.__current_word < 6:
            self.selected_word = self.__words[1][self.__index]
        elif self.__current_word >= 6:
            self.selected_word = self.__words[2][self.__index]

        if self.__index == 2:
            self.__index = -1
        self.__index += 1

        # Create the widgets

        guess_label = tk.Label(window, text="Guess the word:", font=("Arial", 15))
        guess_label.grid(row=0, column=0)

        for i in range(len(self.selected_word[0])):
            textbox = tk.Entry(window, width=2, font=("Arial", 35), justify=tk.CENTER)
            textbox.grid(row=2, column=i, padx=5, pady=20)
            textbox.bind("<KeyRelease>", self.__move_focus)
            self.active_textbox.append(textbox)

        word_label = tk.Label(window, text=self.selected_word[0], font=("Arial", 40, "bold"))
        word_label.grid(row=4, column=0, columnspan=5)

    def __move_focus(self, event):
        
        current_index = self.active_textbox.index(event.widget)
         # Check if Backspace key was pressed
        if event.keysym == 'BackSpace':
        # Handle the Backspace key event here
            if current_index > 0:
                self.active_textbox[current_index - 1].focus_set()
                return
        
        # Function to move focus to the next textbox
        current_text = event.widget.get()

        # Move focus to the next textbox if current textbox has reached the desired length
        if len(current_text) == 1:
            next_index = current_index + 1
            if current_index < len(self.active_textbox) - 1:
                while(self.active_textbox[next_index].get() != ''):
                    next_index += 1
                self.active_textbox[next_index].focus_set()

    def print_game(self):

        if self.main_window is not None:
            self.remove_all_widgets()
            self.active_textbox = []
        else:
            self.main_window = tk.Tk()

        self.main_window.title("Guess Game")  

        game.next_word(self.main_window)

        time_label = tk.Label(self.main_window, text="Time left", font=("Arial", 12))
        time_label.grid(row=5, column=2, sticky=tk.SE)

        game.label_timer = time_label
        self.update()

        self.main_window.focus_force()
        self.main_window.mainloop()
    
    def update(self):

        if(self.seconds_left == 0):
            self.main_window.destroy()
            messagebox.showinfo("Game Over", "Game Over")
            return

       #sorround with try except the following code
        try:
            if(self.seconds_left == 15 or self.seconds_left == 11 or self.seconds_left == 8 or self.seconds_left == 4):
                word_indx = choice(range(0, len(self.selected_word[0])))

                if (self.active_textbox[word_indx] != None):
                    if(self.active_textbox[word_indx].get() == ''):
                        character = self.selected_word[0][word_indx]
                        self.active_textbox[word_indx].insert(0, character)
                        self.active_textbox[word_indx].config(state="disabled")
            
            if(self.seconds_left == 10):
                self.label_timer.config(bg="orange")
            if(self.seconds_left == 5):
                self.label_timer.config(bg="red")
        except Exception as e:
            print(e)
            pass    

        #trim all whitespaces on self.completed_word
        self.completed_word = ''
        for i in range(0, len(self.active_textbox)):
            self.completed_word += self.active_textbox[i].get()
            self.completed_word = self.completed_word.strip()

        if(self.completed_word == self.selected_word[0] and self.words_completed < 20):
            self.words_completed += 1
            self.__current_word += 1
            self.completed_word = ''
            self.seconds_left = 20
            self.print_game()

        #if seconds_left less or equal to 3, then beep sound
        if(self.seconds_left <= 3):
            winsound.Beep(1000, 100)

        self.label_timer.config(text=f"Time left: {self.seconds_left } seconds")    
        self.seconds_left -= 1 
        self.main_window.after(1000, self.update )
    

    def remove_all_widgets(self):
    # Get a list of all the widgets in the window
        widgets = self.main_window.winfo_children()

        # Remove each widget from the window
        for widget in widgets:
            widget.destroy()

game = Game()
game.prepare_game()
game.print_game()

   

