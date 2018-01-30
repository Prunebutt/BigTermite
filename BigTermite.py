#! /usr/bin/env python3
#
# GUI module generated by PAGE version 4.10
# In conjunction with Tcl version 8.6
#    Jan 29, 2018 06:35:47 PM
# -*- coding utf-8 -*-

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import layout_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    layout_support.set_Tk_var()
    top = Big_Termite (root)
    layout_support.init(root, top)
    root.mainloop()

w = None
def create_Big_Termite(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    layout_support.set_Tk_var()
    top = Big_Termite (w)
    layout_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Big_Termite():
    global w
    w.destroy()
    w = None


class Big_Termite:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+648+269")
        top.title("Big Termite")
        top.bind('<Button-1>',layout_support.lambd)

        top.bind('0', lambda e: layout_support.record_action('Zucken P', True))
        top.bind('1', lambda e: layout_support.record_action('Laufen'))
        top.bind('2', lambda e: layout_support.record_action('Antenne A', True))
        top.bind('3', lambda e: layout_support.record_action('Antenne P', True))
        top.bind('4', lambda e: layout_support.record_action('Troph. A'))
        top.bind('5', lambda e: layout_support.record_action('Troph. B'))
        top.bind('6', lambda e: layout_support.record_action('Ruhen'))
        top.bind('7', lambda e: layout_support.record_action('Putzen A'))
        top.bind('8', lambda e: layout_support.record_action('Putzen P'))
        top.bind('9', lambda e: layout_support.record_action('Zucken A', True))
        top.bind('p', lambda e: layout_support.record_action('Anderes'))

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.03, rely=0.04, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=565)

        self.TimerDisplay = Label(top)
        self.TimerDisplay.place(relx=0.25, rely=0.17, height=26, width=90)
        self.TimerDisplay.configure(font=("Courier", 14))
        self.TimerDisplay.configure(relief=RAISED)
        self.TimerDisplay.configure(text='''00:00:00.00''')
        self.TimerDisplay.configure(textvariable=layout_support.timer_display)

        self.StartButton = ttk.Button(self.Frame1)
        self.StartButton.place(relx=0.74, rely=0.04, height=57, width=97)
        self.StartButton.configure(command= lambda: layout_support.start_pause_tracker())
        self.StartButton.configure(takefocus="")
        self.StartButton.configure(text='''Start''')

        self.StopButton = ttk.Button(self.Frame1)
        self.StopButton.place(relx=0.74, rely=0.19, height=57, width=97)
        self.StopButton.configure(command=layout_support.stop_tracker)
        self.StopButton.configure(takefocus="")
        self.StopButton.configure(text='''Stop''')
        self.StopButton.configure(state=DISABLED)

        self.ExportChecker = Checkbutton(self.Frame1)
        self.ExportChecker.place(relx=0.50, rely=0.24, relheight=0.05
                                 , relwidth=0.12)
        self.ExportChecker.configure(activebackground="#d9d9d9")
        self.ExportChecker.configure(justify=LEFT)
        self.ExportChecker.configure(state=ACTIVE)
        self.ExportChecker.configure(text='''Export''')
        self.ExportChecker.configure(variable=layout_support.export_checker)

        self.DecimalComma = Checkbutton(self.Frame1)
        self.DecimalComma.place(relx=0.50, rely=0.1, relheight=0.05
                                 , relwidth=0.22)
        self.DecimalComma.configure(activebackground="#d9d9d9")
        self.DecimalComma.configure(justify=LEFT)
        self.DecimalComma.configure(state=ACTIVE)
        self.DecimalComma.configure(text='''Dezimal Comma''')
        self.DecimalComma.configure(variable=layout_support.decimal_comma)

        self.RunButton = ttk.Button(self.Frame1)
        self.RunButton.place(relx=0.09, rely=0.5, height=57, width=97)
        self.RunButton.configure(command= lambda: layout_support.record_action('Laufen'))
        self.RunButton.configure(takefocus="")
        self.RunButton.configure(text='''Laufen (1)''')

        self.RestButton = ttk.Button(self.Frame1)
        self.RestButton.place(relx=0.1, rely=0.78, height=57, width=97)
        self.RestButton.configure(command= lambda: layout_support.record_action('Ruhen'))
        self.RestButton.configure(takefocus="")
        self.RestButton.configure(text='''Ruhen (6)''')

        self.AntennaPButton = ttk.Button(self.Frame1)
        self.AntennaPButton.place(relx=0.42, rely=0.53, height=47, width=97)
        self.AntennaPButton.configure(command= lambda: layout_support.record_action('Antenne P',
                                                                                    True))
        self.AntennaPButton.configure(takefocus="")
        self.AntennaPButton.configure(text='''Antenne P (3)''')
        self.AntennaPButton.configure(width=97)

        self.CleanPButton = ttk.Button(self.Frame1)
        self.CleanPButton.place(relx=0.42, rely=0.84, height=47, width=97)
        self.CleanPButton.configure(takefocus="")
        self.CleanPButton.configure(command= lambda: layout_support.record_action('Putzen P'))
        self.CleanPButton.configure(text='''Putzen P (8)''')
        self.CleanPButton.configure(width=97)

        self.AntennaAButton = ttk.Button(self.Frame1)
        self.AntennaAButton.place(relx=0.42, rely=0.41, height=47, width=97)
        self.AntennaAButton.configure(command= lambda: layout_support.record_action('Antenne A',
                                                                                    True))
        self.AntennaAButton.configure(takefocus="")
        self.AntennaAButton.configure(text='''Antenne A (2)''')
        self.AntennaAButton.configure(width=97)

        self.CleanAButton = ttk.Button(self.Frame1)
        self.CleanAButton.place(relx=0.42, rely=0.72, height=47, width=97)
        self.CleanAButton.configure(command= lambda: layout_support.record_action('Putzen A'))
        self.CleanAButton.configure(takefocus="")
        self.CleanAButton.configure(text='''Putzen A (7)''')
        self.CleanAButton.configure(width=97)

        self.TwitchAButton = ttk.Button(self.Frame1)
        self.TwitchAButton.place(relx=0.74, rely=0.79, height=37, width=97)
        self.TwitchAButton.configure(command= lambda: layout_support.record_action('Zucken A',
                                                                                   True))
        self.TwitchAButton.configure(takefocus="")
        self.TwitchAButton.configure(text='''Zucken A (9)''')
        self.TwitchAButton.configure(width=97)

        self.TwitchPButton = ttk.Button(self.Frame1)
        self.TwitchPButton.place(relx=0.74, rely=0.88, height=37, width=97)
        self.TwitchPButton.configure(command= lambda: layout_support.record_action('Zucken P',
                                                                                   True))
        self.TwitchPButton.configure(takefocus="")
        self.TwitchPButton.configure(text='''Zucken P (0)''')
        self.TwitchPButton.configure(width=97)

        self.OtherButton = ttk.Button(self.Frame1)
        self.OtherButton.place(relx=0.74, rely=0.65, height=37, width=97)
        self.OtherButton.configure(command= lambda: layout_support.record_action('Anderes'))
        self.OtherButton.configure(takefocus="")
        self.OtherButton.configure(text='''Anderes (P)''')
        self.OtherButton.configure(width=97)

        self.TrophAButton = ttk.Button(self.Frame1)
        self.TrophAButton.place(relx=0.74, rely=0.41, height=37, width=97)
        self.TrophAButton.configure(command= lambda: layout_support.record_action('Troph. A'))
        self.TrophAButton.configure(takefocus="")
        self.TrophAButton.configure(text='''Troph. A (4)''')
        self.TrophAButton.configure(width=97)

        self.TrophPButton = ttk.Button(self.Frame1)
        self.TrophPButton.place(relx=0.74, rely=0.5, height=37, width=97)
        self.TrophPButton.configure(command= lambda: layout_support.record_action('Troph. P'))
        self.TrophPButton.configure(takefocus="")
        self.TrophPButton.configure(text='''Troph. P (5)''')
        self.TrophPButton.configure(width=97)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.0, rely=0.95, height=19, width=244)
        self.Label2.configure(text='''Big Termite, Copyright: Flossmann 2018''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


if __name__ == '__main__':
    vp_start_gui()
