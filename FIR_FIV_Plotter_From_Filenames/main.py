# This is a sample Python script.
import csv
from tkinter import *
from tkinter import ttk
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *

import cv2

from matplotlib import pyplot as plt, gridspec
import numpy as np
import xlwt
from xlsxwriter import Workbook

def massProcessing():
    global fileNames
    fileNames = askopenfilenames(parent=window)
    fileNames = sorted(fileNames)
    output = format(text2.get("1.0",'end-1c'))

    FIR_RAW = []
    FIV_RAW = []

    for i in range (len(fileNames)):
        print(fileNames[i])
        if (fileNames[i].find("_FIR_") != -1):
            FIR_position = fileNames[i].find("FIR") + 4
            FIR = fileNames[i][FIR_position:-4]
            FIR = float(FIR.replace(',', '.'))
            print(FIR)
            FIR_RAW.append(FIR)
        if (fileNames[i].find("_FIV_") != -1):
            FIV_position = fileNames[i].find("FIV") + 4
            FIV = fileNames[i][FIV_position:-4]
            FIV = float(FIV.replace(',', '.'))
            print(FIV)
            FIV_RAW.append(FIV)
    print(len(FIR_RAW))

    with open(output, 'a', newline='\n') as f:
        for j in range(min(len(FIR_RAW),len(FIV_RAW))):
            print(j)
            writer = csv.writer(f, delimiter=' ')
            writer.writerow([j,FIR_RAW[j],FIV_RAW[j]])
            # writer.writerow(FIV_RAW)

            #
            # im = cv2.imread(fileNames[i])
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            # im = im[:,:,1]  # 2 for Nikita, 0 for Inessa, 1 for Andrew :)
            # im = im[:,:,1]  # 2 for Nikita, 0 for Inessa, 1 for Andrew :)
            # cv2.imshow('test', im)
            # sum = np.sum(im[(200):(500),(200):(500)])
            # sum = np.sum(im[(0):(1080), (0):(1440)])
            # sum = np.uint32(sum)
            # print(sum)
            #     writer.writerow([i,FIV, FIR])
       # Kf.close()
    plt.figure()
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('FIV, FIR, unitless')
    plt.title('FIR, FIV vs time')
    x = np.linspace(1,len(FIR_RAW),len(FIR_RAW))
    plt.plot(x, FIR_RAW, 'red',marker='o', label = 'FIR')
    x = np.linspace(1, len(FIV_RAW), len(FIV_RAW))
    plt.plot(x, FIV_RAW, 'violet',marker='o', label='FIV')
    plt.legend()
    plt.show()
    # plt.pause(0.01)  # pause
    text1.insert(INSERT, 'Готово')

def selectOutfile():
    Output = filedialog.askdirectory(parent=window)
    OutputF = Output + '/labs1.csv'
    text2.insert(INSERT, OutputF)

    # global fileName, fileNameBase, fileNameBaseBG, fileNameBG, imBase, im, imBG, BG_normalized, imBaseBG
    # text1.delete(1.0, END)
    # text1.delete(1.0, END)
    # fileName = askopenfilenames(parent=window)
    # text1.insert(INSERT, fileName)
    # fileName = format(text1.get("1.0", 'end-1c'))
    # im = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
    # # im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    # print(type(im))
    # coef = int(text1.get(1.0, END))
    # im_multiplied = cv2.multiply(np.uint8(im), coef)
    # outputFilename = format(text1.get("1.0", 'end-1c')) + "_multiplied.png"
    #
    # cv2.imwrite(outputFilename, im_multiplied)
    # cv2.imshow(outputFilename, im_multiplied)
    # # plt.title('im multiplied')
    # # plt.colorbar()
    # # plt.show()
    # # fileName = fileName[:-3]
    # # plt.savefig(fileName + 'png')
    # # plt.show()
    # # outputFile = format(text3.get("1.0", 'end-1c'))
    return
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('1150x650')
    window.title("MassProcessing")
    text1 = Text(width=15, height=1)  # image
    text1.grid(column=1, row=1, sticky=W)
    text2 = Text(width=70, height=1)  # image
    text2.grid(column=1, row=0, sticky=W)
    btn1 = Button(window, text="Select Images", command=massProcessing)
    btn1.grid(column=0, row=1, sticky=W)
    btn2 = Button(window, text="Select SavePlace", command=selectOutfile)
    btn2.grid(column=0, row=0, sticky=W)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
