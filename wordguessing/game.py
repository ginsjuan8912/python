
from WordProcessor import Processor
import tkinter as tk
from tkinter import messagebox

def countdown(seconds):
    if seconds > 0:
        countdown_label.config(text=f"Time left: {seconds} seconds")
        seconds -= 1
        root.after(1000, countdown, seconds)
    else:
        messagebox.showinfo("Countdown", "Time's up!")

root = tk.Tk()
root.title("Countdown Window")

countdown_label = tk.Label(root, text="")
countdown_label.pack(pady=10)

start_button = tk.Button(root, text="Start Countdown", command=lambda: countdown(10))
start_button.pack(pady=10)

root.mainloop()

