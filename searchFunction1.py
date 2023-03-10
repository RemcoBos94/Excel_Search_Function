import numpy as np
import pandas as pd
import openpyxl
import glob
import os
import array as arr
import shutil

import app
import Controller
import addFunctions
import searchFunction1
import searchFunction2
import searchFunction3


def sf1():

    # Input => data coming from UI

    global input1
    input1 = app.entry1.get()
  
    global folderPath
    folderPath = app.entry4.get()

    global folderDestination
    folderDestination = app.entry5.get()


    # Main Code

    os.chdir(folderPath)
    FileList = glob.glob('**/*.xlsx', recursive=True)
    
    y = len(FileList)
    out = arr.array('h')
    
    for x in range(y):
    
        counter = 0
        xls = pd.ExcelFile(FileList[x])
        sheetNames = xls.sheet_names
        l = len(sheetNames)

        for i in range(l):

            df = pd.read_excel(FileList[x], sheet_name=sheetNames[i])
            filteredData1= df[df.apply(lambda row: row.astype(str).str.contains(input1).any(), axis=1)]
            if not filteredData1.empty:
                counter = counter + 1

        if counter == 0:
            out.append(0)
        else:
            out.append(1)

    
    z = 0
    for x in range(y):
        if out[x] == 0:
            del FileList[z]
        else:
            z = z + 1


    # Output => transfers excel files that contain the given string to a selected folder

    n = len(FileList)

    for i in range(n):
        filei = FileList[i]
        substring = "\\"
        if filei.find(substring) != -1:
            filej = filei.replace("\\","/")
            split_string = filej.rsplit("/", 1)
            filename = split_string[1]
            original = r'' + folderPath + '/' + filej
            target = r'' + folderDestination + '/' + filename
            shutil.copyfile(original, target)
        else:
            original = r'' + folderPath + '/' + filei
            target = r'' + folderDestination + '/' + filei
            shutil.copyfile(original, target)

    app.tk.messagebox.showinfo(title="Info", message="Transfer Completed! There are " + str(n) + " excel files transfered to " + folderDestination)
