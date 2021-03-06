"""
# Created by mstatv
"""
from tkinter import ttk
import tkinter as tk


# params class
class Params(ttk.Frame):
    def __init__(self, parent, controller, show_mrpomo):
        super().__init__(parent)

        # style
        self["style"] = "Background.TFrame"

        # appearance configure
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        # params container
        params_container = ttk.Frame(self, padding="30 15 30 15", style="Background.TFrame")
        params_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)
        params_container.columnconfigure(0, weight=1)
        params_container.rowconfigure(1, weight=1)

        # label for params container
        # mrpomo
        label_mrpomo = ttk.Label(params_container, text="MrPomo: ", style="LightText.TLabel")
        label_mrpomo.grid(column=0, row=0, sticky="W")

        # create spinbox
        # mrpomo
        input_mrpomo = tk.Spinbox(
            params_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.mrpomo,
            width=10
        )
        input_mrpomo.grid(column=1, row=0, sticky="EW")
        input_mrpomo.focus()

        # label for params container
        # stretch
        label_stretch = ttk.Label(params_container, text="Stretch: ", style="LightText.TLabel")
        label_stretch.grid(column=0, row=1, sticky="W")

        # create spinbox
        # stretch
        input_stretch = tk.Spinbox(
            params_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.stretch,
            width=10
        )
        input_stretch.grid(column=1, row=1, sticky="EW")
        input_stretch.focus()

        # label for params container
        # break
        label_break = ttk.Label(params_container, text="Break: ", style="LightText.TLabel")
        label_break.grid(column=0, row=2, sticky="W")

        # create spinbox
        # break
        input_break = tk.Spinbox(
            params_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.sbreak,
            width=10
        )
        input_break.grid(column=1, row=2, sticky="EW")
        input_break.focus()

        # create space between labels and spin boxes
        # appearance tinkering
        for child in params_container.winfo_children():
            child.grid_configure(padx=7, pady=7)

        # mrpomo timer button
        # sending user to timer screen/frame
        # container_mrpomo = ttk.Frame(self, style="Background.TFrame")
        # container_mrpomo.grid(sticky="EW", padx=7)
        # container_mrpomo.columnconfigure(0, weight=1)

        button_mrpomo = ttk.Button(
            self,
            text="MrPomo",
            command=show_mrpomo,
            style="MrPomoButton.TButton",
            cursor="tcross"
        )
        button_mrpomo.grid(row=0, column=1, sticky="E", padx=7, pady=(7, 0))
