import tkinter as tk
from tkinter import filedialog, Text
import os

import numpy as np
import pandas as pd
import openpyxl
import glob

import array as arr
import test
import app
import addFunctions
import searchFunction1
import searchFunction2
import searchFunction3


def addFolder():
    folderPath = filedialog.askdirectory(title="Select Folder")
    app.entry4.delete(0, tk.END)
    app.entry4.insert(0, folderPath)


def addDestination():
    folderDestination = filedialog.askdirectory(title="Select Folder")
    app.entry5.delete(0, tk.END)
    app.entry5.insert(0, folderDestination)
