"""
# Created by mstatv
"""
'''
This file is to contain all elements related 
to the function of MrPomo's timer
the idea is to create a desktop productivity timer app
'''

import tkinter as tk
import tkinter.ttk as ttk


# timer class, ttk.Frame is inherited
class Timer(ttk.Frame):
    # init function
    def __init__(self, parent):
        # make 'self' into ttk.Frame
        super().__init__(parent)

        self.time_actual = tk.StringVar(value="00:10")  # creating time actual variable
        self.mrpomo_running = True  # boolean marker for run status

        # inner frame for MrPomo timer -> fixed height here of '100'
        frame_timer = ttk.Frame(self, height="100")
        frame_timer.grid(pady=(10, 0), sticky="NEWS")

        # label creation
        t_counter = ttk.Label(frame_timer, textvariable=self.time_actual)
        t_counter.grid()

        # calling next function
        self.countdown()

    # countdown of timer
    def countdown(self):
        # local variable of time actual
        time_actual = self.time_actual.get()




# class for MrPomo timer inheriting from tkinter.Tk
class MrPomoTimer(tk.TK):
    # init function
    def __init__(self, *args, **kwargs):
        # making self = to tkinter object
        super().__init__(*args, **kwargs)

        self.title("MrPomo")
        self.columnconfigure(0, weight=1)  # content column, will always be towards top of window

        # container frame
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        # frame creation, using instance of Timer class
        frame_mrpomo = Timer(container)
        frame_mrpomo.grid(row=0, column=0, sticky="NEWS")

