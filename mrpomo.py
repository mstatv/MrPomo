from collections import deque
import tkinter as tk
import tkinter.ttk as ttk
from src import Timer, Params

"""
# Created by mstatv
"""
'''
MAIN MrPomo File
the idea is to create a desktop productivity timer app
'''

# color constants, to color app
PRIMARY_CLR = "#26c6da"
SECONDARY_CLR = "#78909c"
BG_LIGHT_CLR = "#a7c0cd"
TXT_LIGHT_CLR = "#6ff9ff"
TXT_DARK_CLR = "#0095a8"


# class for MrPomo timer inheriting from tkinter.Tk
class MrPomo(tk.Tk):
    # init function
    def __init__(self, *args, **kwargs):
        # making self = to tkinter object
        super().__init__(*args, **kwargs)

        # style of app
        mrstyle = ttk.Style(self)
        mrstyle.theme_use("clam")

        mrstyle.configure("Timer.TFrame", background=BG_LIGHT_CLR)
        mrstyle.configure("Background.TFrame", background=PRIMARY_CLR)
        mrstyle.configure("TimerText.TLabel", background=BG_LIGHT_CLR, foreground=TXT_DARK_CLR, font="Sans 40")
        mrstyle.configure("LightText.TLabel", background=PRIMARY_CLR, foreground=TXT_LIGHT_CLR)

        mrstyle.configure("MrPomoButton.TButton", background=SECONDARY_CLR, foreground=TXT_LIGHT_CLR)
        mrstyle.map("MrPomoButton.TButton", background=[("active", PRIMARY_CLR), ("disabled", TXT_LIGHT_CLR)])

        # set self property for styling
        self["background"] = PRIMARY_CLR

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

        # dictionary creation for src frames
        self.src_frames = dict()

        # frame creation, using instance of Timer class
        frame_mrpomo = Timer(container, self, lambda: self.show_frame(Params))
        frame_mrpomo.grid(row=0, column=0, sticky="NEWS")

        # frame creation, using Params
        frame_params = Params(container, self, lambda: self.show_frame(MrPomo))
        frame_params.grid(row=0, column=0, sticky="NEWS")

        # adding to src_frames
        self.src_frames[MrPomo] = frame_mrpomo
        self.src_frames[Params] = frame_params

        self.show_frame(MrPomo)

    # show frame function
    def show_frame(self, container):
        frame = self.src_frames[container]
        frame.tkraise()


##############
# test block #
##############
test = MrPomo()
test.mainloop()
