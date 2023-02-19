import numpy as np
import pandas as pd
import openpyxl
import glob
import os
import array as arr
import test

import app
import Controller
import addFunctions
import searchFunction1
import searchFunction2
import searchFunction3



def C():
    test1 = app.entry1.get()
    test2 = app.entry2.get()
    test3 = app.entry3.get()
    test4 = app.entry4.get()
    test5 = app.entry5.get()

    if test4.strip():
        if test5.strip():
            if test1.strip() and test2.strip() and test3.strip():
                searchFunction3.sf3()
            else:
                if test1.strip() and test2.strip():
                    searchFunction2.sf2()
                else:
                    if test1.strip() and test3.strip():
                        app.tk.messagebox.showerror(title="error", message="Fill in the string(s) in the right place!!")
                    else:
                        if test1.strip():
                            searchFunction1.sf1()
                        else:
                            app.tk.messagebox.showerror(title="error", message="Fill in the string(s) in the right place!!")
        else:
            app.tk.messagebox.showerror(title="error", message="Fill in the string(s) in the right place!! Also make sure you select a destination Folder!!")
    else:
        app.tk.messagebox.showerror(title="error", message="Fill in the string(s) in the right place!! Also make sure you select an origin and destination Folder!!")
            
                
        

















                


   