
from WordProcessor import Processor
import tkinter as tk
from tkinter import messagebox

class Game:

    #define an array of words
    __current_word = 1
    __words = [[],[],[]]
    __word_processor = Processor()
    active_textbox = []

    def start_game(self):

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
    
    def print_next_word(self, window: tk.Tk):
        selected_word = ''
        if self.__current_word <= 3: #First three easy words
            selected_word = self.__words[0][self.__current_word]
        elif self.__current_word > 3 and self.__current_word <= 6:
            selected_word = self.__words[1][self.__current_word]
        elif self.__current_word > 6:
            selected_word = self.__words[2][self.__current_word]

        # Create the widgets

        guess_label = tk.Label(window, text="Guess the word:", font=("Arial", 20))
        guess_label.grid(row=0, column=0, columnspan=3)
       

      
        last_added = None

        for i in range(len(selected_word[0])):
            textbox = tk.Entry(window, width=1, font=("Arial", 40))
            textbox.grid(row=1, column=i)
            textbox.bind("<<KeyPress>>", self.__move_focus)
            self.active_textbox.append(textbox)

           

        word_label = tk.Label(window, text=selected_word[1], font=("Arial", 40, "bold"))
        word_label.grid(row=2, column=0, columnspan=3)

    def __move_focus(self, event):
        # Function to move focus to the next textbox
        
        current_index = self.active_textbox.index(event.widget)
        current_text = event.widget.get()

        # Move focus to the next textbox if current textbox has reached the desired length
        if len(current_text) == 1:
            if current_index < len(self.active_textbox) - 1:
                self.active_textbox[current_index + 1].focus_set()
        


def countdown(seconds):

    if seconds > 0:
        time_label.config(text=f"Time left: {seconds} seconds")
        seconds -= 1
        window.after(1000, countdown, seconds)
    else:
        messagebox.showinfo("Countdown", "Time's up!")




# Create the main window

game = Game()
game.start_game()


window = tk.Tk()
window.title("Guess Game")

game.print_next_word(window)

time_label = tk.Label(window, text="Time left", font=("Arial", 12))
time_label.grid(row=3, column=2, sticky=tk.SE)

# Run the main window loop
window.mainloop()
