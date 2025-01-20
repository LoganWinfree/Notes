import tkinter
import tkinter.ttk as ttk
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sb


def preview():
   print("Preview")

def save():
   print("Save")


def main():
    fPad = 10
    fWidth = 600
    fWidthTotal = fWidth + 2*fPad
    fHeight = 300

    bgColor = "black"

    distOptions = ["Binomial", "Normal"]



    root = tkinter.Tk()
    root.title("Stats Pdf Constructor")
    root.config(bg=bgColor)
    root.geometry(str(str(fWidthTotal) + "x" + str(fHeight))) 
    
    frame = tkinter.Frame(root)
    frame.config(bg=bgColor)
    frame.columnconfigure(0, pad=fPad)
    frame.columnconfigure(1, pad=fPad)

    leftFrame = tkinter.Frame(frame, width=int(fWidth/2), height=fHeight)
    leftFrame.grid_propagate(0)
    leftFrame.columnconfigure(0, weight=1)
    rightFrame = tkinter.Frame(frame, width=int(fWidth/2), height=fHeight)
    rightFrame.grid_propagate(0)
    rightFrame.columnconfigure(0, weight=1)

##################################################################################

    #For Distribution selection and main menu
    label1 = tkinter.Label(leftFrame, text="Menu1")
    label1.grid(row=0, sticky="nsew")

    menu1 = tkinter.Frame(leftFrame)
    
    menu1.rowconfigure(0, weight=1)
    #Dist Type
    distSelectLabel = tkinter.Label(menu1, text='Select Distribution Type')
    distSelectLabel.grid(row=0, column=0, sticky="nsew")
    distName = tkinter.StringVar()
    distName.set(distOptions[0])
    distCombo = tkinter.OptionMenu(menu1, distName, *distOptions)
    distCombo.grid(row=1, column=0)
    distSubmitButton = tkinter.Button(menu1, text="Submit", command=preview)
    distSubmitButton.grid(row=1, column=1)

    previewButton = tkinter.Button(menu1, text="Preview", command=preview)
    previewButton.grid(row=2, column=0)

    saveButton = tkinter.Button(menu1, text="Save", command=save)
    saveButton.grid(row=2, column=1)



    menu1.grid(row=1, sticky="nsew")


    #For Distribution statistics
    label2 = tkinter.Label(rightFrame, text="Menu2")
    label2.grid(row=0, sticky="nsew")

    menu2 = tkinter.Frame(rightFrame)
    
    menu2.grid(row=1)

    leftFrame.grid(row=0, column=0)
    rightFrame.grid(row=0, column=1)

    frame.pack()
    root.mainloop()

if __name__ == "__main__":
  main()

