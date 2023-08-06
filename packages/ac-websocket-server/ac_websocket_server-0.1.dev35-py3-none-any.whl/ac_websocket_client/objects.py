#!/usr/bin/env python

'''Assetto Corsa Websockets App Objects'''

import tkinter as tk
from tkinter import ttk

APP_TITLE = 'ACWS Client'
CONSOLE_X = 86
CONSOLE_Y = 17
ENTRY_X = 40
FRAME_X = 800
FRAME_Y = 100
PAD_X = 10
PAD_Y = 5


class DebugUI():
    '''Helper class to debug UI'''

    @classmethod
    def print_window_info(cls, w, depth=0):
        '''Print debug information on UI'''
        print('  ' * depth + f'{w.winfo_class()} w={str(w.winfo_width())}/{str(w.winfo_reqwidth())} h={str(w.winfo_height())}/{str(w.winfo_reqheight())} x/y=+{str(w.winfo_x())}+{str(w.winfo_y())}')
        for i in w.winfo_children():
            cls.print_window_info(i, depth+1)


class GriddedButton():
    '''Helper class to create a button in a grid'''

    @classmethod
    def create(cls, parent, row: int, column: int, **kwargs) -> ttk.Button:
        '''Helper function to create a button in a grid'''

        button = ttk.Button(parent, **kwargs)

        button.grid(row=row, column=column, padx=PAD_X, pady=PAD_Y)

        return button


class GriddedEntry():
    '''Helper class to create an entry in a grid'''

    @classmethod
    def create(cls, parent, row: int, column: int, **kwargs) -> ttk.Entry:
        '''Helper function to create a label in a grid'''

        entry = ttk.Entry(parent, width=ENTRY_X, **kwargs)

        entry.grid(row=row, column=column, padx=PAD_X, pady=PAD_Y)

        return entry


class GriddedFrame():
    '''Helper class to create a frame in a grid'''

    @classmethod
    def create(cls, row: int, column: int, height: float = 1, width: float = 1) -> tk.Frame:
        '''Helper function to create a Frame with no propogation and standard settings'''

        frame = ttk.Frame(height=FRAME_Y * height,
                          width=FRAME_X * width)

        frame.grid_propagate(False)

        frame.grid(row=row, column=column,
                   padx=PAD_X, pady=PAD_Y)

        return frame

    @classmethod
    def columnconfigure(cls, parent, *weights):
        '''Helper function to configure column weights'''
        i = 0
        for weight in weights:
            parent.columnconfigure(i, weight=weight)

    @classmethod
    def rowconfigure(cls, parent, *weights):
        '''Helper function to configure row weights'''
        i = 0
        for weight in weights:
            parent.rowconfigure(i, weights=weight)


class GriddedLabel():
    '''Helper class to create a label in a grid'''

    @classmethod
    def create(cls, parent, row: int, column: int, **kwargs) -> ttk.Label:
        '''Helper function to create a label in a grid'''

        label = ttk.Label(parent, **kwargs)

        label.grid(row=row, column=column, padx=PAD_X, pady=PAD_Y)

        return label


class GriddedListbox():
    '''Helper class to create a listbox in a grid'''

    @classmethod
    def create(cls, parent, **kwargs) -> tk.Listbox:
        '''Helper function to create a listbox in a grid'''

        listbox = tk.Listbox(parent,
                             height=CONSOLE_Y,
                             width=CONSOLE_X,
                             **kwargs)

        listbox.grid(row=0, column=0, padx=PAD_X, pady=PAD_Y)

        scrollbar = tk.Scrollbar()
        listbox.config(yscrollcommand=scrollbar.set)

        return listbox


class TrafficLight():
    '''Tk based traffic light'''

    def __init__(self, parent, row: int, column: int):
        self.colour = 'red'
        self.canvas = tk.Canvas(parent, width=20, height=20)
        self.canvas.grid(row=row, column=column, padx=PAD_X, pady=PAD_Y)
        self.light = self.canvas.create_oval(5, 5, 20, 20, fill=self.colour)

    def green(self):
        self.canvas.itemconfigure(self.light, fill='green')

    def red(self):
        self.canvas.itemconfigure(self.light, fill='red')
