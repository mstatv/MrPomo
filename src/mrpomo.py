from collections import deque
import tkinter as tk
import tkinter.ttk as ttk

"""
# Created by mstatv
"""
'''
This file is to contain all elements related 
to the function of MrPomo's timer
the idea is to create a desktop productivity timer app
'''


# timer class, ttk.Frame is inherited
class Timer(ttk.Frame):
    # init function
    def __init__(self, parent):
        # make 'self' into ttk.Frame
        super().__init__(parent)

        self.time_actual = tk.StringVar(value="00:05")  # creating time actual variable

        # order of MrPomo sequence: work session, stretch, work session, stretch, work session, break
        # using conventional pomodoro technique --> though intervals will be longer
        # work sessions = 50 min; stretch = 10 min; break = 20 min
        self.mrpomo_sequ = ["MrPomo", "Stretch", "MrPomo", "Strech", "MrPomo", "Break"]
        self.mrpomo_sched = deque(self.mrpomo_sequ)
        self.mrpomo_current_session = tk.StringVar(value=self.mrpomo_sched[0])  # displaying current session title
        self.mrpomo_running = True  # boolean marker for run status

        self._countdown_counter = None  # private counter

        mrpomo_label = ttk.Label(self, textvariable=self.mrpomo_current_session)  # creating label
        mrpomo_label.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10, 0))  # placing label on grid

        # inner frame for MrPomo timer -> fixed height here of '100'
        frame_timer = ttk.Frame(self, height="100")
        frame_timer.grid(pady=(10, 0), sticky="NEWS")

        # label creation
        t_counter = ttk.Label(frame_timer, textvariable=self.time_actual)
        t_counter.place(relx=0.5, rely=0.5, anchor="center")  # halfway through frame, anchored at center

        # button container for start/stop/reset
        container_buttons = ttk.Frame(self, padding=10)  # holds buttons
        container_buttons.grid(row=2, column=0, sticky="EW")
        container_buttons.columnconfigure((0, 1, 2), weight=1)

        # start button
        self.button_start = ttk.Button(container_buttons, text="Start", command=self.t_start, cursor="tcross")
        self.button_start.grid(row=0, column=0, sticky="EW")

        # stop button
        self.button_stop = ttk.Button(
            container_buttons,
            text="Stop",
            state="disabled",
            command=self.t_stop,
            cursor="pencil"
        )
        self.button_stop.grid(row=0, column=1, sticky="EW", padx=5)

        # reset button
        self.button_reset = ttk.Button(container_buttons, text="Reset", command=self.t_reset, cursor="pencil")

    # t_start function for use with start button
    def t_start(self):
        self.mrpomo_running = True
        self.button_start["state"] = "disabled"
        self.button_stop["state"] = "enabled"
        self.countdown()

    # t_stop function for use with stop button
    def t_stop(self):
        self.mrpomo_running = False
        self.button_start["state"] = "enabled"
        self.button_stop["state"] = "disabled"

        # if _countdown_counter exists
        if self._countdown_counter:
            self.term_after(self._countdown_counter)
            self._countdown_counter = None

    # t_reset function for use with reset button
    def t_reset(self):
        self.t_stop()
        self.time_actual.set("50:00")  # reset starting time
        self.mrpomo_sched = deque(self.mrpomo_sequ)  # reset sequence

    # countdown of timer
    def countdown(self):
        # local variable of time actual
        time_actual = self.time_actual.get()

        # logic for countdown
        if self.mrpomo_running and time_actual != "00:00":
            # parsing minutes from seconds -> creating two variables
            mins, secs = time_actual.split(":")

            if int(secs) > 0:  # logic to countdown seconds
                mins = int(mins)
                secs = int(secs) - 1
            else:
                secs = 59
                mins = int(mins) - 1

            # format string to set minutes to 2 digits and seconds to 2 digits (MM:SS)
            self.time_actual.set(f"{mins:02d}:{secs:02d}")
            self._countdown_counter = self.after(1000, self.countdown)  # setting coutdown counter to self.after

        elif self.mrpomo_running and time_actual == "00:00":

            self.mrpomo_sched.rotate(-1)  # first value moved to end
            next_session = self.mrpomo_sched[0]  # move to next session from schedule
            self.mrpomo_current_session.set(next_session)  # change label of timer session

            # implementing logic for schedule set in Timer class -> __init__ function
            if next_session == "MrPomo":  # work session
                self.time_actual.set("50:00")
            elif next_session == "Stretch":  # stretch
                self.time_actual.set("10:00")
            elif next_session == "Break":  # break
                self.time_actual.set("20:00")

            self._countdown_counter = self.after(1000, self.countdown)  # setting counter to self.after value


# class for MrPomo timer inheriting from tkinter.Tk
class MrPomo(tk.Tk):
    # init function
    def __init__(self, *args, **kwargs):
        # making self = to tkinter object
        super().__init__(*args, **kwargs)

        self.title("MrPomo")
        self.columnconfigure(0, weight=1)  # content column, will always be towards top of window
        self.rowconfigure(1, weight=1)

        # container frame
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        # frame creation, using instance of Timer class
        frame_mrpomo = Timer(container)
        frame_mrpomo.grid(row=0, column=0, sticky="NEWS")


# TODO: SEPARATE PROGRAM INTO MULTIPLE FILES?

##############
# test block #
##############
test = MrPomo()
test.mainloop()
