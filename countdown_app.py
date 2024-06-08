"""
    This program takes in input as seconds and evaluates it into respective hour, minutes and seconds. 
    Input can also be in a time format (00:00:00). When the countdown is done , a notification box appears to show times up
"""

import time 
import tkinter as tk
from tkinter import messagebox


class CountDownTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry = ("460x220")
        self.root.title("Countdown Timer")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.time_entry = tk.Entry(self.root, font = ("Arial", 30 ))
        self.time_entry.grid(row= 0 , column= 0 , columnspan=2, padx= 5, pady=5)

        self.start_button= tk.Button(self.root, font = ("Helvetica", 30 ), text= "Start",background="green",command= self.start)
        self.start_button.grid(row=1 , column= 0, padx= 5, pady= 5)

        self.stop_button= tk.Button(self.root, font = ("Helvetica", 30 ), text= "Stop",background="red", command= self.stop)
        self.stop_button.grid(row=1 , column=1, padx= 5, pady= 5)

        self.time_label = tk.Label(self.root, font= ("Helvetica", 30), text= "Time: 00:00:00")
        self.time_label.grid(row= 2 , column=0 , columnspan=2, padx=5, pady=5)

        self.stop_loop  = False
        self.root.mainloop()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 00, 00, 00
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes =int( string_split[1])
            seconds = int(string_split[2])

        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])

        elif len(string_split) == 1:
            seconds = int(string_split[0])

        else:
            print("invalid Time Format")
            return


        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds , 60)
            hours , minutes = divmod(minutes, 60)

            self.time_label.config(text=f"Time: {int(hours): 03d}:{int(minutes): 03d}:{int(seconds): 03d}")
            self.root.update()
            time.sleep(1)

        if not self.stop_loop:
            messagebox.showinfo("Timer", "Times Up")
            

    def stop(self):
        self.stop_loop= True 
        self.time_label.config(text= "Text: 00:00:00")

    def on_closing(self):
        if messagebox.askyesno("Exit","Quit?"):
            self.stop()
            self.root.destroy()
            
                 
CountDownTimer()