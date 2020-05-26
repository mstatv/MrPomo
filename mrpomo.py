from collections import deque
import tkinter as tk
import tkinter.ttk as ttk
from src import Timer, Params

"""
# Created by mstatv
"""
'''
This file is to contain all elements related 
to the function of MrPomo's timer
the idea is to create a desktop productivity timer app
'''


# class for MrPomo timer inheriting from tkinter.Tk
class MrPomo(tk.Tk):
    # init function
    def __init__(self, *args, **kwargs):
        # making self = to tkinter object
        super().__init__(*args, **kwargs)

        self.title("MrPomo")
        self.columnconfigure(0, weight=1)  # content column, will always be towards top of window
        self.rowconfigure(1, weight=1)

        # values for controller
        self.mrpomo = tk.StringVar(value=50)
        self.stretch = tk.StringVar(value=10)
        self.sbreak = tk.StringVar(value=20)

        # order of MrPomo sequence: work session, stretch, work session, stretch, work session, break
        # using conventional pomodoro technique --> though intervals will be longer
        # work sessions = 50 min; stretch = 10 min; break = 20 min
        self.mrpomo_sequ = ["MrPomo", "Stretch", "MrPomo", "Strech", "MrPomo", "Break"]
        self.mrpomo_sched = deque(self.mrpomo_sequ)

        # container frame
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        # frame creation, using instance of Timer class
        frame_mrpomo = Timer(container, self)
        frame_mrpomo.grid(row=0, column=0, sticky="NEWS")
        
        # frame creation, using Params
        frame_params = Params(container, self)
        frame_params.grid(row=0, column=0, sticky="NEWS")

##############
# test block #
##############
test = MrPomo()
test.mainloop()
