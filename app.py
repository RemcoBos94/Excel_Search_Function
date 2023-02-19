import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
import sys
import numpy as np
import pandas as pd
import openpyxl
import glob

import array as arr

import app
import Controller
import addFunctions
import searchFunction1
import searchFunction2
import searchFunction3


root = tk.Tk()
root.configure(background='#98EA8A')
root.geometry("700x550")

def Quit():
    sys.exit()



canvas = tk.Canvas(root, bd=0, highlightthickness=0, relief='ridge', bg="#98EA8A")
canvas.pack()


label1 = tk.Label(canvas, text="Excel Search Function", pady=0, font=('Times New Roman', 20), background='#98EA8A')
label1.pack()

label2 = tk.Label(canvas, text="Excel files must include these strings =>", pady=20, font=('Times New Roman', 15), background='#98EA8A')
label2.pack()

label3 = tk.Label(canvas, text="AND", pady=15, font=('Times New Roman', 15), background='#98EA8A')
label3.pack()

label4 = tk.Label(canvas, text="AND", pady=15, font=('Times New Roman', 15), background='#98EA8A')
label4.pack()

label5 = tk.Label(canvas, text="Folder where excel files must be examined", pady=20, font=('Times New Roman', 15), background='#98EA8A')
label5.pack()


openFolder = tk.Button(canvas, text="Open Folder", padx=10, pady=5, fg="white", bg="green", command=addFunctions.addFolder)
openFolder.pack()

label6 = tk.Label(canvas, text="Folder where positive excel files must be copied to", pady=20, font=('Times New Roman', 15), background='#98EA8A')
label6.pack()


openDestination = tk.Button(canvas, text="Open Folder", padx=10, pady=5, fg="white", bg="green", command=addFunctions.addDestination)
openDestination.pack()

searchFunction = tk.Button(canvas, text="Search and Transfer", padx=10, pady=5, fg="white", bg="green", command=Controller.C)
searchFunction.pack()

searchFunction = tk.Button(canvas, text="Exit", padx=10, pady=5, fg="white", bg="red", command=Quit)
searchFunction.pack()


entry1 = tk.Entry (canvas)
canvas.create_window(205, 100, window=entry1, width=250)

entry2 = tk.Entry (canvas)
canvas.create_window(205, 155, window=entry2, width=250)

entry3 = tk.Entry (canvas)
canvas.create_window(205, 210, window=entry3, width=250)

entry4 = tk.Entry (canvas)
canvas.create_window(400, 295, window=entry4, width=250)

entry5 = tk.Entry (canvas)
canvas.create_window(400, 395, window=entry5, width=250)































root.mainloop()




























